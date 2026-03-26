# Solve & Explain – Übungsblatt lösen und erklären

Erstelle zwei LaTeX-Dokumente für das gegebene Übungsblatt:
1. **Lösung** (`loesung_<name>.tex/.pdf`) – saubere Musterlösung, wie von einem guten Studenten geschrieben
2. **Erklärung** (`erklaerung_<name>.tex/.pdf`) – ausführliche Schritt-für-Schritt-Erklärung für jemanden der das Thema noch nicht versteht

## Arbeitsweise

### Schritt 1: Aufgabenblatt analysieren
- Lies das Übungsblatt (PDF oder Beschreibung im Prompt)
- Identifiziere alle Aufgaben und Teilaufgaben
- Arbeite ALLE Lösungen mathematisch korrekt durch bevor du schreibst

### Schritt 2: Zwei Agents parallel starten
Starte zwei Agents gleichzeitig – einen für die Lösung, einen für die Erklärung. Gib beiden die komplett durchgerechneten Lösungen im Prompt mit, damit sie nur noch LaTeX schreiben müssen.

### Schritt 3: Kompilieren & aufräumen
Kompiliere beide .tex-Dateien zu PDFs, lösche .aux/.log-Dateien.

---

## Stil der LÖSUNG

- Sprache: Deutsch (oder Sprache des Übungsblatts)
- Ton: Wie von einem Studenten geschrieben (nicht wie ein Lehrbuch)
  - "Ich verwende...", "Ich muss zeigen...", "Setze ich ein..."
  - NICHT: "Rezept", "Trick", "Der Tester bekommt..."
- Struktur pro Aufgabe:
  - Aufgabenstellung kurz wiederholen
  - Rechnung/Beweis sauber durchführen
  - Klares Ergebnis am Ende
- Übersichtliche Tabellen und Boxen (\fbox) für Zusammenfassungen
- **Skizzen/Graphen mit TikZ+pgfplots** wo verlangt oder hilfreich
- Bei Beweisen: Alle Schritte zeigen, nichts überspringen
- Bei Gegenbeispielen: Konkret zeigen WARUM es scheitert

### LaTeX-Pakete (Lösung)
```latex
\usepackage[utf8]{inputenc}
\usepackage[ngerman]{babel}  % oder andere Sprache
\usepackage{amsmath,amssymb}
\usepackage{geometry}\geometry{margin=2.5cm}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{tikz}
\usepackage{pgfplots}\pgfplotsset{compat=1.18}
```

---

## Stil der ERKLÄRUNG

Die Erklärung ist das Herzstück – sie muss so geschrieben sein, dass jemand OHNE Vorwissen das Thema versteht.

### Grundprinzipien
1. **Jedes Konzept von Grund auf erklären** – was ist X? Warum macht man das?
2. **Bei JEDEM Schritt erklären WARUM** – nicht nur WAS man tut
3. **Alltagsanalogien** verwenden (grüne `analogie`-Boxen)
4. **Wichtige Regeln/Formeln** in blaue `merkbox`-Boxen
5. **Schritt-für-Schritt-Rechnungen** – nichts überspringen, jeden Zwischenschritt zeigen
6. **Konkrete Beispiele** vor abstrakten Regeln

### Struktur der Erklärung
1. **Grundlagen-Teil** (vor den Aufgaben): Alle nötigen Konzepte/Definitionen/Formeln erklären
2. **Pro Aufgabe**: Was bedeutet die Aufgabe? → Welche Methode? → Schritt für Schritt → Ergebnis
3. **Zusammenfassung** am Ende: Ergebnisübersicht + "goldene Regeln"

### tcolorbox-Umgebungen
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

### Erklär-Regeln
- Schreibe wie für einen 15-Jährigen
- Verwende `\begin{merkbox}` für Definitionen, Formeln, wichtige Regeln
- Verwende `\begin{analogie}` für Alltagsvergleiche (mindestens 1 pro Aufgabentyp)
- Bei Rechnungen: `align*`-Umgebung mit Begründung rechts (`&& \text{(weil ...)}`)
- Bei Textaufgaben: Erst den Text in Variablen/Formeln übersetzen, dann rechnen
- "Typische Fallen" als merkbox wenn es häufige Fehlerquellen gibt
- **Skizzen mit TikZ+pgfplots** überall wo es hilft

### LaTeX-Pakete (Erklärung)
Gleiche Pakete wie Lösung, plus tcolorbox.

---

## Ausgabe

Erstelle die Dateien im aktuellen Verzeichnis (oder im Verzeichnis des Übungsblatts). Benenne sie:
- `loesung_<name>.tex` + `.pdf`
- `erklaerung_<name>.tex` + `.pdf`

wobei `<name>` aus dem Kontext abgeleitet wird (z.B. `blatt03`, `ueb2`, `hw04`).

Nach dem Kompilieren: `.aux`, `.log`, `.toc`, `.out` Dateien löschen.

$ARGUMENTS
