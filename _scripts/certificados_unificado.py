#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script unificado para processar e gerenciar certificados:
  1. Processa certificados escaneados no Severiano (rotação e concatenação de grades)
  2. Copia certificados processados para o site Jekyll com thumbnails
  3. Gera index.md com galeria de certificados
  4. Mantém manifesto para controle de conteúdo e duplicatas

Uso:
    python3 _scripts/certificados_unificado.py

O script deve ser executado a partir da raiz do site Jekyll.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
import unicodedata
from pathlib import Path
from datetime import datetime

from pypdf import PdfReader, PdfWriter

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

# Fonte dos certificados escaneados (para processamento)
ORIGEM_ESCANEADOS = Path(
    os.path.expanduser(
        "~/Documentos/Documentos pessoais e currículo/"
        "Certificados e Diplomas escaneados no Severiano/separados"
    )
)

# Fonte dos certificados existentes em subpastas (para processamento)
ORIGEM_SUBPASTAS = Path(
    os.path.expanduser(
        "~/Documentos/Documentos pessoais e currículo/Certificados"
    )
)

# Destino do processamento (certificados rotacionados e concatenados) - pasta temporária
DESTINO_TEMP = Path(
    os.path.expanduser(
        "~/Documentos/Documentos pessoais e currículo/"
        "Certificados/.temp_processados"
    )
)

# Fonte dos certificados já processados (para cópia ao site)
ORIGEM_PROCESSADOS = Path(
    os.path.expanduser(
        "~/Documentos/Documentos pessoais e currículo/Certificados"
    )
)

# Raiz do site Jekyll (diretório de onde o script é chamado)
SITE_ROOT = Path(__file__).resolve().parent.parent
DESTINO_SITE = SITE_ROOT / "certificados"
THUMBS_DIR = DESTINO_SITE / "thumbs"
INDEX_MD = DESTINO_SITE / "index.md"

# Extensões suportadas
EXTENSOES = {".pdf", ".png", ".jpg", ".jpeg"}

# Tamanho do thumbnail (largura em pixels)
THUMB_WIDTH = 300

# Sufixos de grade e rotação
SUFIXOS_GRADE = [" - grade", " - Grade", " - GRADE"]
SUFIXO_GIRAR = " - girar"

# Manifestos JSON
MANIFEST_PROCESSADOS = DESTINO_TEMP / ".manifest_processados.json"
MANIFEST_SITE = DESTINO_SITE / ".manifest.json"

# ---------------------------------------------------------------------------
# Funções auxiliares — hashing e manifesto
# ---------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    """Calcula o SHA-256 do conteúdo de um arquivo."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloco in iter(lambda: f.read(8192), b""):
            h.update(bloco)
    return h.hexdigest()


