# Igbo Phoneme Count Documentation

## Summary

This document confirms the phoneme inventory of the Igbo language as represented in this repository, based on standard Igbo phonology.

### Confirmed Counts

- **Regular Consonants**: 28
- **Syllabic Nasals (Pseudo-vowels)**: 2
- **Total Consonants**: 30
- **Vowels**: 9 (5 in A-group, 4 in E-group)

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

## Consonant Alternation Patterns

The repository documents 19 distinct consonant alternation patterns that occur in Igbo:

1. G/V
2. N/L/Y (three-way)
3. R/H
4. L/R
5. Y/H
6. F/H/SH (three-way)
7. R/SH
8. J/Z
9. S/SH
10. B/V
11. F/P
12. B/W
13. S/T
14. F/V
15. Y/GH
16. R/F
17. W/GH
18. NY/Ṅ
19. NW/Ṅ

These patterns represent systematic phonological variations that occur in different dialects or phonological contexts.

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
