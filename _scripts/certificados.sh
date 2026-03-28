#!/bin/bash
#
# Script simplificado para executar o processamento de certificados
# Versão compacta para execução rápida
#
# Uso:
#   ./_scripts/certificados.sh
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

# Executa o script
if python3 _scripts/certificados_unificado.py; then
    echo ""
    echo "✅ Certificados processados com sucesso!"
    echo "📁 Verifique: certificados/index.md"
else
    echo ""
    echo "❌ Erro no processamento"
    exit 1
fi
