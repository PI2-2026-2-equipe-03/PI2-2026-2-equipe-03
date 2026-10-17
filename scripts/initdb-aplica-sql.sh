#!/bin/sh
# aplica o sql do backend na criação do volume do postgres.
# ordem: tudo de init/, depois tudo de migrations/.
# o postgres só executa /docker-entrypoint-initdb.d quando o volume é novo,
# então isto não roda de novo em banco já existente (use `down -v`).
set -e

aplicar() {
  [ -d "$1" ] || return 0
  for arquivo in "$1"/*.sql; do
    # -s pula arquivo vazio e o caso de glob sem match
    [ -s "$arquivo" ] || continue
    echo "[initdb] aplicando $arquivo"
    psql -v ON_ERROR_STOP=1 \
      --username "$POSTGRES_USER" \
      --dbname "$POSTGRES_DB" \
      -f "$arquivo"
  done
}

aplicar /sql/init
aplicar /sql/migrations
