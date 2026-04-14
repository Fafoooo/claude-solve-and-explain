# Solve & Explain – Übungsblatt lösen und erklären

Erstelle zwei LaTeX-Dokumente für das gegebene Übungsblatt:
1. **Lösung** (`loesung_<name>.tex/.pdf`) – saubere Musterlösung, wie von einem guten Studenten geschrieben
2. **Erklärung** (`erklaerung_<name>.tex/.pdf`) – ausführliche Schritt-für-Schritt-Erklärung für jemanden der das Thema noch nicht versteht

---

## Arbeitsweise

### Schritt 1: Aufgabenblatt analysieren
- Lies das Übungsblatt (PDF oder Beschreibung im Prompt)
- Identifiziere alle Aufgaben und Teilaufgaben
- Arbeite ALLE Lösungen mathematisch korrekt durch bevor du schreibst

### Schritt 2: Zwei Agents parallel starten
Starte zwei Agents gleichzeitig – einen für die Lösung, einen für die Erklärung. Gib beiden die komplett durchgerechneten Lösungen im Prompt mit, damit sie nur noch LaTeX schreiben müssen. Der Lösungs-Agent folgt den Regeln unter "Stil der LÖSUNG", der Erklärungs-Agent folgt den Regeln unter "Stil der ERKLÄRUNG".

### Schritt 3: Kompilieren & aufräumen
Kompiliere beide .tex-Dateien zu PDFs, lösche .aux/.log/.toc/.out-Dateien.

### Schritt 4: Feynman-Check (optional)
Lies die fertige Erklärung nochmal durch und prüfe mit der Feynman-Technik:
- Kann man jedes Konzept in einem Satz mit Alltagsworten erklären?
- Gibt es Lücken (undefinierte Begriffe, übersprungene Schritte, fehlendes "Warum")?
- Falls ja: Lücken füllen und Erklärung verbessern.

---

## Stil der LÖSUNG

### Ton & Sprache
- **Sprache**: Deutsch (oder Sprache des Übungsblatts)
- **KEINE KI-Phrasen / keine Meta-Narration**. Die Lösung muss klingen wie von einem Studenten selbst hingeschrieben, nicht wie von einer KI erklärt. VERBOTEN:
  - "Zuerst erkläre ich, wie..." / "Bevor ich anfange, kläre ich..."
  - "Ich stelle eine Tabelle auf und werte schrittweise aus..."
  - "Ich beweise jetzt per Induktion, dass..."
  - "Die Idee ist einfach: ..." / "Bevor ich hinschreibe, halte ich fest..."
  - "Rezept", "Trick", "Man beachte..."
- **ERLAUBT** ist "Ich setze...", "Setze F' := ..." im konkreten mathematischen Kontext (Standardsprache im Beweis). Aber keine Vorankündigungen, kein "Jetzt mache ich X".
- Direkte, knappe Sätze. Rechnung hinknallen, Ergebnis kenntlich machen. Keine erfundenen Variablennamen (kein "F ≡ ..." wenn die Angabe kein F definiert).

### Struktur pro Aufgabe
1. **Angabe** kurz wiederholen (als eigener Block `\textbf{Angabe.}`) – das Aufgabenblatt sieht der Korrektor nicht immer daneben
2. **In nummerierte Schritte** aufteilen: `\textbf{Schritt 1: ...}`, `\textbf{Schritt 2: ...}` etc.
   - Schritt zeigt WAS gemacht wird (z.B. "Wahrheitstabelle aufstellen"), dann folgt die Durchführung
   - Jeder Schritt soll für sich lesbar sein – man soll auf einen Blick sehen, "was tu ich wann?"
3. **Ergebnis am Ende** klar abgesetzt (fett oder in `\fbox{\parbox{...}}`)

### Herleitungen zeigen – der rote Faden
Auch wenn die Lösung knapp sein soll: der Weg zum Ergebnis muss nachvollziehbar sein. Nicht nur das finale Ergebnis hinknallen.
- **Zeilenweise Herleitung** statt nur Schlussergebnis: Bei Tabellen-Transformationen (Wahrheitstabelle → Normalform, Matrix → Gleichungssystem, etc.) für die ersten 2-3 Zeilen/Schritte explizit vorrechnen, dann "analog für die restlichen" + Gesamtergebnis. Format als Aufzählung (`itemize`) oder schmale Tabelle.
- **Zwischenspalten** in Tabellen zeigen (z.B. bei Wahrheitstabellen: nicht nur Ergebnisspalte, sondern auch Hilfsspalten für Teilausdrücke). Auch wenn eine Spalte "technisch nicht nötig" ist – sie hilft beim Ablesen.
- **Operator-Präzedenz / Auswertungsreihenfolge** explizit benennen, wenn sie für den Lösungsweg relevant ist ("von innen nach außen", "Punkt vor Strich" etc.).
- **Beweise** zusätzlich mit **konkretem Beispiel** illustrieren, das die abstrakten Schritte an einer einfachen Instanz vorführt.

