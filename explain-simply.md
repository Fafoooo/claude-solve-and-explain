# Explain Simply – Beginner-Friendly LaTeX Explanations

Schreibe eine ausführliche, einfache Erklärung als LaTeX-Dokument. Die Erklärung muss so geschrieben sein, dass jemand OHNE Vorwissen das Thema versteht.

## Grundprinzipien

1. **Jedes Konzept von Grund auf erklären** – was ist X? Warum macht man das?
2. **Bei JEDEM Schritt erklären WARUM** – nicht nur WAS man tut
3. **Alltagsanalogien** verwenden (grüne `analogie`-Boxen)
4. **Wichtige Regeln/Formeln** in blaue `merkbox`-Boxen
5. **Schritt-für-Schritt-Rechnungen** – nichts überspringen, jeden Zwischenschritt zeigen
6. **Konkrete Beispiele** vor abstrakten Regeln
7. **Schreibe wie für einen 15-Jährigen**

## Struktur

1. **Grundlagen-Teil** (vor den Aufgaben):
   - Alle nötigen Konzepte/Definitionen/Formeln erklären
   - Jeweils mit Analogie und Merkbox
   - "Typische Fallen" als Merkbox wenn es häufige Fehlerquellen gibt

2. **Pro Aufgabe**:
   - Was bedeutet die Aufgabe in einfachen Worten?
   - Welche Methode/Strategie verwende ich?
   - Schritt für Schritt durchrechnen mit Begründung bei jedem Schritt
   - Ergebnis klar hervorheben

3. **Zusammenfassung** am Ende:
   - Ergebnisübersicht (Tabelle)
   - "Goldene Regeln" als Merkbox

## tcolorbox-Umgebungen

```latex
\usepackage{tcolorbox}
\tcbuselibrary{breakable}

\newtcolorbox{merkbox}[1][]{
  colback=blue!5, colframe=blue!40,
  fonttitle=\bfseries, title={Merke},
  breakable, #1
}

\newtcolorbox{analogie}[1][]{
  colback=green!5, colframe=green!40,
  fonttitle=\bfseries, title={Analogie},
  breakable, #1
}
```

## Verwendung der Boxen

- `\begin{merkbox}` – Definitionen, Formeln, wichtige Regeln, typische Fallen
- `\begin{merkbox}[title={Strategie}]` – Vorgehensweise/Rezept für einen Aufgabentyp
- `\begin{analogie}` – Alltagsvergleiche (mindestens 1 pro Aufgabentyp)
- `\begin{analogie}[title={Beispiel: ...}]` – konkrete Beispiele aus dem Alltag

## Erklär-Regeln

- Bei Rechnungen: `align*`-Umgebung mit Begründung rechts:
```latex
\begin{align*}
(f+g)(-x) &= f(-x) + g(-x)
    && \text{(Definition der Addition)} \\
  &= -f(x) + (-g(x))
    && \text{(weil $f,g$ ungerade)} \\
  &= -(f+g)(x). \;\checkmark
\end{align*}
```
- Bei Textaufgaben: Erst den Text in Variablen/Formeln übersetzen, dann rechnen
- Bei Vorzeichentabellen, Wahrheitstabellen etc.: Zeile für Zeile erklären wie man sie ausfüllt
- **Skizzen mit TikZ+pgfplots** überall wo es hilft
- Mindestens 1 Beispielrechnung komplett vorrechnen bevor die eigentliche Aufgabe kommt

## LaTeX-Pakete

```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[ngerman]{babel}
\usepackage{amsmath,amssymb}
\usepackage{geometry}\geometry{margin=2.5cm}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{tikz}
\usepackage{pgfplots}\pgfplotsset{compat=1.18}
\usepackage{tcolorbox}
\tcbuselibrary{breakable}
```

## Qualitätskriterien

- Jemand ohne Vorwissen kann dem Text folgen
- Kein Schritt wird übersprungen
- Jedes "warum" ist beantwortet
- Mindestens 1 Analogie pro Themenblock
- Kompiliert fehlerfrei mit pdflatex

$ARGUMENTS
