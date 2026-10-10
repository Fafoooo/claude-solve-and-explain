---
name: solve-and-explain
description: Löst ein Mathe-/Theorie-Übungsblatt und erzeugt aus EINER LaTeX-Quelle zwei PDFs – loesung_blattNN.pdf (schlicht, zum Abgeben, jeder Rechenschritt einzeln) und erklaerung_blattNN.pdf (identisch, plus Erklärungen und Grafiken zu jedem Schritt). Use when an exercise sheet (Übungsblatt, Exercise sheet, Hausübung) should be solved, manually or by the Moodle auto-solver.
version: 2.0.0
metadata:
  hermes:
    tags: [math, latex, university, exercises]
    requires_toolsets: [terminal]
---

# Solve & Explain

Aus **einer** Datei `blattNN.tex` entstehen zwei PDFs:

| `loesung_blattNN.pdf` (wird abgegeben) | `erklaerung_blattNN.pdf` (zum Verstehen) |
|---|---|
| Angabe + Lösung, jeder Schritt einzeln | **exakt dasselbe** Dokument … |
| schlicht, keine Erklärtexte | … plus Erklärkästen zu jedem Schritt |
| Grafiken **nur**, wenn die Aufgabe eine verlangt | … plus erklärende Grafiken |

Weil beide aus derselben Quelle kommen, haben sie dieselben Nummern, dieselben Zeilen und dieselbe Optik.
Erklärungen stehen **nur** in `\explain{…}` und `\explainfig{…}` und verschwinden in der Lösung.

Dateien des Skills: `templates/blatt.tex` (Vorlage), `scripts/build.sh` (baut beide PDFs),
`scripts/check_steps.py` (findet übersprungene Schritte und verbotene Floskeln).
`SKILL_DIR` ist das Verzeichnis dieser Datei (bei Hermes `${HERMES_SKILL_DIR}`).

## Die Schrittregel (das Wichtigste)

Die Lösung muss sich **ohne Nachschlagen** nachvollziehen lassen. Deshalb gilt:

1. **Eine Umformung pro Zeile.** Rechts steht immer, was gemacht wurde: `\why{$|\,+4$}`,
   `\why{$|\,\cdot(-1)$}`, `\why{$Z_2 - 3Z_1$}`, `\why{Distributivgesetz}`, `\why{einsetzen: $\beta=-2$}`.
2. **Einsetzen ist ein eigener Schritt.** Erst die Zahl einsetzen, in der nächsten Zeile ausrechnen.
3. **Rechnungen sichtbar:** `2\cdot(-2) = -4` steht da, nicht nur das Ergebnis. Keine Kopfrechnung über mehr als einen Rechenschritt.
4. **Gauß / Matrizen:** jede Zeilenoperation eine eigene Matrix mit Operation daneben.
5. **Gleichungssysteme:** jede Variable einzeln isolieren, jeden Schritt als eigene Zeile.
6. **Beweise:** jede Folgerung mit Begründung (Definition, Satz, Voraussetzung), am Ende $\square$.
7. **Verboten:** „offensichtlich“, „trivial“, „analog“, „leicht sieht man“, „man sieht“, „ergibt sich“,
   „durch Umformen“, „nach kurzer Rechnung“, „obviously“, „clearly“, „similarly“, „straightforward“.
   Statt „analog“ wird der zweite Fall vollständig ausgeschrieben.
8. **Probe** bei jedem Rechenergebnis (Einsetzen und Nachrechnen, ebenfalls Schritt für Schritt).
9. **Ergebnis** am Ende jeder Teilaufgabe in `\boxed{…}`.

Beispiel, falsch: `0 = \alpha + 2(-2) = \alpha - 4 \Rightarrow \alpha = 4`. Richtig:

```latex
\begin{align*}
0 &= \alpha + 2\cdot(-2) && \why{einsetzen: $\beta = -2$}\\
0 &= \alpha - 4          && \why{$2\cdot(-2) = -4$}\\
4 &= \alpha              && \why{$|\,+4$}
\end{align*}
```

## Aufbau pro Aufgabe

```latex
\aufgabe{1.1}                       % Beispielnummer genau wie auf dem Blatt
\angabe{Original-Angabe, wörtlich oder knapp, inkl. aller Zahlen und Teilaufgaben.}
\explain{Worum geht es? Welche Methode und warum? (nur im Erklär-PDF)}
\teil{a}
… Schritte nach der Schrittregel …
\explain{Was passiert im Schritt davor, in Alltagsworten. Typische Falle.}
\explainfig{ \begin{tikzpicture} … \end{tikzpicture} }   % erklärende Grafik
\[ \boxed{x = 4} \]
```

