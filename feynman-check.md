# Feynman Check – Verify Explanations Are Actually Understandable

Apply the Feynman technique to check and improve an existing explanation document. The idea: if you can't explain it simply, you don't understand it well enough.

## What this does

Takes an existing explanation (LaTeX/PDF/text) and runs it through 4 steps:

### Step 1: Read & Explain Back Simply
Read the explanation and try to re-explain every concept in one sentence using everyday words. If any concept needs jargon or feels hand-wavy, flag it.

### Step 2: Find Gaps
Identify where the explanation:
- Uses a term without defining it first
- Skips a step in a calculation
- Says "obviously" or "clearly" (nothing is obvious to a beginner)
- Lacks a "why" (says WHAT to do but not WHY)
- Missing an analogy where one would help
- Has a wall of math without verbal explanation between steps

### Step 3: Fill the Gaps
For each gap found:
- Add the missing definition/explanation
- Add the skipped step
- Replace "obviously" with the actual reasoning
- Add the missing "why"
- Create an analogy
- Add verbal bridge between math steps

### Step 4: Output Improved Version
Rewrite the problematic sections and output the fixes. Either:
- Edit the existing file directly (if path given)
- Output the improved sections as text

## How to use

```
/feynman-check review erklaerung_blatt03.tex - are the explanations actually understandable?
```

```
/feynman-check check if a beginner could follow the subspace proof in section 2
```

## Quality checklist

After running, every section should pass these tests:
- [ ] Could a 15-year-old follow this? (no unexplained jargon)
- [ ] Is every "why" answered? (no unmotivated steps)
- [ ] Is there at least one analogy per topic?
- [ ] Are calculations step-by-step with no gaps?
- [ ] Are key formulas/rules in merkbox?
- [ ] Is there a summary at the end?

$ARGUMENTS
