# Generated Monosyllabic Verb Roots and Infinitives

This directory contains systematically generated JSON data for all possible monosyllabic verb roots and their infinitives in Igbo, following the repository's data structure conventions.

## Files

### 1. `generated-monosyllabic-roots.json`
Contains all monosyllabic verb roots formed by combining consonants with vowels.
- **Format**: JSON array of root objects following the prime-roots schema
- **Total entries**: 270 (30 consonants × 9 vowels)
- Each root includes:
  - `id`: Unique identifier (e.g., `"ba_generated"`)
  - `plain_name`: The root form (e.g., `"ba"`)
  - `syllable_id`: Reference to syllable (e.g., `"ba_mid"`)
  - `vowelGroup`: "A" or "E" based on first vowel
  - `gloss`: "generated_root"
  - `generated`: `true` flag
  - `consonant`: Source consonant
  - `vowel`: Source vowel

### 2. `generated-dialectal-roots.json`
Contains dialectal variations of monosyllabic verb roots.
- **Format**: JSON array of dialectal variation objects
- **Total entries**: 63 unique dialectal pairs
- Covers major dialectal alternation patterns:
  - L/R (la/ra, le/re, etc.)
  - B/V (ba/va, be/ve, etc.)
  - G/V (ga/va, go/vo, etc.)
  - F/P (fa/pa, fo/po, etc.)
  - J/Z (ja/za, jo/zo, etc.)
  - S/T (sa/ta, so/to, etc.)
  - Y/H (ya/ha, yo/ho, etc.)
- Each entry includes:
  - `id`: Unique identifier
  - `base_form`: Primary form
  - `dialectal_form`: Alternate form
  - `combined_form`: Display format (e.g., `"la / ra"`)
  - `base_consonant` and `dialectal_consonant`
  - `vowel` and `vowelGroup`
  - `syllable_id` and `dialectal_syllable_id`
  - `type`: "dialectal_variation"

### 3. `generated-infinitives.json`
Contains infinitives for all base monosyllabic verb roots.
- **Format**: JSON array of infinitive objects
- **Total entries**: 270
- **Vowel harmony rules applied**:
  - A-group vowels (a, ẹ, ị, ọ, ụ) → prefix `ị` (e.g., `ma` → `ịma`)
  - E-group vowels (e, i, o, u) → prefix `i` (e.g., `go` → `igo`)
- Each entry includes:
  - `id`: Unique identifier (e.g., `"ịma_infinitive"`)
  - `infinitive_form`: The infinitive (e.g., `"ịma"`)
  - `base_root_id`: Reference to root entry
  - `base_root`: Root form
  - `prefix`: The infinitive prefix (ị or i)
  - `vowelGroup`: A or E
  - `syllable_id`: Reference to infinitive syllable
  - `type`: "infinitive"

### 4. `generated-dialectal-infinitives.json`
Contains infinitives with dialectal variations.
- **Format**: JSON array of dialectal infinitive objects
- **Total entries**: 63 unique dialectal pairs
- Applies same vowel harmony rules as base infinitives
- Each entry includes:
  - `id`: Unique identifier
  - `infinitive_form`: Combined display (e.g., `"ịla / ịra"`)
  - `base_infinitive` and `dialectal_infinitive`
  - `base_root` and `dialectal_root`
  - `base_root_id`: Reference to dialectal root entry
  - `prefix`: The infinitive prefix
  - `vowelGroup`: A or E
  - `syllable_id` and `dialectal_syllable_id`
  - `type`: "dialectal_infinitive"

## Generation Method

All files were generated using the `generate_verb_roots.py` script, which:

1. Loads consonants from `language-data/consonants.json`
2. Loads vowels from `language-data/vowels.json`
3. Generates all possible consonant-vowel combinations
4. Identifies dialectal alternations from the consonants data
5. Applies vowel harmony rules to generate infinitives
6. Outputs structured JSON following repository schemas

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

### Base Forms (JSON)
```json
{
  "id": "ma_generated",
  "plain_name": "ma",
  "syllable_id": "ma_mid",
  "vowelGroup": "A",
  "gloss": "generated_root",
  "generated": true,
  "consonant": "m",
  "vowel": "a"
}
```

Infinitive:
```json
{
  "id": "ịma_infinitive",
  "infinitive_form": "ịma",
  "base_root_id": "ma_generated",
  "base_root": "ma",
  "prefix": "ị",
  "vowelGroup": "A",
  "syllable_id": "ịma_mid",
  "generated": true,
  "type": "infinitive"
}
```

### Dialectal Variations (JSON)
```json
{
  "id": "la_ra_dialectal",
  "base_form": "la",
  "dialectal_form": "ra",
  "combined_form": "la / ra",
  "base_consonant": "l",
  "dialectal_consonant": "r",
  "vowel": "a",
  "vowelGroup": "A",
  "syllable_id": "la_mid",
  "dialectal_syllable_id": "ra_mid",
  "generated": true,
  "type": "dialectal_variation"
}
```

## Usage

These JSON files can be:
- Loaded into applications via standard JSON parsers
- Queried for linguistic analysis
- Used as a comprehensive reference for Igbo verb morphology
- Integrated with other repository data via ID references

## Data Structure Notes

- All entries follow repository schema conventions
- IDs are unique and descriptive
- `generated: true` flag distinguishes generated data from manually curated entries
- Syllable IDs reference assumed mid-tone forms (tone data not included in generation)
- All entries use UTF-8 encoding with proper Igbo characters

## Regeneration

To regenerate these files:

```bash
python3 generate_verb_roots.py
```

The script will overwrite the existing JSON files with fresh data.

## Validation

Generated files pass repository validation:
```bash
python3 validate.py
```

Tests verify data integrity:
```bash
python3 test_generated_roots.py
```

## Notes

- Not all generated roots correspond to actual Igbo words
- This is a systematic generation of all possible phonological forms
- Actual meaning and usage should be verified against Igbo dictionaries
- Tone markings are not included in this generation (tones are crucial in Igbo)
- Each root would typically have high, mid, or low tone variants
- The `gloss` field is set to "generated_root" as these are not assigned specific meanings
