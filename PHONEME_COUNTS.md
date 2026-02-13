# Igbo Phoneme Count Documentation

## Summary

This document confirms the phoneme inventory of the Igbo language as represented in this repository.

### Current Counts in Repository

- **Regular Consonants**: 28
- **Syllabic Nasals (Pseudo-vowels)**: 2 (m̩, n̩)
- **Total Consonant Entries**: 30
- **Consonants with Dialectal Variations**: 20 (marked with `"shifting": true`)
- **Distinct Alternation Patterns**: 19
- **Vowels**: 9 (5 in A-group, 4 in E-group)

### Important Notes on Counting

1. **Dialectal Alternations**: 20 consonants participate in 19 alternation patterns (e.g., L/R, B/V, F/H/SH)
2. **Current methodology**: Each distinct consonant letter counts as ONE entry, regardless of how many alternation patterns it participates in
3. **Alternative methodologies** could yield counts of 49, 50, or potentially 42 depending on how alternating consonants are counted

### If the expected count is 42 consonants:
- Current file has **30 consonant entries**
- Would need **12 additional entries** to reach 42
- These additional entries may represent:
  - Dialectal variants listed as separate consonants
  - Alternative realizations of alternating consonants
  - Or a different counting methodology should be applied to existing data

## Detailed Breakdown

### Consonants (30 total)

#### Regular Consonants (28)
The repository contains 28 regular consonant phonemes:

1. **b** - Voiced bilabial plosive
2. **ch** - Voiceless postalveolar affricate
3. **d** - Voiced alveolar plosive
4. **f** - Voiceless labiodental fricative
5. **g** - Voiced velar plosive
6. **gb** - Voiced labial-velar plosive (distinctive Igbo sound)
7. **gh** - Voiced velar fricative
8. **gw** - Labialized voiced velar plosive
9. **h** - Voiceless glottal fricative
10. **j** - Voiced postalveolar affricate
11. **k** - Voiceless velar plosive
12. **kp** - Voiceless labial-velar plosive (distinctive Igbo sound)
13. **kw** - Labialized voiceless velar plosive
14. **l** - Alveolar lateral approximant
15. **m** - Bilabial nasal
16. **n** - Alveolar nasal
17. **ṅ** - Velar nasal
18. **nw** - Labialized velar nasal
19. **ny** - Palatal nasal
20. **p** - Voiceless bilabial plosive
21. **r** - Alveolar trill or tap
22. **s** - Voiceless alveolar fricative
23. **sh** - Voiceless postalveolar fricative
24. **t** - Voiceless alveolar plosive
25. **v** - Voiced labiodental fricative
26. **w** - Labial-velar approximant
27. **y** - Palatal approximant
28. **z** - Voiced alveolar fricative

#### Syllabic Nasals / Pseudo-vowels (2)
These consonants can function as the nucleus of a syllable, acting like vowels:

1. **m̩** (M̩) - Syllabic bilabial nasal
2. **n̩** (N̩) - Syllabic alveolar nasal

Called **myiriụdaume** (vowel-like) in Igbo, these are DISTINCT from regular consonants M and N.

**Examples:**
- **mmanụ** (oil) - first 'm' is syllabic
- **mmiri** (water) - first 'm' is syllabic
- **nnu** (salt) - first 'n' is syllabic
- **nne** (mother) - first 'n' is syllabic

### Vowels (9 total)

Igbo vowels are organized into two harmony groups:

#### A-Group Vowels (5) - Short and Sharp
1. **a** - Open front unrounded vowel
2. **ẹ** - Open-mid front unrounded vowel
3. **ị** - Near-close front unrounded vowel
4. **ọ** - Open-mid back rounded vowel
5. **ụ** - Near-close back rounded vowel

#### E-Group Vowels (4) - Tense and Close
1. **e** - Close-mid front unrounded vowel
2. **i** - Close front unrounded vowel
3. **o** - Close-mid back rounded vowel
4. **u** - Close back rounded vowel

## Consonant Alternation Patterns and Counting

The repository documents **19 distinct consonant alternation patterns** that represent systematic dialectal or phonological variations in Igbo. **20 consonants** participate in these alternation patterns.

### The 19 Alternation Patterns:

1. G/V - velar-labiodental alternation
2. N/L/Y - three-way nasal-lateral-palatal alternation
3. R/H - trill-fricative alternation
4. L/R - lateral-trill alternation (classic example: mili/miri "water")
5. Y/H - palatal-glottal alternation
6. F/H/SH - three-way fricative alternation
7. R/SH - trill-fricative alternation
8. J/Z - affricate-fricative alternation
9. S/SH - alveolar-postalveolar fricative alternation
10. B/V - plosive-fricative alternation
11. F/P - fricative-plosive alternation
12. B/W - plosive-approximant alternation
13. S/T - fricative-plosive alternation
14. F/V - voiceless-voiced labiodental pair
15. Y/GH - palatal-velar fricative alternation
16. R/F - trill-fricative alternation
17. W/GH - labial-velar alternation
18. NY/Ṅ - palatal-velar nasal merger
19. NW/Ṅ - labialized-velar nasal merger

### Counting Consonants with Alternations

The current file contains **30 distinct consonant entries**. However, different counting methodologies could yield different totals:

**Method 1 - Phonemic count (current): 30**
- Each unique consonant letter = 1 entry
- L and R are both in the file as separate consonants
- They are marked as participating in the L/R alternation pattern

**Method 2 - Phonemic + patterns: 49**
- 30 base consonants + 19 alternation patterns = 49

**Method 3 - Per-pattern instances: 50**  
- Count each consonant once for each alternation pattern it participates in
- Example: 'f' participates in 4 patterns, so would count as 4 instances

**Method 4 - Dialectal variants as separate entries: 42(?)**
- This may be the intended counting method
- Would require treating some alternating consonants as distinct dialect-specific forms
- _Requires clarification of which variants should be separate entries_

### Note on "42 Consonants"

If the expected count is 42 consonants, this likely means:
- Dialectal variants should be listed as separate consonant entries beyond the current 30
- OR a specific counting methodology should be used that yields 42
- **Current file has 30 entries; missing 12 entries to reach 42**

The 20 consonants marked with `"shifting": true` participate in alternation patterns, suggesting they have dialectal or contextual variants that may need to be enumerated separately.

## Notes on Phoneme Counting

### Why Not 42 Consonants?

Some sources may cite different consonant counts depending on:

1. **Dialectal Variations**: Different Igbo dialects may have additional sounds
2. **Orthographic vs. Phonemic**: Counting orthographic symbols vs. actual phonemes
3. **Allophonic Variants**: Including or excluding predictable sound variations
4. **Historical Changes**: Older descriptions may include sounds no longer distinct

### Standard Igbo Inventory

This repository follows **Standard Igbo** phonology as documented in:
- Modern Igbo linguistic literature
- The Ndebe orthography system
- Contemporary Igbo dictionaries

The counts of **28 regular consonants + 2 syllabic nasals = 30 total consonants** and **9 vowels** represent the consensus of contemporary Igbo linguistics.

## Validation

The `validate.py` script includes automated checks to confirm these counts:

```bash
python3 validate.py
```

This will verify:
- ✓ Regular consonants: 28
- ✓ Syllabic nasals: 2
- ✓ Total consonants: 30
- ✓ Total vowels: 9

## References

- Consonant inventory: `language-data/consonants.json`
- Vowel inventory: `language-data/vowels.json`
- Validation script: `validate.py`
