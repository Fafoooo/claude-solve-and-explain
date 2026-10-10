# claude-solve-and-explain

Skill zum Lösen von Mathe- und Theorie-Übungsblättern für **Claude Code** und **Hermes Agent**.
Aus **einer** LaTeX-Quelle entstehen zwei PDFs:

| `loesung_blattNN.pdf` – wird abgegeben | `erklaerung_blattNN.pdf` – zum Verstehen |
|---|---|
| Angabe + Lösung, **jeder Rechenschritt einzeln** mit Begründung rechts | exakt dasselbe Dokument |
| schlicht, keine Erklärtexte | plus Erklärkasten direkt hinter jedem Schritt |
| Grafik nur, wenn die Aufgabe eine verlangt | plus erklärende Grafiken |

Beide PDFs haben dieselben Nummern, Zeilen und dieselbe Optik, weil sie aus derselben Datei gebaut werden.

## Was neu ist (v2)

- **Schrittregel:** eine Umformung pro Zeile, Einsetzen als eigener Schritt, keine „offensichtlich“/„analog“.
- **Automatische Schritt-Prüfung** (`scripts/check_steps.py`): meldet Zeilen ohne Begründung,
  mehrere Umformungen in einer Zeile, verbotene Floskeln und unverlangte Grafiken in der Lösung.
- **Nachrechnen mit Python** (SymPy/SciPy) und eine **unabhängige zweite Prüfung** vor dem Bauen.
- Lösung in der Sprache der Angabe, Erklärungen immer auf Deutsch.

## Dateien

```
SKILL.md                 Anleitung für den Agenten
templates/blatt.tex      Vorlage (Schalter \explainmode, Makros \angabe, \why, \explain, \explainfig)
scripts/build.sh         blattNN.tex → loesung_blattNN.pdf + erklaerung_blattNN.pdf
scripts/check_steps.py   Schritt-Prüfung (python3 check_steps.py --selftest)
```

## Installation

```bash
# Claude Code (global)
git clone https://github.com/Fafoooo/claude-solve-and-explain ~/.claude/skills/solve-and-explain

# Hermes Agent
git clone https://github.com/Fafoooo/claude-solve-and-explain ~/.hermes/skills/education/solve-and-explain
```

Voraussetzungen: `pdflatex` (TeX Live mit `latex-extra`, `pictures`, `science`, `lang-german`),
`pdftoppm`/`pdftotext` (poppler), Python 3 mit `sympy`/`scipy` zum Nachrechnen.

## Verwendung

```
/solve-and-explain löse das angehängte Blatt
```

Der Moodle-Solver von Hermes nutzt den Skill automatisch für neue Blätter in Mathe-Kursen
und legt die Ergebnisse unter `uebNN/` im Kurs-Repo ab.
