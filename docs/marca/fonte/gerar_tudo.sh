#!/usr/bin/env bash
# Regenera todas as artes estáticas e animadas da marca a partir do código.
# Requisitos: python3 com fonttools[woff] uharfbuzz pillow shapely; node com @resvg/resvg-js (npm i @resvg/resvg-js); ffmpeg.
set -e
cd "$(dirname "$0")"
PY=${PYTHON:-python3}
$PY preparar_fontes.py
for s in gerar_logos gerar_social gerar_icones gerar_emojis gerar_ilustracoes gerar_teco anim gerar_loader_css gerar_emojis_anim gerar_png gerar_visao_geral; do $PY $s.py; done
echo "pronto. Motion: veja ../motion/LEIA-ME.md"
