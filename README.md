# claude-solve-and-explain

A Claude Code slash command that solves exercise sheets and generates two LaTeX PDFs: a clean **solution** and a beginner-friendly **explanation** with step-by-step walkthroughs, colored info boxes, and TikZ graphs.

## What it does

Given an exercise sheet (PDF or text), the skill:

1. Analyzes all tasks and works out the solutions
2. Launches two agents in parallel:
   - **Solution PDF** - clean, student-style write-up with proofs, calculations, and TikZ sketches
   - **Explanation PDF** - detailed step-by-step guide with analogies, highlighted formulas, and "why" at every step
3. Compiles both `.tex` files to PDF and cleans up build artifacts

## Output example

| Solution | Explanation |
|----------|-------------|
| Concise, well-structured | Every concept explained from scratch |
| Written like a student | Written like a tutor for beginners |
| `\fbox{}` summary boxes | Blue `merkbox` for key formulas |
| TikZ graphs where needed | Green `analogie` boxes for real-world comparisons |
| 3-9 pages typical | 13-25 pages typical |

## Installation

Copy the skill file to your Claude Code commands directory:

```bash
# Global (available in all projects)
cp solve-and-explain.md ~/.claude/commands/

# Project-only
mkdir -p .claude/commands
cp solve-and-explain.md .claude/commands/
```

## Usage

```
/solve-and-explain solve exercises 1-5 from the attached PDF
```

```
/solve-and-explain Aufgabe 10: Bestimme ob W ein Unterraum von V ist...
```

The skill works with any subject (math, logic, linear algebra, physics, etc.) and any language (defaults to German, adapts to the exercise sheet's language).

## Features

- **Parallel agents** for fast generation
- **TikZ/pgfplots** graphs and sketches where needed
- **tcolorbox** environments for visual highlighting:
  - `merkbox` (blue) - definitions, formulas, key rules
  - `analogie` (green) - everyday analogies and comparisons
- **Beginner-friendly explanations** - assumes no prior knowledge
- **Student-tone solutions** - "I need to show...", not textbook-speak
- **Automatic PDF compilation** with cleanup

## Requirements

- [Claude Code](https://claude.ai/claude-code) CLI
- LaTeX distribution with `pdflatex`, `tikz`, `pgfplots`, `tcolorbox` (e.g. TeX Live, MacTeX)

