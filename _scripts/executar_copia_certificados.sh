#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# executar_certificados.sh
#
# Cria (ou reutiliza) um virtualenv Python, instala dependências listadas
# em requirements.txt e executa o script copiar_certificados.py.
#
# Uso:
#   bash _scripts/executar_certificados.sh
#
# Pode ser executado de qualquer lugar; o script se ajusta automaticamente
# para a raiz do site Jekyll.
# ---------------------------------------------------------------------------

set -euo pipefail

# ---- Diretórios -----------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$SITE_ROOT/venv"
REQUIREMENTS="$SCRIPT_DIR/requirements.txt"
PYTHON_SCRIPT="$SCRIPT_DIR/copiar_certificados.py"

# ---- Cores para output ----------------------------------------------------
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

info()  { echo -e "${GREEN}[INFO]${NC}  $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
error() { echo -e "${RED}[ERRO]${NC}  $*"; exit 1; }

# ---- Verificar dependências do sistema ------------------------------------
info "Verificando dependências do sistema..."

# Python 3
if ! command -v python3 &>/dev/null; then
    error "python3 não encontrado. Instale com: sudo apt install python3"
fi
PYTHON_VERSION=$(python3 --version 2>&1)
info "Python encontrado: $PYTHON_VERSION"

# python3-venv (necessário para criar o virtualenv)
if ! python3 -m venv --help &>/dev/null; then
    error "Módulo venv não disponível. Instale com: sudo apt install python3-venv"
fi

# ImageMagick (convert) — necessário para gerar thumbnails
if ! command -v convert &>/dev/null; then
    warn "ImageMagick ('convert') não encontrado."
    warn "Os thumbnails NÃO serão gerados."
    warn "Para instalar: sudo apt install imagemagick"
    echo ""
    read -rp "Deseja continuar mesmo assim? [s/N] " resposta
    if [[ ! "$resposta" =~ ^[sS]$ ]]; then
        info "Abortado pelo usuário."
        exit 0
    fi
else
    info "ImageMagick encontrado: $(convert --version | head -1)"
fi

# ---- Criar / reutilizar virtualenv ---------------------------------------
if [ ! -d "$VENV_DIR" ]; then
    info "Criando virtualenv em $VENV_DIR ..."
    python3 -m venv "$VENV_DIR"
    info "Virtualenv criado."
else
    info "Virtualenv já existe em $VENV_DIR"
fi

# Ativa o virtualenv
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"
info "Virtualenv ativado ($(python --version))"

# ---- Instalar / atualizar dependências ------------------------------------
if [ -f "$REQUIREMENTS" ]; then
    # Verifica se o requirements.txt tem linhas não-comentadas
    if grep -qvE '^\s*(#|$)' "$REQUIREMENTS" 2>/dev/null; then
        info "Instalando dependências de $REQUIREMENTS ..."
        pip install --quiet --upgrade pip
        pip install --quiet -r "$REQUIREMENTS"
        info "Dependências instaladas."
    else
        info "requirements.txt sem dependências externas — nada a instalar."
    fi
else
    warn "Arquivo requirements.txt não encontrado em $SCRIPT_DIR"
fi

# ---- Executar o script principal ------------------------------------------
echo ""
info "============================================="
info "  Executando copiar_certificados.py"
info "============================================="
echo ""

python "$PYTHON_SCRIPT"

# ---- Finalização ----------------------------------------------------------
echo ""
info "============================================="
info "  Script finalizado com sucesso!"
info "============================================="
info "Arquivos gerados em: $SITE_ROOT/certificados/"
info "Para visualizar localmente: jekyll serve"
