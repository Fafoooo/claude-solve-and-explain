# claude-solve-and-explain

Eine Sammlung von Claude Code Slash-Commands zum Lösen von Übungsblättern und Erstellen von LaTeX-PDFs. Enthält 5 Skills, die zusammen oder einzeln verwendet werden können.

## Skills

### `/solve-and-explain` (Haupt-Skill)
Der Orchestrator. Bekommt ein Übungsblatt, analysiert alle Aufgaben, rechnet die Lösungen durch und startet dann zwei Agents parallel – einen für die Lösung, einen für die Erklärung.

### `/latex-solution-writer`
Schreibt saubere LaTeX-Musterlösungen im Studenten-Stil. Beweise, Rechnungen, Zusammenfassungs-Boxen, TikZ-Graphen. In der ersten Person geschrieben ("Ich muss zeigen...") statt Lehrbuch-Sprache.

### `/explain-simply`
Schreibt anfängerfreundliche LaTeX-Erklärungen mit `merkbox` (blau) und `analogie` (grün) tcolorbox-Umgebungen. Jedes Konzept von Grund auf erklärt, jeder Schritt mit "warum" begründet, Alltagsanalogien durchgehend.

### `/feynman`
Die Feynman-Lerntechnik: Ein Konzept einfach erklären, Lücken im Verständnis finden, diese füllen und die Erklärung verfeinern. Verwenden wenn man etwas Neues lernt oder sein Verständnis testen will.

### `/feynman-check`
Qualitätsprüfung mit der Feynman-Technik für bestehende Erklärungen. Findet Lücken: undefinierte Begriffe, übersprungene Schritte, fehlende "Warum"s, Mathe-Wände ohne Worterklärungen. Füllt diese Lücken dann. Nach dem Erstellen einer Erklärung verwenden, um zu prüfen ob sie wirklich verständlich ist.

## Ausgabe

| Lösung (latex-solution-writer) | Erklärung (explain-simply) |
|--------------------------------|----------------------------|
| Kompakt, gut strukturiert | Jedes Konzept von Grund auf erklärt |
| Geschrieben wie ein Student | Geschrieben wie ein Nachhilfelehrer |
| `\fbox{}` Zusammenfassungs-Boxen | Blaue `merkbox` für Formeln/Regeln |
| TikZ-Graphen wo nötig | Grüne `analogie`-Boxen für Alltagsvergleiche |
| Typisch 3-9 Seiten | Typisch 13-25 Seiten |

## Installation

```bash
# Alle Skills global installieren
cp solve-and-explain.md ~/.claude/commands/
cp latex-solution-writer.md ~/.claude/commands/
cp explain-simply.md ~/.claude/commands/
cp feynman.md ~/.claude/commands/
cp feynman-check.md ~/.claude/commands/

# Oder nur für ein Projekt
mkdir -p .claude/commands
cp *.md .claude/commands/
```

## Verwendung

```bash
# Komplette Pipeline: Lösung + Erklärung parallel
/solve-and-explain löse Aufgaben 1-5 vom angehängten PDF

# Nur eine saubere Lösung
/latex-solution-writer schreibe Lösungen für Aufgaben 10a, 10d, 10e

# Nur eine anfängerfreundliche Erklärung
/explain-simply erkläre den Unterraum-Test mit Beispielen für Aufgabe 10

# Konzept mit Feynman-Technik verstehen
/feynman erkläre mir was ein Untervektorraum ist

# Bestehende Erklärung auf Verständlichkeit prüfen
/feynman-check prüfe erklaerung_blatt03.tex - versteht ein Anfänger das?
```

Funktioniert mit jedem Fach (Mathe, Logik, Lineare Algebra, Physik, etc.) und passt sich der Sprache des Übungsblatts an.

## Features

- **Parallele Agents** für schnelle Generierung (solve-and-explain)
- **TikZ/pgfplots** Graphen und Skizzen
- **tcolorbox** Umgebungen:
  - `merkbox` (blau) - Definitionen, Formeln, wichtige Regeln, typische Fehler
  - `analogie` (grün) - Alltagsanalogien und Vergleiche
- **Schritt-für-Schritt-Rechnungen** mit `align*` und Begründungen
- **Automatische PDF-Kompilierung** mit Aufräumen

## Voraussetzungen

- [Claude Code](https://claude.ai/claude-code) CLI
- LaTeX-Distribution mit `pdflatex`, `tikz`, `pgfplots`, `tcolorbox` (z.B. TeX Live, MacTeX)
