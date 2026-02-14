# Generated Prime Roots and Infinitives

This directory contains systematically generated JSON data for all monosyllabic verb roots and their infinitives in Igbo.

## Files

### Prime Roots Directory (`prime-roots/`)

#### `generated-prime-roots.json`
Contains all 270 monosyllabic prime verb roots as a single comprehensive array.

**Why prime roots?** Monosyllabic verb roots like `ma`, `ku`, `ba` cannot be broken down further, making them prime roots. In contrast, `kuwa` is a derived root (ku + wa), not a prime root.

- **Format**: JSON array of root objects following the prime-roots schema
- **Total entries**: 270 (30 consonants × 9 vowels)
- Each root includes:
  - `id`: Unique identifier (e.g., `"ba_generated"`)
  - `plain_name`: The root form (e.g., `"ba"`)
  - `syllable_id`: Reference to syllable (e.g., `"ba_mid"`)
  - `vowelGroup`: "A" or "E" based on first vowel
  - `gloss`: "generated_root"
  - `generated`: `true` flag to distinguish from manually curated entries

**Example:**
```json
{
  "id": "ma_generated",
  "plain_name": "ma",
  "syllable_id": "ma_mid",
  "vowelGroup": "A",
  "gloss": "generated_root",
  "generated": true
}
```

### Collection Files (main `verbs/` directory)

#### `generated-dialectal-roots.json`
Contains 63 dialectal variations of monosyllabic verb roots.

**Dialectal patterns covered:**
- L/R (la/ra, le/re, etc.)
- B/V (ba/va, be/ve, etc.)
- G/V (ga/va, go/vo, etc.)
- F/P (fa/pa, fo/po, etc.)
- J/Z (ja/za, jo/zo, etc.)
- S/T (sa/ta, so/to, etc.)
- Y/H (ya/ha, yo/ho, etc.)

Each entry includes:
- `id`: Unique identifier
- `base_form`: Primary form
- `dialectal_form`: Alternate form
- `combined_form`: Display format (e.g., `"la / ra"`)
- `vowelGroup`: A or E
- Syllable references for both forms

#### `generated-infinitives.json`
Contains 270 infinitives for all base monosyllabic verb roots.

**Vowel harmony rules applied:**
- A-group vowels (a, ẹ, ị, ọ, ụ) → prefix `ị` (e.g., `ma` → `ịma`)
- E-group vowels (e, i, o, u) → prefix `i` (e.g., `go` → `igo`)

Each entry includes:
- `id`: Unique identifier
- `infinitive_form`: The infinitive (e.g., `"ịma"`)
- `base_root_id`: Reference to prime root
- `prefix`: The infinitive prefix (ị or i)
- `vowelGroup`: A or E
- `type`: "infinitive"

#### `generated-dialectal-infinitives.json`
Contains 63 infinitives with dialectal variations.

## Generation Method

All files were generated using the `generate_verb_roots.py` script, which:

1. Loads consonants from `language-data/consonants.json`
2. Loads vowels from `language-data/vowels.json`
3. Generates all possible consonant-vowel combinations (prime roots)
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

## Prime Roots vs. Derived Roots

**Prime Roots** (in `prime-roots/generated-prime-roots.json`):
- Monosyllabic: Single consonant + single vowel
- Cannot be broken down further
- Examples: `ma`, `ku`, `ba`, `go`
- Total: 270 (all possible CV combinations)

**Derived Roots** (in `derived-roots/` directory):
- Formed by combining prime roots
- Can be broken down into components
- Examples: 
  - `kuwa` = `ku` + `wa` (break)
  - Other compounds formed from prime roots

**Infinitives** (NOT prime roots):
- Derived forms with prefixes
- Examples: `ịma` (from `ma`), `igo` (from `go`)
- Stored separately as they are transformations of prime roots

## Usage

These JSON files can be:
- Loaded into applications via standard JSON parsers
- Queried for linguistic analysis
- Used as a comprehensive reference for Igbo verb morphology
- Integrated with other repository data via ID references

## Regeneration

To regenerate these files:

```bash
python3 generate_verb_roots.py
```

The script will create/overwrite:
- `prime-roots/generated-prime-roots.json` (270 prime roots)
- `generated-dialectal-roots.json` (63 dialectal variations)
- `generated-infinitives.json` (270 infinitives)
- `generated-dialectal-infinitives.json` (63 dialectal infinitives)

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
- The `generated: true` flag distinguishes these from manually curated entries
