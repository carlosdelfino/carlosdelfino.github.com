#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para copiar certificados (PDF, PNG, JPG/JPEG) da pasta pessoal
para a pasta 'certificados/' do site Jekyll e gerar um index.md que
indexa todos os certificados com thumbnails clicáveis.

Uso:
    python3 _scripts/copiar_certificados.py

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

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

ORIGEM = Path(
    os.path.expanduser(
        "~/Documentos/Documentos pessoais e currículo/Certificados"
    )
)

# Raiz do site Jekyll (diretório de onde o script é chamado)
SITE_ROOT = Path(__file__).resolve().parent.parent
DESTINO = SITE_ROOT / "certificados"
THUMBS_DIR = DESTINO / "thumbs"
INDEX_MD = DESTINO / "index.md"

EXTENSOES = {".pdf", ".png", ".jpg", ".jpeg"}

# Tamanho do thumbnail (largura em pixels)
THUMB_WIDTH = 300

# Manifesto JSON que mapeia hash SHA-256 → nome do arquivo no destino.
# Permite detectar duplicatas, renomeações e evitar cópias desnecessárias.
MANIFEST_FILE = DESTINO / ".manifest.json"


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


def carregar_manifesto() -> dict:
    """
    Carrega o manifesto existente.
    Formato: { "sha256hex": { "dest_name": str, "thumb_name": str } }
    """
    if MANIFEST_FILE.exists():
        try:
            with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def salvar_manifesto(manifesto: dict) -> None:
    """Persiste o manifesto em disco."""
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifesto, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def slugify(texto: str) -> str:
    """Converte um nome de arquivo em slug seguro para URLs."""
    # Remove extensão para slug, mas mantemos para o arquivo
    nome = Path(texto).stem
    # Normaliza unicode
    nome = unicodedata.normalize("NFKD", nome)
    nome = nome.encode("ascii", "ignore").decode("ascii")
    # Substitui caracteres não alfanuméricos por hífen
    nome = re.sub(r"[^\w\s-]", "", nome).strip().lower()
    nome = re.sub(r"[-\s]+", "-", nome)
    return nome


def nome_destino(arquivo: Path, subpasta: str = "") -> str:
    """Gera um nome de arquivo seguro para o destino, mantendo a extensão."""
    prefixo = ""
    if subpasta:
        prefixo = slugify(subpasta) + "--"
    slug = slugify(arquivo.name)
    ext = arquivo.suffix.lower()
    return f"{prefixo}{slug}{ext}"


def gerar_thumbnail(arquivo_src: Path, thumb_path: Path) -> bool:
    """
    Gera thumbnail para o certificado.
    - Para imagens (PNG/JPG/JPEG): redimensiona com ImageMagick (convert).
    - Para PDFs: extrai a primeira página como imagem com ImageMagick.
    Retorna True se o thumbnail foi gerado com sucesso.
    """
    thumb_path.parent.mkdir(parents=True, exist_ok=True)

    ext = arquivo_src.suffix.lower()
    try:
        if ext in (".png", ".jpg", ".jpeg"):
            subprocess.run(
                [
                    "convert",
                    str(arquivo_src),
                    "-thumbnail",
                    f"{THUMB_WIDTH}x",
                    "-quality", "85",
                    str(thumb_path),
                ],
                check=True,
                capture_output=True,
            )
        elif ext == ".pdf":
            # Converte a primeira página do PDF em PNG
            subprocess.run(
                [
                    "convert",
                    "-density", "150",
                    f"{arquivo_src}[0]",
                    "-thumbnail",
                    f"{THUMB_WIDTH}x",
                    "-quality", "85",
                    str(thumb_path),
                ],
                check=True,
                capture_output=True,
            )
        return thumb_path.exists()
    except FileNotFoundError:
        print(
            "⚠  ImageMagick ('convert') não encontrado. "
            "Instale com: sudo apt install imagemagick"
        )
        return False
    except subprocess.CalledProcessError as e:
        print(f"⚠  Erro ao gerar thumbnail de {arquivo_src.name}: {e}")
        return False


