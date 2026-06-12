#!/bin/bash
#
# Script simplificado para executar o processamento de certificados
# Versão compacta para execução rápida
#
# Uso:
#   ./_scripts/certificados.sh [--high --file arquivo.pdf]
#
# Opções:
#   --high      Gerar imagem em alta resolução da primeira página de um PDF
#   --file      Nome do arquivo PDF para gerar imagem em alta resolução (requer --high)
#
# Notas:
#   - O script corrige automaticamente nomes no formato dd-mm-yyyy para yyyy-mm-dd
#   - Os certificados são ordenados por data (mais recente primeiro) no index.md
#

echo "🚀 Processando certificados..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/certificados_unificado.py"

# Verifica dependências básicas
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado"
    exit 1
fi

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "❌ Script unificado não encontrado"
    exit 1
fi

# Muda para o diretório raiz
cd "$PROJECT_ROOT" || exit 1

# Executa o script passando todos os argumentos
if python3 "$PYTHON_SCRIPT" "$@"; then
    echo ""
    echo "✅ Certificados processados com sucesso!"
    echo "📁 Verifique: certificados/index.md"
    if [[ " $* " =~ " --high " ]]; then
        echo "🔍 Imagens em alta resolução em: certificados/high/"
    fi
else
    echo ""
    echo "❌ Erro no processamento"
    exit 1
fi
