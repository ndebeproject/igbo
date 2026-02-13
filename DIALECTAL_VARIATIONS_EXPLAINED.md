# Understanding Dialectal Consonant Variations in Igbo

## User's Concern

> "what happened to all the consonants i gave you that change by dialect like L/R"

This document addresses the counting and representation of Igbo consonants that exhibit dialectal variations.

## Current State

The repository contains **30 consonant entries** in `consonants.json`:
- 28 regular consonants
- 2 syllabic nasals (m̩, n̩)

Of these, **20 consonants** are marked with `"shifting": true` and participate in **19 alternation patterns**.

## The L/R Example

L and R are both present in the consonants list as **separate entries**:

```json
{
  "letter": "l",
  "type": "lateral",
  "alternation_sets": [
    {
      "pattern": "L/R",
      "alternates_with": ["r"]
    }
  ]
}

{
  "letter": "r",  
  "type": "trill",
  "alternation_sets": [
    {
      "pattern": "L/R",
      "alternates_with": ["l"]
    }
  ]
}
```

**Example**: The word for "water" is:
- `mili` in some dialects (using L)
- `miri` in other dialects (using R)

Both L and R are counted (2 consonants), and their alternation is documented in the pattern "L/R".

## All 20 Alternating Consonants

These consonants participate in dialectal or phonological alternation patterns:

1. **b** - B/V, B/W patterns
2. **f** - F/H/SH, F/P, F/V, R/F patterns (4 patterns)
3. **g** - G/V pattern
4. **gh** - Y/GH, W/GH patterns
5. **h** - R/H, Y/H, F/H/SH patterns (3 patterns)
6. **j** - J/Z pattern
7. **l** - N/L/Y, L/R patterns
8. **n** - N/L/Y pattern
9. **ṅ** - NY/Ṅ, NW/Ṅ patterns
10. **nw** - NW/Ṅ pattern
11. **ny** - NY/Ṅ pattern
12. **p** - F/P pattern
13. **r** - R/H, L/R, R/SH, R/F patterns (4 patterns)
14. **s** - S/SH, S/T patterns
15. **sh** - F/H/SH, R/SH, S/SH patterns (3 patterns)
16. **t** - S/T pattern
17. **v** - G/V, B/V, F/V patterns (3 patterns)
18. **w** - B/W, W/GH patterns
19. **y** - N/L/Y, Y/H, Y/GH patterns (3 patterns)
20. **z** - J/Z pattern

## The 19 Distinct Alternation Patterns

1. **B/V** - bilabial plosive ↔ labiodental fricative
2. **B/W** - bilabial plosive ↔ approximant
3. **F/H/SH** - three-way fricative alternation
4. **F/P** - fricative ↔ plosive
5. **F/V** - voiceless ↔ voiced labiodental
6. **G/V** - velar plosive ↔ labiodental fricative
7. **J/Z** - affricate ↔ fricative
8. **L/R** - lateral ↔ trill (classic example: mili/miri "water")
9. **N/L/Y** - three-way nasal-lateral-palatal
10. **NW/Ṅ** - labialized velar ↔ velar nasal
11. **NY/Ṅ** - palatal ↔ velar nasal
12. **R/F** - trill ↔ fricative
13. **R/H** - trill ↔ glottal fricative
14. **R/SH** - trill ↔ postalveolar fricative
15. **S/SH** - alveolar ↔ postalveolar fricative
16. **S/T** - fricative ↔ plosive
17. **W/GH** - approximant ↔ velar fricative
18. **Y/GH** - palatal ↔ velar fricative
19. **Y/H** - palatal ↔ glottal fricative

## Counting Methodologies

Different ways to count consonants with dialectal variations:

### Method 1: Unique Letter Forms (Current - 30 total)
- Each unique consonant letter = 1 entry
- L = 1, R = 1
- Total: 30 consonants

### Method 2: Base + Pattern Count (49 total)
- 30 base consonants + 19 alternation patterns = 49
- This counts the patterns themselves as separate entities

### Method 3: Per-Pattern Instances (50 total)
- Each consonant counted once per pattern it participates in
- L participates in 2 patterns → counts as 2
- R participates in 4 patterns → counts as 4
- Total: 50

### Method 4: Dialectal Variants as Separate Entries (42?)
- **This may be what the user intended**
- Would require 12 additional consonant entries beyond the current 30
- These could be:
  - Dialect-specific variants listed separately
  - Alternative realizations of alternating consonants
  - Additional consonants not currently in the file

## Question for User

To reach a count of **42 consonants**, we need to understand:

1. **Should dialectal variants be separate entries?**
   - Currently: L and R are separate entries (both counted)
   - Should there be: L-Dialect1, R-Dialect2 as distinct entries?

2. **Are there missing consonants?**
   - The current file has 30 entries
   - 42 - 30 = **12 missing entries**
   - What are these 12 additional consonants or variants?

3. **Should we use a different counting method?**
   - Methods 2 and 3 give us 49-50 (too high)
   - Method 1 gives us 30 (current)
   - What methodology yields exactly 42?

## Current Documentation Status

✅ **What's documented**:
- All 30 consonant letters are in the file
- All 20 alternating consonants are marked with `"shifting": true`
- All 19 alternation patterns are documented with pattern names
- Each consonant lists which patterns it participates in

⚠️ **What needs clarification**:
- Whether dialectal variants should be separate consonant entries
- Which specific consonants or variants are missing to reach 42
- The correct counting methodology for your use case

## Verification

Run validation to see current counts:
```bash
python3 validate.py
```

Output shows:
- Total consonants: 30
- Consonants with alternations: 20
- Distinct alternation patterns: 19

See `PHONEME_COUNTS.md` for complete details on all consonants and their alternation patterns.
