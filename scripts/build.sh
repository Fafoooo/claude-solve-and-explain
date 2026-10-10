#!/usr/bin/env bash
# Baut aus blattNN.tex beide PDFs: loesung_blattNN.pdf (\explainmode=0) und erklaerung_blattNN.pdf (=1).
set -euo pipefail
[ $# -eq 1 ] || { echo "usage: build.sh blattNN.tex" >&2; exit 2; }
tex=$(realpath "$1"); dir=$(dirname "$tex"); base=$(basename "$tex" .tex)
cd "$dir"
for mode in 0 1; do
  job=$([ "$mode" = 0 ] && echo "loesung_$base" || echo "erklaerung_$base")
  for pass in 1 2; do  # zweiter Lauf für Referenzen/Seitenumbrüche
    if ! pdflatex -interaction=nonstopmode -halt-on-error -jobname="$job" \
         "\\def\\explainmode{$mode}\\input{$base.tex}" > "$job.buildlog" 2>&1; then
      echo "FEHLER beim Bauen von $job.pdf:" >&2
      grep -E -A3 '^!' "$job.buildlog" >&2 || tail -n 30 "$job.buildlog" >&2
      exit 1
    fi
  done
  rm -f "$job".{aux,log,out,toc,buildlog}
  echo "ok: $dir/$job.pdf"
done