def titulo_legivel(nome_arquivo: str) -> str:
    """Gera um título legível a partir do nome do arquivo."""
    nome = Path(nome_arquivo).stem
    # Remove prefixo de subpasta (slug--) se existir
    if "--" in nome:
        nome = nome.split("--", 1)[1]
    # Substitui hifens e underscores por espaços
    nome = nome.replace("-", " ").replace("_", " ")
    # Capitaliza
    nome = nome.strip().title()
    return nome


def coletar_certificados() -> list[dict]:
    """
    Percorre a pasta de origem recursivamente e coleta os certificados.
    Retorna lista de dicts com informações de cada certificado.
    """
    certificados = []

    if not ORIGEM.exists():
        print(f"❌ Pasta de origem não encontrada: {ORIGEM}")
        return certificados

    for arquivo in ORIGEM.rglob("*"):
        if not arquivo.is_file():
            continue
        if arquivo.suffix.lower() not in EXTENSOES:
            continue

        # Determina subpasta relativa (para evitar colisão de nomes)
        relativo = arquivo.relative_to(ORIGEM)
        subpasta = str(relativo.parent) if relativo.parent != Path(".") else ""

        dest_name = nome_destino(arquivo, subpasta)
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

    # Ordena do mais novo para o mais antigo (data de modificação)
    certificados.sort(key=lambda c: c["mtime"], reverse=True)

    return certificados


def copiar_arquivos(certificados: list[dict]) -> dict:
    """
    Copia os certificados para a pasta de destino usando hash SHA-256
    para controle de conteúdo. Retorna o novo manifesto atualizado.

    Lógica:
    - Calcula SHA-256 de cada arquivo de origem.
    - Se o hash já existe no manifesto e o dest_name é o mesmo → pula
      (conteúdo idêntico, sem renomeação).
    - Se o hash já existe mas o dest_name mudou → renomeia no destino
      (arquivo renomeado na origem).
    - Se o hash é novo → copia o arquivo.
    - Arquivos com mesmo conteúdo (duplicatas) são ignorados: apenas
      a primeira ocorrência é mantida.
    """
    DESTINO.mkdir(parents=True, exist_ok=True)
    THUMBS_DIR.mkdir(parents=True, exist_ok=True)

    manifesto_antigo = carregar_manifesto()
    manifesto_novo: dict[str, dict] = {}
    hashes_vistos: set[str] = set()

    for cert in certificados:
        file_hash = sha256_file(cert["origem"])

        # Detecta duplicata por conteúdo dentro da mesma execução
        if file_hash in hashes_vistos:
            print(
                f"  ⚠ Duplicata ignorada (mesmo conteúdo): "
                f"{cert['dest_name']}"
            )
            continue
        hashes_vistos.add(file_hash)

        dest_path = DESTINO / cert["dest_name"]
        thumb_path = THUMBS_DIR / cert["thumb_name"]
        antigo = manifesto_antigo.get(file_hash)

        if antigo:
            antigo_dest = antigo["dest_name"]
            antigo_thumb = antigo.get("thumb_name")

            if antigo_dest == cert["dest_name"]:
                # Mesmo hash, mesmo nome → nada a fazer
                if dest_path.exists():
                    print(f"  → Inalterado (hash ok): {cert['dest_name']}")
                else:
                    # Arquivo sumiu do destino, recopia
                    shutil.copy2(cert["origem"], dest_path)
                    print(
                        f"  ✔ Re-copiado (faltava no destino): "
                        f"{cert['dest_name']}"
                    )
            else:
                # Mesmo conteúdo, nome diferente → renomeia
                antigo_path = DESTINO / antigo_dest
                if antigo_path.exists():
                    antigo_path.rename(dest_path)
                    print(
                        f"  ↻ Renomeado: {antigo_dest} → {cert['dest_name']}"
                    )
                else:
                    shutil.copy2(cert["origem"], dest_path)
                    print(
                        f"  ✔ Copiado (renomeado na origem): "
                        f"{cert['dest_name']}"
                    )
                # Renomeia thumbnail antigo se existir
                if antigo_thumb:
                    antigo_thumb_path = THUMBS_DIR / antigo_thumb
                    if antigo_thumb_path.exists():
                        if antigo_thumb != cert["thumb_name"]:
                            antigo_thumb_path.rename(thumb_path)
                            print(
                                f"  ↻ Thumb renomeado: "
                                f"{antigo_thumb} → {cert['thumb_name']}"
                            )
        else:
            # Hash novo → arquivo novo, copia
            shutil.copy2(cert["origem"], dest_path)
            print(f"  ✔ Copiado: {cert['dest_name']}")

        # Gera thumbnail se não existe
        if not thumb_path.exists():
            ok = gerar_thumbnail(cert["origem"], thumb_path)
            if ok:
                print(f"  🖼 Thumbnail: {cert['thumb_name']}")
            else:
                cert["thumb_name"] = None
        else:
            print(f"  → Thumbnail já existe: {cert['thumb_name']}")

        # Registra no novo manifesto
        manifesto_novo[file_hash] = {
            "dest_name": cert["dest_name"],
            "thumb_name": cert["thumb_name"],
        }

    return manifesto_novo


