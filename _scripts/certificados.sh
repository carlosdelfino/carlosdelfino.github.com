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

echo "🚀 Processando certificados..."

# Verifica dependências básicas
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado"
    exit 1
fi

if [ ! -f "_scripts/certificados_unificado.py" ]; then
    echo "❌ Script unificado não encontrado"
    exit 1
fi

# Muda para o diretório raiz
cd "$(dirname "$0")/.."

# Executa o script passando todos os argumentos
if python3 _scripts/certificados_unificado.py "$@"; then
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
