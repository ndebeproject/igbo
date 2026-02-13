# Igbo Phoneme Count Documentation

## Summary

This document confirms the phoneme inventory of the Igbo language as represented in this repository, based on standard Igbo phonology **including dialectal variations**.

### Confirmed Counts

- **Base Consonants**: 30 (28 regular + 2 syllabic nasals)
- **Major Dialectal Variant Forms**: 12
- **Total Consonants (including dialectal variants)**: **42**
- **Vowels**: 9 (5 in A-group, 4 in E-group)
- **Pseudovowel Consonant Category**: 1 (containing 2 syllabic nasals: m̩, n̩)

## Understanding the Count

The count of **42 consonants** includes:
1. **30 base consonant forms** - the phonemes documented in consonants.json
2. **12 major dialectal variant forms** - alternation patterns like L/R, B/V, etc.

This accounts for the fact that Igbo consonants exhibit significant **dialectal variation**, where different dialects may use different consonants in corresponding positions. For example, the L/R alternation means some dialects consistently use 'L' where others use 'R' (as in *mili* vs *miri* for "water").

### Dialect Preferences

Each major alternation pattern now includes dialect preference information in the JSON structure:

```json
{
  "letter": "l",
  "alternation_sets": [
    {
      "pattern": "L/R",
      "alternates_with": ["r"],
      "notes": "Classic lateral-trill interchange",
      "preferred_in_dialects": ["Onitsha", "Central Igbo"],
      "dialect_distribution": {
        "l": ["Onitsha", "Central Igbo"],
        "r": ["Owerri", "Umuleri", "Bonny"]
      }
    }
  ]
}
```

This structure allows applications to:
- Identify which consonant is preferred in a specific dialect
- Convert text between dialects by applying the appropriate alternations
- Document regional variations in pronunciation and spelling

## Detailed Breakdown

### Base Consonants (30 total)

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

## Major Dialectal Alternation Patterns (12)

These patterns represent major dialectal variations where different Igbo dialects systematically use different consonants. Each alternation pattern now includes **dialect preference information** indicating which variant is preferred in which dialect.

1. **L/R** - L and R interchange (e.g., *mili* vs *miri* "water")
   - **L** preferred in: Onitsha, Central Igbo
   - **R** preferred in: Owerri, Umuleri, Bonny

2. **B/V** - B and V alternate dialectally
   - **B** preferred in: Onitsha
   - **V** preferred in: Owerri, Umuleri

3. **G/V** - G and V interchange
   - **G** preferred in: Onitsha
   - **V** preferred in: Owerri

4. **F/H/SH** - Complex three-way fricative alternation

5. **S/SH** - Alveolar-postalveolar fricative alternation
   - **S** preferred in: Onitsha
   - **SH** preferred in: Owerri, Umuleri

6. **Y/H** - Palatal-glottal alternation
   - **Y** preferred in: Onitsha
   - **H** preferred in: Owerri

7. **N/L/Y** - Three-way nasal-lateral-palatal alternation

8. **J/Z** - Voiced affricate-fricative alternation
   - **J** preferred in: Onitsha
   - **Z** preferred in: Owerri

9. **S/T** - Fricative-plosive alternation
   - **S** preferred in: Onitsha
   - **T** preferred in: Owerri

10. **F/P** - Labiodental-bilabial alternation
    - **F** preferred in: Onitsha, Central Igbo
    - **P** preferred in: Owerri

11. **B/W** - Plosive-approximant alternation
    - **B** preferred in: Onitsha
    - **W** preferred in: Owerri

12. **W/GH** - Approximant-fricative alternation
    - **W** preferred in: Onitsha
    - **GH** preferred in: Owerri

When counting consonants **with dialectal variants**, we count each alternation pattern as representing an additional consonant form, giving us **42 total consonants**.

### Dialect Information

The consonants.json file now includes dialect preference information in the `alternation_sets`:
- `preferred_in_dialects`: Lists which dialects prefer this specific consonant
- `dialect_distribution`: Maps each variant in the pattern to the dialects that prefer it

This allows applications to select the appropriate consonant variant based on the target dialect.

### Additional Alternation Patterns (7)

The repository also documents 7 additional alternation patterns that represent more subtle phonological variations:

13. F/V - Voicing alternation
14. Y/GH - Palatal-velar alternation
15. R/F - Trill-fricative alternation
16. R/H - Trill-fricative alternation
17. R/SH - Trill-fricative alternation
18. NY/Ṅ - Palatal-velar nasal merger
19. NW/Ṅ - Labialized-velar nasal merger

**Total: 19 distinct alternation patterns documented**

## Notes on Phoneme Counting

### Why 42 Consonants?

The count of 42 consonants includes **both base forms and major dialectal variants**:
- 30 base consonant phonemes (found in consonants.json)
- +12 major dialectal variant forms (from alternation patterns)
- = **42 total consonant forms**

This counting method recognizes that Igbo dialects can systematically use different consonants in corresponding positions, making these variants important for comprehensive linguistic documentation.

### Alternative Counting Methods

Different sources may cite different consonant counts depending on:

1. **Dialectal Variations**: Different Igbo dialects may have additional sounds
2. **Orthographic vs. Phonemic**: Counting orthographic symbols vs. actual phonemes
3. **Allophonic Variants**: Including or excluding predictable sound variations
4. **Historical Changes**: Older descriptions may include sounds no longer distinct
5. **Counting Method**: Whether dialectal variants are counted separately

### Standard Igbo Inventory

This repository follows **Standard Igbo** phonology as documented in:
- Modern Igbo linguistic literature
- The Ndebe orthography system
- Contemporary Igbo dictionaries

**With dialectal variation counting:**
- **42 consonants** (30 base + 12 major dialectal variants)
- **9 vowels**
- **1 pseudovowel consonant category** (containing 2 syllabic nasals)

**Base phoneme counting:**
- **30 consonants** (28 regular + 2 syllabic nasals)
- **9 vowels**

## Validation

The `validate.py` script includes automated checks to confirm these counts:

```bash
python3 validate.py
```

This will verify:
- ✓ Base consonant forms: 30
- ✓ Major dialectal variants: 12
- ✓ Total consonants (with dialectal variants): 42
- ✓ Pseudo-vowel consonants: 2 (counted as 1 category)
- ✓ Total vowels: 9

You can also run the dedicated phoneme count test:

```bash
python3 test_phoneme_counts.py
```

## References

- Consonant inventory: `language-data/consonants.json`
- Vowel inventory: `language-data/vowels.json`
- Validation script: `validate.py`
- Test script: `test_phoneme_counts.py`