def sincronizar_destino(manifesto_novo: dict, manifesto_antigo: dict) -> None:
    """
    Remove do destino arquivos que não estão mais presentes na origem
    (foram deletados ou eram duplicatas eliminadas).
    """
    nomes_validos = {v["dest_name"] for v in manifesto_novo.values()}
    thumbs_validos = {
        v["thumb_name"] for v in manifesto_novo.values() if v.get("thumb_name")
    }
    # Arquivos extras para preservar
    preservar = {"index.md", ".manifest.json"}

    removidos = 0

    # Limpa certificados obsoletos
    if DESTINO.exists():
        for f in DESTINO.iterdir():
            if f.is_file() and f.name not in nomes_validos and f.name not in preservar:
                f.unlink()
                print(f"  🗑 Removido (obsoleto): {f.name}")
                removidos += 1

    # Limpa thumbnails obsoletos
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


def gerar_index(certificados: list[dict]) -> None:
    """Gera o arquivo index.md com a listagem de certificados."""

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

    # CSS inline para a galeria de thumbnails
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
    linhas.append("  top: 0; left: 0;")
    linhas.append("  width: 100%; height: 100%;")
    linhas.append("  background: rgba(0,0,0,0.8);")
    linhas.append("  z-index: 9999;")
    linhas.append("  justify-content: center;")
    linhas.append("  align-items: center;")
    linhas.append("}")
    linhas.append(".cert-modal-overlay.active {")
    linhas.append("  display: flex;")
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
    linhas.append(".cert-modal-content iframe,")
    linhas.append(".cert-modal-content img {")
    linhas.append("  width: 100%;")
    linhas.append("  height: 100%;")
    linhas.append("  border: none;")
    linhas.append("  object-fit: contain;")
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
    linhas.append(
        '  <button class="cert-modal-close" '
        'onclick="fecharModal()">&times;</button>'
    )
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
            arquivo_url = (
                "{{ site.baseurl }}/certificados/" + cert["dest_name"]
            )
            if cert["thumb_name"]:
                thumb_url = (
                    "{{ site.baseurl }}/certificados/thumbs/"
                    + cert["thumb_name"]
                )
            else:
                # Fallback: usar o próprio arquivo como thumb (para imagens)
                if ext in (".png", ".jpg", ".jpeg"):
                    thumb_url = arquivo_url
                else:
                    thumb_url = (
                        "{{ site.baseurl }}/images/"
                        "carlosdelfino-palestra-400x161.png"
                    )

            # Tipo de conteúdo para o modal
            if ext == ".pdf":
                tipo = "pdf"
            else:
                tipo = "img"

            linhas.append(f'<div class="certificado-card">')
            linhas.append(
                f'  <img src="{thumb_url}" '
                f'alt="{cert["titulo"]}" '
                f'onclick="abrirModal(\'{arquivo_url}\', \'{tipo}\')" '
                f'title="Clique para visualizar">'
            )
            linhas.append(f'  <div class="titulo">{cert["titulo"]}</div>')
            linhas.append(f"</div>")

    linhas.append("</div><!-- /.certificados-gallery -->")
    linhas.append("")

    # JavaScript do modal
    linhas.append("<script>")
    linhas.append("function abrirModal(url, tipo) {")
    linhas.append("  var overlay = document.getElementById('certModal');")
    linhas.append(
        "  var content = document.getElementById('certModalContent');"
    )
    linhas.append("  if (tipo === 'pdf') {")
    linhas.append(
        '    content.innerHTML = \'<iframe src="\' + url + \'"></iframe>\';'
    )
    linhas.append("  } else {")
    linhas.append(
        '    content.innerHTML = \'<img src="\' + url + \'" '
        'alt="Certificado">\';'
    )
    linhas.append("  }")
    linhas.append("  overlay.classList.add('active');")
    linhas.append("}")
    linhas.append("function fecharModal() {")
    linhas.append("  var overlay = document.getElementById('certModal');")
    linhas.append(
        "  var content = document.getElementById('certModalContent');"
    )
    linhas.append("  overlay.classList.remove('active');")
    linhas.append("  content.innerHTML = '';")
    linhas.append("}")
    linhas.append(
        "document.getElementById('certModal')"
        ".addEventListener('click', function(e) {"
    )
    linhas.append("  if (e.target === this) fecharModal();")
    linhas.append("});")
    linhas.append("document.addEventListener('keydown', function(e) {")
    linhas.append("  if (e.key === 'Escape') fecharModal();")
    linhas.append("});")
    linhas.append("</script>")
    linhas.append("")

    conteudo = "\n".join(linhas)

    with open(INDEX_MD, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"\n✅ index.md gerado em: {INDEX_MD}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"📂 Origem: {ORIGEM}")
    print(f"📂 Destino: {DESTINO}")
    print()

    certificados = coletar_certificados()

    if not certificados:
        print("Nenhum certificado encontrado.")
        return

    print(f"📄 {len(certificados)} certificado(s) encontrado(s).\n")

    manifesto_antigo = carregar_manifesto()

    print("--- Copiando arquivos (controle por hash SHA-256) ---")
    manifesto_novo = copiar_arquivos(certificados)

    print("\n--- Sincronizando destino ---")
    sincronizar_destino(manifesto_novo, manifesto_antigo)

    # Salva manifesto atualizado
    salvar_manifesto(manifesto_novo)
    print(f"\n📋 Manifesto salvo: {MANIFEST_FILE}")

    # Filtra certificados para o index: apenas os que estão no manifesto
    nomes_no_manifesto = {v["dest_name"] for v in manifesto_novo.values()}
    certificados_unicos = [
        c for c in certificados if c["dest_name"] in nomes_no_manifesto
    ]

    print(
        f"   {len(certificados_unicos)} certificado(s) únicos "
        f"(de {len(certificados)} encontrados).\n"
    )

    print("--- Gerando index.md ---")
    gerar_index(certificados_unicos)

    print(f"\n🎉 Concluído! {len(certificados_unicos)} certificados processados.")
    print(
        "   Lembre-se de adicionar '_scripts/' ao 'exclude' "
        "no _config.yml se ainda não estiver."
    )


if __name__ == "__main__":
    main()
