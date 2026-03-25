#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# executar_escaneados.sh
#
# Cria (ou reutiliza) um virtualenv Python, instala pypdf e executa
# o script processar_escaneados.py.
#
# Uso:
#   bash _scripts/executar_escaneados.sh
#
# Pode ser executado de qualquer lugar; o script se ajusta automaticamente
# para a raiz do site Jekyll.
# ---------------------------------------------------------------------------

set -euo pipefail

# ---- Diretórios -----------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$SITE_ROOT/venv"
PYTHON_SCRIPT="$SCRIPT_DIR/processar_escaneados.py"

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

# python3-venv
if ! python3 -m venv --help &>/dev/null; then
    error "Módulo venv não disponível. Instale com: sudo apt install python3-venv"
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
info "Instalando/atualizando pypdf..."
pip install --quiet --upgrade pip
pip install --quiet --upgrade pypdf
info "pypdf instalado."

# ---- Executar o script principal ------------------------------------------
echo ""
info "============================================="
info "  Executando processar_escaneados.py"
info "============================================="
echo ""

python "$PYTHON_SCRIPT"

# ---- Finalização ----------------------------------------------------------
echo ""
info "============================================="
info "  Script finalizado com sucesso!"
info "============================================="