def carregar_manifesto(arquivo_manifesto: Path) -> dict:
    """Carrega o manifesto existente."""
    if arquivo_manifesto.exists():
        try:
            with open(arquivo_manifesto, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def salvar_manifesto(manifesto: dict, arquivo_manifesto: Path) -> None:
    """Persiste o manifesto em disco."""
    arquivo_manifesto.parent.mkdir(parents=True, exist_ok=True)
    with open(arquivo_manifesto, "w", encoding="utf-8") as f:
        json.dump(manifesto, f, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------------------
# Funções auxiliares — processamento de escaneados
# ---------------------------------------------------------------------------

def eh_arquivo_grade(nome: str) -> bool:
    """Retorna True se o nome do arquivo termina com sufixos de grade."""
    stem = Path(nome).stem
    return any(stem.endswith(sufixo.strip()) for sufixo in SUFIXOS_GRADE)


def precisa_girar(arquivo: Path) -> bool:
    """Retorna True se o arquivo precisa ser girado (está na pasta escaneados ou tem sufixo - girar)."""
    # Verifica se está na pasta de escaneados
    try:
        arquivo.relative_to(ORIGEM_ESCANEADOS)
        return True
    except ValueError:
        pass
    
    # Verifica se tem o sufixo - girar
    return arquivo.stem.endswith(SUFIXO_GIRAR.strip())


def nome_grade_para(arquivo: Path) -> list[Path]:
    """Dado um arquivo principal, retorna os possíveis caminhos dos arquivos grade."""
    return [arquivo.with_name(f"{arquivo.stem}{sufixo}{arquivo.suffix}") for sufixo in SUFIXOS_GRADE]


def nome_destino_processado(arquivo: Path, subpasta: str = "") -> Path:
    """Gera o caminho de destino mantendo a estrutura de subpastas na pasta temporária."""
    if subpasta:
        return DESTINO_TEMP / subpasta / arquivo.name
    return DESTINO_TEMP / arquivo.name


def rotacionar_e_unir(principal: Path, grades: list[Path] | None, destino: Path, girar: bool = True) -> None:
    """
    Processa o arquivo principal (e dos grades, se existirem), unindo-os em um único PDF de saída.
    Se girar=True, rotaciona 90° horário todas as páginas.
    """
    writer = PdfWriter()

    # Processa o arquivo principal
    reader_principal = PdfReader(str(principal))
    for page in reader_principal.pages:
        if girar:
            page.rotate(90)
        writer.add_page(page)

    # Processa os arquivos grade, se existirem
    if grades:
        for grade in grades:
            if grade.exists():
                reader_grade = PdfReader(str(grade))
                for page in reader_grade.pages:
                    if girar:
                        page.rotate(90)
                    writer.add_page(page)

    # Salva no destino
    destino.parent.mkdir(parents=True, exist_ok=True)
    with open(destino, "wb") as f:
        writer.write(f)


def coletar_pdfs_para_processar() -> list[dict]:
    """Percorre ambas as fontes recursivamente e coleta os PDFs para processar."""
    pdfs_para_processar = []

    # Fonte 1: Escaneados
    if ORIGEM_ESCANEADOS.exists():
        for arquivo in ORIGEM_ESCANEADOS.rglob("*"):
            if not arquivo.is_file():
                continue
            if arquivo.suffix.lower() != ".pdf":
                continue

            # Determina subpasta relativa
            relativo = arquivo.relative_to(ORIGEM_ESCANEADOS)
            subpasta = str(relativo.parent) if relativo.parent != Path(".") else ""

            pdfs_para_processar.append(
                {
                    "origem": arquivo,
                    "subpasta": f"escaneados/{subpasta}" if subpasta else "escaneados",
                    "destino": nome_destino_processado(arquivo, subpasta),
                    "mtime": arquivo.stat().st_mtime,
                }
            )

    # Fonte 2: Subpastas existentes (exceto Antes de 2025)
    if ORIGEM_SUBPASTAS.exists():
        for arquivo in ORIGEM_SUBPASTAS.rglob("*"):
            if not arquivo.is_file():
                continue
            if arquivo.suffix.lower() != ".pdf":
                continue
            # Ignora a pasta Antes de 2025 (já processados)
            if "Antes de 2025" in str(arquivo.parent):
                continue

            # Determina subpasta relativa
            relativo = arquivo.relative_to(ORIGEM_SUBPASTAS)
            subpasta = str(relativo.parent) if relativo.parent != Path(".") else ""

            pdfs_para_processar.append(
                {
                    "origem": arquivo,
                    "subpasta": subpasta,
                    "destino": nome_destino_processado(arquivo, subpasta),
                    "mtime": arquivo.stat().st_mtime,
                }
            )

    # Ordena do mais novo para o mais antigo
    pdfs_para_processar.sort(key=lambda p: p["mtime"], reverse=True)

    return pdfs_para_processar


def processar_escaneados(pdfs_para_processar: list[dict]) -> dict:
    """Processa os PDFs usando hash SHA-256 para controle de conteúdo."""
    manifesto_antigo = carregar_manifesto(MANIFEST_PROCESSADOS)
    manifesto_novo: dict[str, dict] = {}
    hashes_vistos: set[str] = set()
    
    processados = 0
    erros = 0
    pulados = 0

    for pdf_info in pdfs_para_processar:
        principal = pdf_info["origem"]
        subpasta = pdf_info["subpasta"]
        destino = pdf_info["destino"]
        
        # Verifica se é arquivo grade
        if eh_arquivo_grade(principal.name):
            continue
            
        # Busca arquivos grade correspondentes
        grade_paths = nome_grade_para(principal)
        grades_existentes = [path for path in grade_paths if path.exists()]
        tem_grade = len(grades_existentes) > 0
        
        # Calcula hash combinado
        hash_principal = sha256_file(principal)
        hashes_grades = [sha256_file(g) for g in grades_existentes]
        hash_combinado_str = f"{hash_principal}|{'|'.join(sorted(hashes_grades))}"
        hash_combinado = hashlib.sha256(hash_combinado_str.encode()).hexdigest()
        
        # Detecta duplicata por conteúdo
        if hash_combinado in hashes_vistos:
            print(f"  ⚠ Duplicata ignorada (mesmo conteúdo): {principal.name}")
            pulados += 1
            continue
        hashes_vistos.add(hash_combinado)
        
        # Verifica se já foi processado
        antigo = manifesto_antigo.get(hash_combinado)
        if antigo and antigo.get("dest_name") == str(destino.relative_to(DESTINO_TEMP)):
            if destino.exists():
                print(f"  → Inalterado (já processado): {principal.name}")
                manifesto_novo[hash_combinado] = antigo
                processados += 1
                continue
        
        try:
            # Verifica se precisa girar
            deve_girar = precisa_girar(principal)
            rotacionar_e_unir(principal, grades_existentes if tem_grade else None, destino, girar=deve_girar)
            
            acao = "girado" if deve_girar else "copiado"
            if tem_grade:
                nomes_grades = [g.name for g in grades_existentes]
                print(f"  ✔ {principal.name} (+{', '.join(nomes_grades)}) [{subpasta or 'raiz'}] - {acao}")
            else:
                print(f"  ✔ {principal.name} [{subpasta or 'raiz'}] - {acao}")
            
            processados += 1
            
            # Registra no manifesto
            manifesto_novo[hash_combinado] = {
                "dest_name": str(destino.relative_to(DESTINO_TEMP)),
                "subpasta": subpasta,
            }
            
        except Exception as e:
            print(f"  ❌ Erro ao processar {principal.name}: {e}")
            erros += 1
    
    print(f"\n📊 Resumo processamento: {processados} processado(s), {pulados} pulado(s), {erros} erro(s)")
    return manifesto_novo


def limpar_destino_temp(pdfs_para_processar: list[dict], manifesto_novo: dict) -> None:
    """Remove do destino temporário arquivos que não existem mais na origem."""
    nomes_validos = set()
    for pdf_info in pdfs_para_processar:
        if not eh_arquivo_grade(pdf_info["origem"].name):
            nomes_validos.add(str(pdf_info["destino"].relative_to(DESTINO_TEMP)))
    
    preservar = {".manifest_processados.json"}
    removidos = 0
    
    if DESTINO_TEMP.exists():
        for item in DESTINO_TEMP.rglob("*"):
            if item.is_file():
                nome_rel = str(item.relative_to(DESTINO_TEMP))
                if nome_rel not in nomes_validos and nome_rel not in preservar:
                    if eh_arquivo_grade(item.name):
                        item.unlink()
                        print(f"  🗑 Removido (arquivo grade não deveria existir): {nome_rel}")
                        removidos += 1
                    elif nome_rel not in {v["dest_name"] for v in manifesto_novo.values()}:
                        item.unlink()
                        print(f"  🗑 Removido (obsoleto): {nome_rel}")
                        removidos += 1
            elif item.is_dir() and item != DESTINO_TEMP:
                try:
                    if not any(item.iterdir()):
                        item.rmdir()
                        print(f"  🗑 Diretório vazio removido: {item.relative_to(DESTINO_TEMP)}")
                        removidos += 1
                except OSError:
                    pass
    
    if removidos:
        print(f"  🧹 {removidos} arquivo(s)/diretório(s) obsoleto(s) removido(s).")
    else:
        print("  ✓ Nenhum arquivo obsoleto encontrado.")

# ---------------------------------------------------------------------------
# Funções auxiliares — cópia para site Jekyll
# ---------------------------------------------------------------------------

def slugify(texto: str) -> str:
    """Converte um nome de arquivo em slug seguro para URLs."""
    nome = Path(texto).stem
    nome = unicodedata.normalize("NFKD", nome)
    nome = nome.encode("ascii", "ignore").decode("ascii")
    nome = re.sub(r"[^\w\s-]", "", nome).strip().lower()
    nome = re.sub(r"[-\s]+", "-", nome)
    return nome


def nome_destino_site(arquivo: Path, subpasta: str = "") -> str:
    """Gera um nome de arquivo seguro para o destino do site."""
    prefixo = ""
    if subpasta:
        prefixo = slugify(subpasta) + "--"
    slug = slugify(arquivo.name)
    ext = arquivo.suffix.lower()
    return f"{prefixo}{slug}{ext}"


def gerar_thumbnail(arquivo_src: Path, thumb_path: Path) -> bool:
    """Gera thumbnail para o certificado."""
    thumb_path.parent.mkdir(parents=True, exist_ok=True)

    ext = arquivo_src.suffix.lower()
    try:
        if ext in (".png", ".jpg", ".jpeg"):
            subprocess.run(
                ["convert", str(arquivo_src), "-thumbnail", f"{THUMB_WIDTH}x", "-quality", "85", str(thumb_path)],
                check=True, capture_output=True,
            )
        elif ext == ".pdf":
            subprocess.run(
                ["convert", "-density", "150", f"{arquivo_src}[0]", "-thumbnail", f"{THUMB_WIDTH}x", "-quality", "85", str(thumb_path)],
                check=True, capture_output=True,
            )
        return thumb_path.exists()
    except FileNotFoundError:
        print("⚠  ImageMagick ('convert') não encontrado. Instale com: sudo apt install imagemagick")
        return False
    except subprocess.CalledProcessError as e:
        print(f"⚠  Erro ao gerar thumbnail de {arquivo_src.name}: {e}")
        return False


def titulo_legivel(nome_arquivo: str) -> str:
    """Gera um título legível a partir do nome do arquivo."""
    nome = Path(nome_arquivo).stem
    if "--" in nome:
        nome = nome.split("--", 1)[1]
    nome = nome.replace("-", " ").replace("_", " ")
    nome = nome.strip().title()
    return nome


def limpar_pasta_temporaria() -> None:
    """Remove a pasta temporária após o processamento."""
    if DESTINO_TEMP.exists():
        try:
            import shutil
            shutil.rmtree(DESTINO_TEMP)
            print(f"  🗑 Pasta temporária removida: {DESTINO_TEMP}")
        except Exception as e:
            print(f"  ⚠ Erro ao remover pasta temporária: {e}")


def coletar_certificados_site() -> list[dict]:
    """Percorre a pasta temporária (com arquivos processados) e coleta os certificados para o site."""
    certificados = []

    if not DESTINO_TEMP.exists():
        print(f"❌ Pasta temporária de processados não encontrada: {DESTINO_TEMP}")
        return certificados

    for arquivo in DESTINO_TEMP.rglob("*"):
        if not arquivo.is_file():
            continue
        if arquivo.suffix.lower() not in EXTENSOES:
            continue
        # Ignora arquivos grade - eles já foram concatenados aos principais
        if eh_arquivo_grade(arquivo.name):
            continue

        relativo = arquivo.relative_to(DESTINO_TEMP)
        subpasta = str(relativo.parent) if relativo.parent != Path(".") else ""

        dest_name = nome_destino_site(arquivo, subpasta)
        thumb_name = Path(dest_name).stem + ".png"

        certificados.append(
            {
                "origem": arquivo,
                "dest_name": dest_name,
                "thumb_name": thumb_name,
                "subpasta": subpasta,
                "titulo": titulo_legivel(dest_name),
                "extensao": arquivo.suffix.lower(),
                "mtime": arquivo.stat().st_mtime,
            }
        )

    certificados.sort(key=lambda c: c["mtime"], reverse=True)
    return certificados


def copiar_arquivos_site(certificados: list[dict]) -> dict:
    """Copia os certificados para o site usando hash SHA-256 para controle."""
    DESTINO_SITE.mkdir(parents=True, exist_ok=True)
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)

    manifesto_antigo = carregar_manifesto(MANIFEST_SITE)
    manifesto_novo: dict[str, dict] = {}
    hashes_vistos: set[str] = set()

    for cert in certificados:
        file_hash = sha256_file(cert["origem"])

        if file_hash in hashes_vistos:
            print(f"  ⚠ Duplicata ignorada (mesmo conteúdo): {cert['dest_name']}")
            continue
        hashes_vistos.add(file_hash)

        dest_path = DESTINO_SITE / cert["dest_name"]
        thumb_path = THUMBS_DIR / cert["thumb_name"]
        antigo = manifesto_antigo.get(file_hash)

        if antigo:
            antigo_dest = antigo["dest_name"]
            antigo_thumb = antigo.get("thumb_name")

            if antigo_dest == cert["dest_name"]:
                if dest_path.exists():
                    print(f"  → Inalterado (hash ok): {cert['dest_name']}")
                else:
                    shutil.copy2(cert["origem"], dest_path)
                    print(f"  ✔ Re-copiado (faltava no destino): {cert['dest_name']}")
            else:
                antigo_path = DESTINO_SITE / antigo_dest
                if antigo_path.exists():
                    antigo_path.rename(dest_path)
                    print(f"  ↻ Renomeado: {antigo_dest} → {cert['dest_name']}")
                else:
                    shutil.copy2(cert["origem"], dest_path)
                    print(f"  ✔ Copiado (renomeado na origem): {cert['dest_name']}")
                if antigo_thumb:
                    antigo_thumb_path = THUMBS_DIR / antigo_thumb
                    if antigo_thumb_path.exists():
                        if antigo_thumb != cert["thumb_name"]:
                            antigo_thumb_path.rename(thumb_path)
                            print(f"  ↻ Thumb renomeado: {antigo_thumb} → {cert['thumb_name']}")
        else:
            shutil.copy2(cert["origem"], dest_path)
            print(f"  ✔ Copiado: {cert['dest_name']}")

        if not thumb_path.exists():
            ok = gerar_thumbnail(cert["origem"], thumb_path)
            if ok:
                print(f"  🖼 Thumbnail: {cert['thumb_name']}")
            else:
                cert["thumb_name"] = None
        else:
            print(f"  → Thumbnail já existe: {cert['thumb_name']}")

        manifesto_novo[file_hash] = {
            "dest_name": cert["dest_name"],
            "thumb_name": cert["thumb_name"],
        }

    return manifesto_novo


def sincronizar_destino_site(manifesto_novo: dict, manifesto_antigo: dict) -> None:
    """Remove do destino arquivos que não estão mais presentes na origem."""
    nomes_validos = {v["dest_name"] for v in manifesto_novo.values()}
    thumbs_validos = {v["thumb_name"] for v in manifesto_novo.values() if v.get("thumb_name")}
    preservar = {"index.md", ".manifest.json"}

    removidos = 0

    if DESTINO_SITE.exists():
        for f in DESTINO_SITE.iterdir():
            if f.is_file() and f.name not in nomes_validos and f.name not in preservar:
                f.unlink()
                print(f"  🗑 Removido (obsoleto): {f.name}")
                removidos += 1

    if THUMBS_DIR.exists():
        for f in THUMBS_DIR.iterdir():
            if f.is_file() and f.name not in thumbs_validos:
                f.unlink()
                print(f"  🗑 Thumb removido: {f.name}")
                removidos += 1

    if removidos:
        print(f"  🧹 {removidos} arquivo(s) obsoleto(s) removido(s).")
    else:
        print("  ✓ Nenhum arquivo obsoleto encontrado.")


def gerar_index_site(certificados: list[dict]) -> None:
    """Gera o arquivo index.md com a listagem de certificados para o site."""
    linhas = []

    # Front matter Jekyll
    linhas.append("---")
    linhas.append("layout: index")
    linhas.append("title: Certificados")
    linhas.append("permalink: /certificados/")
    linhas.append("share: true")
    linhas.append("toc: false")
    linhas.append("comments: false")
    linhas.append("ads:")
    linhas.append("  show: true")
    linhas.append("image:")
    linhas.append("  feature: carlosdelfino-palestra-400x161.png")
    linhas.append("---")
    linhas.append("")
    linhas.append(
        "Aqui estão listados meus certificados de cursos, "
        "treinamentos e eventos que participei."
    )
    linhas.append("")
    linhas.append("<!--more-->")
    linhas.append("")

    # CSS inline para a galeria
    linhas.append("<style>")
    linhas.append(".certificados-gallery {")
    linhas.append("  display: flex;")
    linhas.append("  flex-wrap: wrap;")
    linhas.append("  gap: 1.5rem;")
    linhas.append("  justify-content: center;")
    linhas.append("  margin: 2rem 0;")
    linhas.append("}")
    linhas.append(".certificado-card {")
    linhas.append("  width: 280px;")
    linhas.append("  border: 1px solid #ddd;")
    linhas.append("  border-radius: 6px;")
    linhas.append("  overflow: hidden;")
    linhas.append("  box-shadow: 0 2px 6px rgba(0,0,0,0.1);")
    linhas.append("  transition: transform 0.2s, box-shadow 0.2s;")
    linhas.append("  background: #fff;")
    linhas.append("  text-align: center;")
    linhas.append("}")
    linhas.append(".certificado-card:hover {")
    linhas.append("  transform: translateY(-4px);")
    linhas.append("  box-shadow: 0 6px 16px rgba(0,0,0,0.15);")
    linhas.append("}")
    linhas.append(".certificado-card img {")
    linhas.append("  width: 100%;")
    linhas.append("  height: 200px;")
    linhas.append("  object-fit: cover;")
    linhas.append("  cursor: pointer;")
    linhas.append("}")
    linhas.append(".certificado-card .titulo {")
    linhas.append("  padding: 0.75rem;")
    linhas.append("  font-size: 0.85rem;")
    linhas.append("  font-weight: 600;")
    linhas.append("  color: #333;")
    linhas.append("}")
    linhas.append("/* Modal/Lightbox para exibir o certificado */")
    linhas.append(".cert-modal-overlay {")
    linhas.append("  display: none;")
    linhas.append("  position: fixed;")
    linhas.append("  top: 0;")
    linhas.append("  left: 0;")
    linhas.append("  right: 0;")
    linhas.append("  bottom: 0;")
    linhas.append("  width: 100vw;")
    linhas.append("  height: 100vh;")
    linhas.append("  background: rgba(0,0,0,0.8);")
    linhas.append("  z-index: 99999;")
    linhas.append("  justify-content: center;")
    linhas.append("  align-items: center;")
    linhas.append("}")
    linhas.append(".cert-modal-overlay.active {")
    linhas.append("  display: flex;")
    linhas.append("}")
    linhas.append("body.cert-modal-open {")
    linhas.append("  overflow: hidden;")
    linhas.append("}")
    linhas.append(".cert-modal-content {")
    linhas.append("  position: relative;")
    linhas.append("  width: 90%;")
    linhas.append("  max-width: 900px;")
    linhas.append("  height: 85vh;")
    linhas.append("  background: #fff;")
    linhas.append("  border-radius: 8px;")
    linhas.append("  overflow: hidden;")
    linhas.append("}")
    linhas.append(".cert-modal-content object,")
    linhas.append(".cert-modal-content embed,")
    linhas.append(".cert-modal-content iframe,")
    linhas.append(".cert-modal-content img {")
    linhas.append("  width: 100%;")
    linhas.append("  height: 100%;")
    linhas.append("  border: none;")
    linhas.append("  display: block;")
    linhas.append("}")
    linhas.append(".cert-modal-content img {")
    linhas.append("  object-fit: contain;")
    linhas.append("}")
    linhas.append(".cert-modal-fallback {")
    linhas.append("  text-align: center;")
    linhas.append("  padding: 2rem;")
    linhas.append("}")
    linhas.append(".cert-modal-fallback a {")
    linhas.append("  color: #448dd6;")
    linhas.append("  font-size: 1.1rem;")
    linhas.append("  font-weight: 600;")
    linhas.append("}")
    linhas.append(".cert-modal-close {")
    linhas.append("  position: absolute;")
    linhas.append("  top: 10px; right: 16px;")
    linhas.append("  font-size: 2rem;")
    linhas.append("  color: #fff;")
    linhas.append("  background: rgba(0,0,0,0.5);")
    linhas.append("  border: none;")
    linhas.append("  border-radius: 50%;")
    linhas.append("  width: 40px; height: 40px;")
    linhas.append("  cursor: pointer;")
    linhas.append("  z-index: 10000;")
    linhas.append("  display: flex;")
    linhas.append("  align-items: center;")
    linhas.append("  justify-content: center;")
    linhas.append("  line-height: 1;")
    linhas.append("}")
    linhas.append("</style>")
    linhas.append("")

    # Modal container
    linhas.append('<!-- Modal para exibir certificado -->')
    linhas.append('<div class="cert-modal-overlay" id="certModal">')
    linhas.append('  <button class="cert-modal-close" onclick="fecharModal()">&times;</button>')
    linhas.append('  <div class="cert-modal-content" id="certModalContent">')
    linhas.append("  </div>")
    linhas.append("</div>")
    linhas.append("")

    # Galeria de certificados
    linhas.append('<div class="certificados-gallery">')

    # Agrupa por subpasta
    subpastas: dict[str, list[dict]] = {}
    for cert in certificados:
        chave = cert["subpasta"] or "Recentes"
        subpastas.setdefault(chave, []).append(cert)

    for grupo, certs in subpastas.items():
        for cert in certs:
            ext = cert["extensao"]
            arquivo_url = "{{ site.baseurl }}/certificados/" + cert["dest_name"]
            if cert["thumb_name"]:
                thumb_url = "{{ site.baseurl }}/certificados/thumbs/" + cert["thumb_name"]
            else:
                if ext in (".png", ".jpg", ".jpeg"):
                    thumb_url = arquivo_url
                else:
                    thumb_url = "{{ site.baseurl }}/images/carlosdelfino-palestra-400x161.png"

            if ext == ".pdf":
                tipo = "pdf"
            else:
                tipo = "img"

            linhas.append(f'<div class="certificado-card">')
            linhas.append(f'  <img src="{thumb_url}" alt="{cert["titulo"]}" onclick="abrirModal(\'{arquivo_url}\', \'{tipo}\')" title="Clique para visualizar">')
            linhas.append(f'  <div class="titulo">{cert["titulo"]}</div>')
            linhas.append(f"</div>")

    linhas.append("</div><!-- /.certificados-gallery -->")
    linhas.append("")

    # JavaScript do modal
    linhas.append("<script>")
    linhas.append("function abrirModal(url, tipo) {")
    linhas.append("  var overlay = document.getElementById('certModal');")
    linhas.append("  var content = document.getElementById('certModalContent');")
    linhas.append("  if (tipo === 'pdf') {")
    linhas.append('    content.innerHTML = \'<object data="\' + url + \'" type="application/pdf" width="100%" height="100%"><p class="cert-modal-fallback">Seu navegador não suporta visualização de PDF embutido. <a href="\' + url + \'" target="_blank">Clique aqui para abrir o certificado</a></p></object>\';')
    linhas.append("  } else {")
    linhas.append('    content.innerHTML = \'<img src="\' + url + \'" alt="Certificado">\';')
    linhas.append("  }")
    linhas.append("  overlay.classList.add('active');")
    linhas.append("  document.body.classList.add('cert-modal-open');")
    linhas.append("}")
    linhas.append("function fecharModal() {")
    linhas.append("  var overlay = document.getElementById('certModal');")
    linhas.append("  var content = document.getElementById('certModalContent');")
    linhas.append("  overlay.classList.remove('active');")
    linhas.append("  document.body.classList.remove('cert-modal-open');")
    linhas.append("  content.innerHTML = '';")
    linhas.append("}")
    linhas.append("document.addEventListener('DOMContentLoaded', function() {")
    linhas.append("  var modal = document.getElementById('certModal');")
    linhas.append("  if (modal && modal.parentNode !== document.body) {")
    linhas.append("    document.body.appendChild(modal);")
    linhas.append("  }")
    linhas.append("  modal.addEventListener('click', function(e) {")
    linhas.append("    if (e.target === this) fecharModal();")
    linhas.append("  });")
    linhas.append("});")
    linhas.append("document.addEventListener('keydown', function(e) {")
    linhas.append("  if (e.key === 'Escape') fecharModal();")
    linhas.append("});")
    linhas.append("</script>")
    linhas.append("")

    conteudo = "\n".join(linhas)

    with open(INDEX_MD, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"✅ index.md gerado em: {INDEX_MD}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("🚀 Script Unificado de Certificados")
    print("=" * 50)
    
    # ETAPA 1: Processar certificados (escaneados + subpastas)
    print("\n📂 ETAPA 1: Processando certificados")
    print(f"📂 Fonte escaneados: {ORIGEM_ESCANEADOS}")
    print(f"📂 Fonte subpastas: {ORIGEM_SUBPASTAS}")
    print(f"📂 Destino temporário: {DESTINO_TEMP}")
    print()

    if not ORIGEM_ESCANEADOS.exists() and not ORIGEM_SUBPASTAS.exists():
        print(f"❌ Nenhuma fonte de certificados encontrada")
    else:
        DESTINO_TEMP.mkdir(parents=True, exist_ok=True)
        pdfs_para_processar = coletar_pdfs_para_processar()
        
        if pdfs_para_processar:
            principais = [p for p in pdfs_para_processar if not eh_arquivo_grade(p["origem"].name)]
            print(f"📄 {len(pdfs_para_processar)} PDF(s) encontrado(s), {len(principais)} principal(is).")
            
            manifesto_antigo = carregar_manifesto(MANIFEST_PROCESSADOS)
            print("--- Processando arquivos (controle por hash SHA-256) ---")
            manifesto_novo = processar_escaneados(principais)
            
            salvar_manifesto(manifesto_novo, MANIFEST_PROCESSADOS)
            print(f"\n📋 Manifesto de processados salvo: {MANIFEST_PROCESSADOS}")
            
            print("\n--- Limpando arquivos obsoletos ---")
            limpar_destino_temp(pdfs_para_processar, manifesto_novo)
        else:
            print("Nenhum PDF encontrado para processar.")

    # ETAPA 2: Copiar para site Jekyll
    print("\n📂 ETAPA 2: Copiando para site Jekyll")
    print(f"📂 Origem temporária: {DESTINO_TEMP}")
    print(f"📂 Destino site: {DESTINO_SITE}")
    print()

    if not DESTINO_TEMP.exists():
        print(f"❌ Pasta temporária de processados não encontrada: {DESTINO_TEMP}")
    else:
        certificados = coletar_certificados_site()
        
        if certificados:
            print(f"📄 {len(certificados)} certificado(s) encontrado(s).")
            
            manifesto_antigo = carregar_manifesto(MANIFEST_SITE)
            print("--- Copiando arquivos (controle por hash SHA-256) ---")
            manifesto_novo = copiar_arquivos_site(certificados)
            
            print("\n--- Sincronizando destino ---")
            sincronizar_destino_site(manifesto_novo, manifesto_antigo)
            
            salvar_manifesto(manifesto_novo, MANIFEST_SITE)
            print(f"\n📋 Manifesto do site salvo: {MANIFEST_SITE}")
            
            nomes_no_manifesto = {v["dest_name"] for v in manifesto_novo.values()}
            certificados_unicos = [c for c in certificados if c["dest_name"] in nomes_no_manifesto]
            
            print(f"\n--- Gerando index.md ---")
            gerar_index_site(certificados_unicos)
        else:
            print("Nenhum certificado encontrado para copiar.")

    # ETAPA 3: Limpar pasta temporária
    print("\n--- Limpando pasta temporária ---")
    limpar_pasta_temporaria()

    print("\n🎉 Script unificado concluído com sucesso!")
    print("   Lembre-se de adicionar '_scripts/' ao 'exclude' no _config.yml se ainda não estiver.")


if __name__ == "__main__":
    main()