### Formatierung
- Übersichtliche Tabellen mit `booktabs` (\toprule, \midrule, \bottomrule)
- **Tabellen müssen in die Seitenbreite passen.** Keine breiten Spalten mit langen Herleitungstexten – lieber Aufzählung (`itemize`) mit Zeile + Herleitung untereinander.
- **Abkürzungen im Titel ausschreiben**: `CNF (konjunktive Normalform)`, `BNF (Backus-Naur-Form)`, `ODE (gewöhnliche Differentialgleichung)` etc. – so sieht der Student im fertigen PDF direkt, wofür die Abkürzung steht.
- **Markierungs-/Verwendungsspalten** in großen Tabellen erhalten (z.B. in einer Wahrheitstabelle: eine Spalte "→ CNF" / "→ DNF" pro Zeile, je nachdem welche Zeile für welche Form verwendet wird). Hilft beim Ablesen.
- Fach-Jargon, der im Lehrbuch zwar Standard, aber leicht verwechselbar ist (z.B. "Minterm"/"Maxterm"), nur verwenden wenn der User ihn ausdrücklich will. Im Zweifel durch klare Beschreibung ersetzen ("Konjunktion der wahren Zeile", "Disjunktion der falschen Zeile").
- Zusammenfassungen in `\fbox{\parbox{...}{...}}` Boxen
- Bei Beweisen: Alle Schritte zeigen, nichts überspringen, $\square$ am Ende
- Bei Gegenbeispielen: Konkret zeigen WARUM es scheitert
- **Skizzen/Graphen mit TikZ+pgfplots** wo verlangt oder hilfreich:
```latex
\begin{center}
\begin{tikzpicture}
\begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$,
             grid=both, width=10cm, height=7cm]
\addplot[blue, thick, domain=-5:5, samples=100]{...};
\end{axis}
\end{tikzpicture}
\end{center}
```

### LaTeX-Pakete (Lösung)
```latex
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[ngerman]{babel}  % oder andere Sprache
\usepackage{amsmath,amssymb}
\usepackage{geometry}\geometry{margin=2.5cm}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{tikz}
\usepackage{pgfplots}\pgfplotsset{compat=1.18}
```

### Qualitätskriterien Lösung
- Fachlich korrekt (alle Rechnungen/Beweise doppelt prüfen)
- Jeder Beweis vollständig (keine "offensichtlich" oder "trivialerweise")
- Ergebnis klar erkennbar und vom Rechenweg abgesetzt
- Kompiliert fehlerfrei mit pdflatex
- Kein erfundener Variablenname, der nicht in der Angabe steht
- Tabellen ragen nicht über den Seitenrand hinaus
- Keine Meta-Narration / KI-Phrasen (siehe Ton-Regeln)

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
7. **Schreibe wie für einen 15-Jährigen**

### Struktur der Erklärung
1. **Grundlagen-Teil** (vor den Aufgaben): Alle nötigen Konzepte/Definitionen/Formeln erklären, jeweils mit Analogie und Merkbox. "Typische Fallen" als Merkbox wenn es häufige Fehlerquellen gibt.
2. **Pro Aufgabe**: Was bedeutet die Aufgabe in einfachen Worten? → Welche Methode? → Schritt für Schritt durchrechnen mit Begründung → Ergebnis klar hervorheben
3. **Zusammenfassung** am Ende: Ergebnisübersicht (Tabelle) + "goldene Regeln" als Merkbox

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

### Verwendung der Boxen
- `\begin{merkbox}` – Definitionen, Formeln, wichtige Regeln, typische Fallen
- `\begin{merkbox}[title={Strategie}]` – Vorgehensweise für einen Aufgabentyp
- `\begin{analogie}` – Alltagsvergleiche (mindestens 1 pro Aufgabentyp)
- `\begin{analogie}[title={Beispiel: ...}]` – konkrete Beispiele aus dem Alltag

### Erklär-Regeln
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

### LaTeX-Pakete (Erklärung)
Gleiche Pakete wie Lösung, plus tcolorbox.

### Qualitätskriterien Erklärung
- Jemand ohne Vorwissen kann dem Text folgen
- Kein Schritt wird übersprungen
- Jedes "warum" ist beantwortet
- Mindestens 1 Analogie pro Themenblock
- Kompiliert fehlerfrei mit pdflatex

---

## Feynman-Check (Qualitätsprüfung)

Nach dem Erstellen der Erklärung optional die Feynman-Technik anwenden:

### Schritt 1: Einfach zurückerklären
Jedes Konzept in der Erklärung in einem Satz mit Alltagsworten wiedergeben. Wenn das nicht geht → Lücke gefunden.

### Schritt 2: Lücken finden
Prüfe ob die Erklärung irgendwo:
- Einen Begriff verwendet ohne ihn vorher zu definieren
- Einen Rechenschritt überspringt
- "offensichtlich" oder "klar" sagt (nichts ist offensichtlich für Anfänger)
- Sagt WAS man tut aber nicht WARUM
- Eine Analogie bräuchte aber keine hat
- Eine Mathe-Wand hat ohne Worterklärung zwischen den Schritten

### Schritt 3: Lücken füllen
Für jede gefundene Lücke:
- Fehlende Definition/Erklärung ergänzen
- Übersprungenen Schritt einfügen
- "offensichtlich" durch tatsächliche Begründung ersetzen
- Fehlendes "warum" ergänzen
- Analogie erstellen
- Verbale Brücke zwischen Mathe-Schritten einfügen

### Schritt 4: Verbesserte Version ausgeben
Die Erklärungsdatei direkt verbessern oder die Fixes als Text ausgeben.

### Qualitäts-Checkliste
- [ ] Könnte ein 15-Jähriger dem Text folgen? (kein unerklärter Fachjargon)
- [ ] Ist jedes "warum" beantwortet? (keine unmotivierten Schritte)
- [ ] Gibt es mindestens eine Analogie pro Themenblock?
- [ ] Sind Rechnungen Schritt für Schritt ohne Lücken?
- [ ] Sind wichtige Formeln/Regeln in merkbox?
- [ ] Gibt es eine Zusammenfassung am Ende?

---

## Ausgabe

Erstelle die Dateien im aktuellen Verzeichnis (oder im Verzeichnis des Übungsblatts). Benenne sie:
- `loesung_<name>.tex` + `.pdf`
- `erklaerung_<name>.tex` + `.pdf`

wobei `<name>` aus dem Kontext abgeleitet wird (z.B. `blatt03`, `ueb2`, `hw04`).

$ARGUMENTS
