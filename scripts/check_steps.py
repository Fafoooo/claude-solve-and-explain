#!/usr/bin/env python3
"""Findet übersprungene Schritte und verbotene Floskeln in einer solve-and-explain-Quelle.

Prüft nur den Lösungsteil (alles außerhalb von \\explain{...} / \\explainfig{...}):
  1. verbotene Floskeln ("offensichtlich", "analog", "clearly", …)
  2. align-Zeilen ohne \\why{…}-Begründung (erste Zeile einer Kette ausgenommen)
  3. Zeilen mit mehr als einem Relationszeichen (=, \\le, \\Rightarrow, …) → mehrere Umformungen
  4. tikzpicture im Lösungsteil ohne "% grafik-verlangt" in der Zeile davor
Exit-Code 1, wenn es Meldungen gibt.
"""
import re
import sys

FORBIDDEN = ["offensichtlich", "trivial", "analog", "leicht sieht man", "man sieht", "ergibt sich",
             "durch umformen", "nach kurzer rechnung", "obviously", "clearly", "similarly",
             "straightforward", "it is easy to see", "it follows easily"]
RELATIONS = re.compile(r"(?<![<>!\\])=(?!=)|\\le(?:q)?\b|\\ge(?:q)?\b|\\Rightarrow|\\Leftrightarrow|\\iff|\\implies|<|>")
ALIGN = re.compile(r"\\begin\{(align\*?|alignat\*?\{\d+\})\}(.*?)\\end\{\1\}", re.S)


def strip_explain(tex):
    """Remove \\explain{...} and \\explainfig{...} (balanced braces), keep line count stable."""
    out, i = [], 0
    while True:
        m = re.search(r"\\explain(?:fig)?\{", tex[i:])
        if not m:
            out.append(tex[i:])
            return "".join(out)
        start = i + m.start()
        out.append(tex[i:start])
        depth, j = 1, i + m.end()
        while j < len(tex) and depth:
            depth += {"{": 1, "}": -1}.get(tex[j], 0) if tex[j - 1] != "\\" else 0
            j += 1
        out.append("\n" * tex[start:j].count("\n"))
        i = j


def line_no(tex, pos):
    return tex.count("\n", 0, pos) + 1


def check(tex):
    issues = []
    body = strip_explain(re.sub(r"(?<!\\)%.*", lambda m: m.group(0) if "grafik-verlangt" in m.group(0) else "", tex))
    low = body.lower()
    for word in FORBIDDEN:
        for m in re.finditer(r"\b" + re.escape(word) + r"\b", low):
            issues.append((line_no(body, m.start()), f'verbotene Floskel "{word}"'))
    for m in ALIGN.finditer(body):
        rows = re.split(r"\\\\", m.group(2))
        offset = m.start(2)
        for k, row in enumerate(rows):
            text = row.strip()
            if not text:
                offset += len(row) + 2
                continue
            ln = line_no(body, offset + len(row) - len(row.lstrip()))
            math_part = re.split(r"&&", text)[0]
            math_part = re.sub(r"\\text\{[^}]*\}|\\why\{[^}]*\}", "", math_part)
            if "\\why{" not in text and k > 0:
                issues.append((ln, "Schritt ohne \\why{…}-Begründung"))
            rels = RELATIONS.findall(math_part.replace("&=", "="))
            if len(rels) > 1:
                issues.append((ln, f"{len(rels)} Relationszeichen in einer Zeile – mehrere Umformungen? Aufteilen"))
            offset += len(row) + 2
    for m in re.finditer(r"\\begin\{tikzpicture\}", body):
        prev = body[:m.start()].rstrip().splitlines()[-1:] or [""]
        if "grafik-verlangt" not in prev[0]:
            issues.append((line_no(body, m.start()), "Grafik im Lösungsteil ohne '% grafik-verlangt' – gehört in \\explainfig{}"))
    return sorted(issues)


def selftest():
    good = "\\begin{align*}\n0 &= a + 2\\cdot(-2) && \\why{x}\\\\\n0 &= a - 4 && \\why{y}\n\\end{align*}"
    bad = ("Das ist offensichtlich.\n\\begin{align*}\n0 &= a + 2(-2) = a - 4\\\\\n4 &= a\n\\end{align*}\n"
           "\\begin{tikzpicture}\\end{tikzpicture}\n\\explain{analog \\begin{tikzpicture}\\end{tikzpicture}}")
    assert check(good) == [], check(good)
    kinds = [msg.split()[0] for _, msg in check(bad)]
    assert kinds.count("verbotene") == 1 and "Grafik" in kinds and "Schritt" in kinds and "2" in kinds, check(bad)
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
        sys.exit(0)
    if len(sys.argv) != 2:
        sys.exit("usage: check_steps.py blattNN.tex | --selftest")
    found = check(open(sys.argv[1], encoding="utf-8").read())
    for ln, msg in found:
        print(f"{sys.argv[1]}:{ln}: {msg}")
    print("keine Meldungen" if not found else f"{len(found)} Meldung(en)")
    sys.exit(1 if found else 0)
