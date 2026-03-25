#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para processar certificados escaneados no Severiano:
  1. Lê os PDFs da pasta de origem (separados/).
  2. Gira cada página 90° no sentido horário.
  3. Se existir um arquivo companheiro com "- grade" no nome,
     une os dois (principal primeiro, grade depois).
  4. Copia o resultado para a pasta de destino (Antes de 2025/).

Uso:
    python3 _scripts/processar_escaneados.py

Dependência externa: pypdf
"""

import os
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

ORIGEM = Path(
    os.path.expanduser(
        "~/Documentos/Documentos pessoais e currículo/"
        "Certificados e Diplomas escaneados no Severiano/separados"
    )
)

DESTINO = Path(
    os.path.expanduser(
        "~/Documentos/Documentos pessoais e currículo/"
        "Certificados/Antes de 2025"
    )
)

SUFIXO_GRADE = " - grade"


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------

def eh_arquivo_grade(nome: str) -> bool:
    """Retorna True se o nome do arquivo (sem extensão) termina com '- grade'."""
    stem = Path(nome).stem
    return stem.endswith(SUFIXO_GRADE.strip())


def nome_grade_para(arquivo: Path) -> Path:
    """Dado um arquivo principal, retorna o caminho esperado do arquivo grade."""
    return arquivo.with_name(f"{arquivo.stem}{SUFIXO_GRADE}{arquivo.suffix}")


def rotacionar_e_unir(principal: Path, grade: Path | None, destino: Path) -> None:
    """
    Rotaciona 90° horário todas as páginas do arquivo principal (e do grade,
    se existir), unindo-os em um único PDF de saída.
    """
    writer = PdfWriter()

    # Processa o arquivo principal
    reader_principal = PdfReader(str(principal))
    for page in reader_principal.pages:
        page.rotate(90)
        writer.add_page(page)

    # Processa o arquivo grade, se existir
    if grade and grade.exists():
        reader_grade = PdfReader(str(grade))
        for page in reader_grade.pages:
            page.rotate(90)
            writer.add_page(page)

    # Salva no destino
    destino.parent.mkdir(parents=True, exist_ok=True)
    with open(destino, "wb") as f:
        writer.write(f)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"📂 Origem:  {ORIGEM}")
    print(f"📂 Destino: {DESTINO}")
    print()

    if not ORIGEM.exists():
        print(f"❌ Pasta de origem não encontrada: {ORIGEM}")
        sys.exit(1)

    DESTINO.mkdir(parents=True, exist_ok=True)

    # Coleta todos os PDFs da origem
    todos_pdfs = sorted(
        [f for f in ORIGEM.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"]
    )

    if not todos_pdfs:
        print("Nenhum PDF encontrado na pasta de origem.")
        return

    # Identifica os arquivos principais (não-grade)
    principais = [f for f in todos_pdfs if not eh_arquivo_grade(f.name)]
    grades_usados: set[str] = set()

    print(f"📄 {len(todos_pdfs)} PDF(s) encontrado(s), "
          f"{len(principais)} principal(is).\n")

    processados = 0
    erros = 0

    for arq in principais:
        grade_path = nome_grade_para(arq)
        tem_grade = grade_path.exists()

        destino_path = DESTINO / arq.name

        try:
            rotacionar_e_unir(arq, grade_path if tem_grade else None, destino_path)

            if tem_grade:
                grades_usados.add(grade_path.name)
                print(f"  ✔ {arq.name}  (+grade)  → {destino_path.name}")
            else:
                print(f"  ✔ {arq.name}  → {destino_path.name}")

            processados += 1

        except Exception as e:
            print(f"  ❌ Erro ao processar {arq.name}: {e}")
            erros += 1

    # Alerta sobre grades órfãos (sem principal correspondente)
    grades_sem_par = [
        f.name for f in todos_pdfs
        if eh_arquivo_grade(f.name) and f.name not in grades_usados
    ]
    if grades_sem_par:
        print(f"\n⚠  {len(grades_sem_par)} arquivo(s) grade sem principal:")
        for g in grades_sem_par:
            print(f"     - {g}")

    print(f"\n🎉 Concluído! {processados} certificado(s) processado(s)"
          f"{f', {erros} erro(s)' if erros else ''}.")


if __name__ == "__main__":
    main()
