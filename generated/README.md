# Generated Monosyllabic Verb Roots and Infinitives

This directory contains generated lists of all possible monosyllabic verb roots and their infinitives in Igbo.

## Files

### 1. `monosyllabic_verb_roots.txt`
Contains all monosyllabic verb roots formed by combining consonants with vowels.
- **Format**: `consonant + vowel` (e.g., `ba`, `ma`, `go`)
- **Total entries**: 270 (30 consonants × 9 vowels)
- Each root is classified by vowel group (A-group or E-group)

### 2. `dialectal_verb_roots.txt`
Contains dialectal variations of monosyllabic verb roots.
- **Format**: `base_root / dialectal_root` (e.g., `la / ra`, `ba / va`)
- **Total entries**: 63 unique dialectal pairs
- Covers major dialectal alternation patterns:
  - L/R (la/ra, le/re, etc.)
  - B/V (ba/va, be/ve, etc.)
  - G/V (ga/va, go/vo, etc.)
  - F/P (fa/pa, fo/po, etc.)
  - J/Z (ja/za, jo/zo, etc.)
  - S/T (sa/ta, so/to, etc.)
  - Y/H (ya/ha, yo/ho, etc.)

### 3. `infinitives.txt`
Contains infinitives for all base monosyllabic verb roots.
- **Format**: `prefix + root` (e.g., `ịma`, `igo`)
- **Total entries**: 270
- **Vowel harmony rules applied**:
  - A-group vowels (a, ẹ, ị, ọ, ụ) → prefix `ị` (e.g., `ma` → `ịma`)
  - E-group vowels (e, i, o, u) → prefix `i` (e.g., `go` → `igo`)

### 4. `dialectal_infinitives.txt`
Contains infinitives with dialectal variations.
- **Format**: `base_infinitive / dialectal_infinitive` (e.g., `ịla / ịra`)
- **Total entries**: 63 unique dialectal pairs
- Applies same vowel harmony rules as base infinitives

## Generation Method

All files were generated using the `generate_verb_roots.py` script, which:

1. Loads consonants from `language-data/consonants.json`
2. Loads vowels from `language-data/vowels.json`
3. Generates all possible consonant-vowel combinations
4. Identifies dialectal alternations from the consonants data
5. Applies vowel harmony rules to generate infinitives

## Vowel Harmony Rules

Igbo has a vowel harmony system with two groups:

### A-Group (ị prefix)
- Vowels: a, ẹ, ị, ọ, ụ
- Infinitive prefix: ị
- Examples: ma → ịma, ba → ịba, dọ → ịdọ

### E-Group (i prefix)
- Vowels: e, i, o, u
- Infinitive prefix: i
- Examples: go → igo, be → ibe, ku → iku

The vowel group is determined by the **first vowel** in the verb root.

## Examples

### Base Forms
```
ma → ịma (A-group: first vowel is 'a')
go → igo (E-group: first vowel is 'o')
ba → ịba (A-group: first vowel is 'a')
ku → iku (E-group: first vowel is 'u')
```

### Dialectal Variations
```
la / ra → ịla / ịra (L/R alternation)
ba / va → ịba / ịva (B/V alternation)
fa / pa → ịfa / ịpa (F/P alternation)
ja / za → ịja / ịza (J/Z alternation)
```

## Notes

- Not all generated roots may correspond to actual Igbo words
- This is a systematic generation of all possible phonological forms
- Actual meaning and usage should be verified against Igbo dictionaries
- Tone markings are not included in this generation (tones are crucial in Igbo)
- Each root would typically have high, mid, or low tone variants

## Regeneration

To regenerate these files:

```bash
python3 generate_verb_roots.py
```

The script will overwrite the existing files with fresh data.