- `\angabe{}` steht in **beiden** PDFs. Die Lösung ist damit ohne das Originalblatt lesbar.
- Verlangt die Aufgabe selbst eine Grafik („skizzieren Sie“, „zeichnen Sie“, grafische Lösung
  eines LP): als normale `tikzpicture` **außerhalb** von `\explainfig`, mit dem Kommentar
  `% grafik-verlangt` in der Zeile davor. Dann steht sie in beiden PDFs.
- Erklärkästen gehören **direkt hinter** den Schritt, den sie erklären. Kein separates Kapitel.
  Ein kurzer Grundlagen-Block vor der ersten Aufgabe ist erlaubt, aber nur als `\explain{}`.
- Erklärkästen in einfacher Sprache: was man macht, **warum**, wie man auf die Idee kommt, typische
  Fehler. Fachbegriffe beim ersten Auftreten definieren.

## Sprache

- Lösung (Schritte, Angabe, `\why`): **Sprache der Angabe** (englisches Blatt → englische Lösung,
  `\usepackage[english]{babel}`).
- Erklärkästen und erklärende Grafiken: **immer Deutsch**.
- Ton der Lösung: sachlich und knapp, wie eine saubere Studentenabgabe. Keine KI-Floskeln.

## Ablauf

1. **Angabe erfassen.** PDF-Seiten als Bilder lesen (`pdftoppm -r 150 -png angabe.pdf seite`),
   zusätzlich `pdftotext -layout`. Formeln immer aus dem Bild übernehmen, nicht aus dem Text-Export.
   Alle Aufgaben und Teilaufgaben auflisten. Keine überspringen.
2. **Durchrechnen** (Notizen, noch kein LaTeX): jede Teilaufgabe vollständig lösen.
3. **Nachrechnen mit Python**, wo es geht: `checks.py` im Ausgabeordner mit SymPy, NumPy oder SciPy
   (Hermes-CT: `~/.hermes/skill-venvs/math/bin/python checks.py`, sonst ein `python3` mit diesen Paketen).
   Das gilt für Gleichungssysteme, Inverse, Determinanten, Eigenwerte und LPs (`scipy.optimize.linprog`).
   Jede Zahl im Endergebnis muss dort bestätigt sein. Bei Abweichung: Rechnung korrigieren, nicht das Skript.
4. **LaTeX schreiben** auf Basis von `templates/blatt.tex` → `blattNN.tex`, nach Schrittregel und Aufbau.
5. **Schritt-Prüfung:** `python3 SKILL_DIR/scripts/check_steps.py blattNN.tex`. Jede Meldung beheben,
   bis keine mehr kommt, oder begründen, warum die Zeile so bleiben muss.
6. **Unabhängige Prüfung:** eine zweite Instanz (Subagent / `delegate_task`) bekommt **nur** die Angabe
   und die fertige `blattNN.tex` und prüft Zeile für Zeile: Rechenfehler? Übersprungener Schritt?
   Fehlende Begründung? Passt das Ergebnis zur Frage? Befunde einarbeiten, höchstens 2 Runden.
7. **Bauen:** `SKILL_DIR/scripts/build.sh blattNN.tex` → `loesung_blattNN.pdf` + `erklaerung_blattNN.pdf`.
   Muss fehlerfrei durchlaufen. Danach beide PDFs kurz öffnen bzw. Seitenzahl prüfen.
8. **Unsicheres markieren:** Ist eine Teilaufgabe nach Schritt 3 und 6 nicht verifiziert, kommt in
   die Lösung **nichts** dazu. Dem Nutzer melden: „⚠️ Aufgabe 2b nicht verifiziert: …“.

## Ablage

```
uebNN/                      (NN zweistellig: ueb01, ueb02, …)
  angabe_blattNN.pdf        Originalangabe
  blattNN.tex               die eine Quelle
  loesung_blattNN.pdf       zum Abgeben
  erklaerung_blattNN.pdf    zum Verstehen
  checks.py                 numerische Nachprüfung
```

Im automatischen Modus (Moodle-Solver): im Kurs-Repo committen
(`git add uebNN && git commit -m "ueb NN: Lösung + Erklärung"`), pushen und eine Zeile melden:
`✅ <Blatttitel> gelöst – <Link zum Ordner>`, plus Warnungen aus Schritt 8.

## Qualitäts-Checkliste (vor dem Abschluss)

- [ ] Alle Aufgaben und Teilaufgaben des Blatts gelöst, Nummern wie auf dem Blatt
- [ ] `check_steps.py` ohne Meldungen
- [ ] Jedes Endergebnis durch `checks.py` oder durch die unabhängige Prüfung bestätigt
- [ ] Lösung enthält keine Erklärtexte und keine Grafiken außer verlangten
- [ ] Erklärung erklärt jeden nicht-trivialen Schritt direkt dahinter
- [ ] Beide PDFs bauen fehlerfrei
