# claude-solve-and-explain

Ein Claude Code Slash-Command zum Lösen von Übungsblättern. Erstellt zwei LaTeX-PDFs: eine saubere **Lösung** und eine anfängerfreundliche **Erklärung** mit Schritt-für-Schritt-Herleitungen, farbigen Infoboxen und TikZ-Graphen.

## Was es tut

1. Analysiert das Übungsblatt und rechnet alle Lösungen durch
2. Startet zwei Agents parallel:
   - **Lösung** – kompakt, im Studenten-Stil, mit TikZ-Skizzen
   - **Erklärung** – jedes Konzept von Grund auf, mit `merkbox` (blau) und `analogie` (grün)
3. Kompiliert beide PDFs und räumt auf
4. Optional: Feynman-Check der Erklärung (Lücken finden und füllen)

## Ausgabe

| Lösung | Erklärung |
|--------|-----------|
| Kompakt, gut strukturiert | Jedes Konzept von Grund auf erklärt |
| Geschrieben wie ein Student | Geschrieben wie ein Nachhilfelehrer |
| `\fbox{}` Zusammenfassungs-Boxen | Blaue `merkbox` für Formeln/Regeln |
| TikZ-Graphen wo nötig | Grüne `analogie`-Boxen für Alltagsvergleiche |
| Typisch 3-9 Seiten | Typisch 13-25 Seiten |

## Installation

```bash
# Global (in allen Projekten verfügbar)
cp solve-and-explain.md ~/.claude/commands/

# Oder nur für ein Projekt
mkdir -p .claude/commands
cp solve-and-explain.md .claude/commands/
```

## Verwendung

```bash
# Komplette Pipeline: Lösung + Erklärung parallel
/solve-and-explain löse Aufgaben 1-5 vom angehängten PDF

# Bestimmte Aufgaben
/solve-and-explain löse nur Aufgabe 10a, 10d, 10e und 10g

# Mit Feynman-Check
/solve-and-explain löse das Blatt und prüfe die Erklärung mit Feynman-Check
```

Funktioniert mit jedem Fach (Mathe, Logik, Lineare Algebra, Physik, etc.) und passt sich der Sprache des Übungsblatts an.

## Was steckt drin

Der Skill enthält alles in einer Datei:

- **Lösungs-Stil**: Studenten-Ton, TikZ-Graphen, `\fbox`-Boxen, `booktabs`-Tabellen
- **Erklärungs-Stil**: Grundlagen-Teil → Aufgaben → Zusammenfassung, `merkbox`/`analogie`, `align*` mit Begründungen
- **Feynman-Check**: Erklärung auf Verständlichkeit prüfen, Lücken finden und füllen
- **LaTeX-Templates**: Alle Pakete und tcolorbox-Definitionen

## Voraussetzungen

- [Claude Code](https://claude.ai/claude-code) CLI
- LaTeX-Distribution mit `pdflatex`, `tikz`, `pgfplots`, `tcolorbox` (z.B. TeX Live, MacTeX)
