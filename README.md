# claude-solve-and-explain

A set of Claude Code slash commands for solving exercise sheets and generating LaTeX PDFs. Includes three skills that work together or independently.

## Skills

### `/solve-and-explain` (main skill)
The orchestrator. Given an exercise sheet, it analyzes all tasks, works out solutions, then launches two agents in parallel to generate both PDFs at once.

### `/latex-solution-writer`
Writes clean, student-style LaTeX solutions. Concise proofs, calculations, summary boxes, TikZ graphs. Written in first person ("I need to show...") rather than textbook-speak.

### `/explain-simply`
Writes beginner-friendly LaTeX explanations with `merkbox` (blue) and `analogie` (green) tcolorbox environments. Every concept explained from scratch, every step justified with "why", real-world analogies throughout.

## Output

| Solution (latex-solution-writer) | Explanation (explain-simply) |
|----------------------------------|------------------------------|
| Concise, well-structured | Every concept explained from scratch |
| Written like a student | Written like a tutor for beginners |
| `\fbox{}` summary boxes | Blue `merkbox` for key formulas |
| TikZ graphs where needed | Green `analogie` boxes for real-world comparisons |
| 3-9 pages typical | 13-25 pages typical |

## Installation

```bash
# All three skills (global)
cp solve-and-explain.md ~/.claude/commands/
cp latex-solution-writer.md ~/.claude/commands/
cp explain-simply.md ~/.claude/commands/

# Or project-only
mkdir -p .claude/commands
cp *.md .claude/commands/
```

## Usage

```bash
# Full pipeline: solution + explanation in parallel
/solve-and-explain solve exercises 1-5 from the PDF

# Just a clean solution
/latex-solution-writer write solutions for exercises 10a, 10d, 10e

# Just a beginner-friendly explanation
/explain-simply explain subspace test with examples for exercise 10
```

Works with any subject (math, logic, linear algebra, physics, etc.) and adapts to the exercise sheet's language.

## Features

- **Parallel agents** for fast generation (solve-and-explain)
- **TikZ/pgfplots** graphs and sketches
- **tcolorbox** environments:
  - `merkbox` (blue) - definitions, formulas, key rules, common mistakes
  - `analogie` (green) - everyday analogies and comparisons
- **Step-by-step calculations** with `align*` and inline justifications
- **Automatic PDF compilation** with cleanup

## Requirements

- [Claude Code](https://claude.ai/claude-code) CLI
- LaTeX distribution with `pdflatex`, `tikz`, `pgfplots`, `tcolorbox` (e.g. TeX Live, MacTeX)
