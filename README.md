# Igbo Language Structure Repository

## Overview

This repository breaks down the Igbo language into its fundamental components to facilitate linguistic analysis, resource development, and applications such as coining new words and language research.

## Key Characteristics of Igbo

### 1. **Verbal Nature**
The Igbo language is heavily verbal. Most words are either verbs or derived from verb roots. This repository reflects this by organizing linguistic data with a focus on verbal structures.

### 2. **Monosyllabic Verb Roots**
Most verb roots in Igbo are monosyllabic (single syllable), such as:
- `ma` (to know)
- `ba` (to enter/to cut - depending on tone)
- `ku` (to kindle)
- `wa` (to split)

### 3. **Tonal System**
Igbo is a tonal language with **three tones**: high, mid (unmarked), and low. The same phonetic sequence can represent completely different words depending on tone marking:
- `bá` (high tone) - different meaning
- `ba` (mid tone) - different meaning  
- `bà` (low tone) - different meaning

**Important**: Tone is a distinguishing feature, so each tonal variation counts as a separate word.

### 4. **Homophones and Homonyms**
Beyond tonal distinctions, Igbo also has many homophones - words with the **same sound AND the same tone but different meanings**:
- `má` (high tone) can mean "know", "beautiful", "strike", etc.
- `gbá` (high tone) can have 15+ different meanings

The repository handles this by:
- Creating separate entries for each meaning: `ma_001` (know), `ma_002` (beautiful), `ma_003` (strike)
- Using a `gloss` field in prime roots to distinguish meanings
- Using sequential numbering: `gba_001`, `gba_002`, ..., `gba_015` for roots with many meanings

### 5. **Vowel Harmony**
Igbo has a vowel harmony system where vowels are divided into two groups:

**A Group** (short and sharp sounds): `a`, `ẹ`, `ị`, `ọ`, `ụ`
**E Group** (tense vowels with close or rounded articulation): `e`, `i`, `o`, `u`

The vowel group of a verb root is determined by the **first vowel** in the root. For example:
- `ma` (to know) belongs to the A group
- `me` (to do/make) would belong to the E group

This harmony affects:
- Suffix and prefix selection in verb conjugation
- Word formation and derivation
- Proper combination of morphemes

### 6. **Phoneme Categorization**
The repository categorizes Igbo's phonetic inventory:

**Vowels**: Documented in `vowels.json` with A/E group classification
**Consonants**: Documented in `consonants.json`, including notes on:
- Shifting sounds (e.g., L/R interchange as in `mili`/`miri` for "water")
- Special Igbo consonants like `gb`, `kp`, `gw` (doubly-articulated sounds)
- Digraphs and special characters

### 7. **Affixation System**
Igbo uses both prefixes and suffixes to modify word meanings:

**Prefixes**: `e`, `o`, `a`, `i`, etc.
- Often mark nominalization or other grammatical functions

**Suffixes**: `go`, `la`, `ba`, `rọ`, etc.
- Often mark tense, aspect, or derivational changes

**Note**: A suffix like `ba` is distinct from the verb root `ba` - they are different lexical items with different functions.

## Repository Structure

```
igbo/
├── language-data/           # Core linguistic data
│   ├── vowels.json          # Vowel inventory with A/E group categorization
│   ├── consonants.json      # Consonant inventory with shifting sound notes
│   ├── syllables.json       # Phonetic inventory with tonal variations
│   ├── verbs/               # Verbal system (primary word class)
│   │   ├── prime-roots/     # Monosyllabic verb roots
│   │   ├── derived-roots/   # Compound/derived verb roots
│   │   ├── auxiliaries/     # Auxiliary verbs
│   │   ├── particles/       # Verbal particles
│   │   ├── prefixes/        # Verbal prefixes
│   │   ├── suffixes/        # Verbal suffixes
│   │   ├── verb-forms/      # Complete inflected forms
│   │   └── tenses.json      # Tense/aspect definitions
│   └── nouns/               # Nominal system
│       ├── basic.json       # Basic nouns
│       └── verbal_nouns.json # Deverbal nouns
└── resources/               # Reference dictionaries (PDFs)
```

## Data Organization

### Hierarchical Structure

The repository follows a **component-based hierarchy** that reflects Igbo morphology:

1. **Syllables** (atomic phonetic units)
   - Each syllable defined with tone (high/mid/low)
   - Forms the building blocks for all words

2. **Morphemes** (minimal meaning units)
   - Prime roots: monosyllabic verb roots
   - Prefixes: grammatical markers
   - Suffixes: aspectual/derivational markers
   - Particles: grammatical function words

3. **Words** (morpheme combinations)
   - Derived roots: combinations of prime roots
   - Verb forms: fully inflected verbs with affixes
   - Nouns: including deverbal nouns

### Data Format

All linguistic data is stored in **JSON format** with consistent schemas:

#### Syllables
```json
{
  "id": "ma_high",
  "tone": "high",
  "phonemes": ["m", "a"],
  "ndebe": ""
}
```

#### Prime Verb Roots
```json
{
  "id": "ma_001",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A"
}
```

#### Verb Forms (Complete Words)
```json
{
  "id": "ma_ama_simplePresent",
  "primeRoot": "ma_001",
  "auxiliary": "ama_001",
  "prefix": "prefix_a",
  "suffixes": ["suffix_rọ"],
  "particles": ["particle_na"],
  "meaning": {
    "id": "meaning_001",
    "description": "knowing"
  },
  "tense": "simplePresent"
}
```

## Design Principles

### 1. **Atomicity**
Break down words into their smallest meaningful components (morphemes and syllables).

### 2. **Tone Awareness**
Treat tonal variations as distinct lexical items with separate IDs and entries.

### 3. **Compositionality**
Represent complex forms through references to simpler components rather than duplication.

### 4. **Systematicity**
Use consistent schemas and naming conventions across all data files.

### 5. **Scalability**
Design the structure to accommodate hundreds or thousands of entries without becoming unwieldy.

## Adding New Data

### Before Adding Large Datasets

1. **Verify Schema Consistency**: Ensure new entries match the established JSON schemas
2. **Check for Duplicates**: Verify that the same morpheme with the same tone isn't already present
3. **Link Components**: Use IDs to reference existing syllables, roots, and morphemes
4. **Document Tone**: Always specify tone marking explicitly
5. **Categorize Correctly**: Distinguish between:
   - Verb roots vs. derived verbs
   - Suffixes vs. roots with same phonetic form
   - Prefixes vs. particles

### Workflow for Adding Verbs

1. Add/verify syllables with tones in `syllables.json`
2. Add prime root in `verbs/prime-roots/`
3. Add related prefixes in `verbs/prefixes/`
4. Add related suffixes in `verbs/suffixes/`
5. Create inflected forms in `verbs/verb-forms/`
6. Link components using consistent ID references

## Reference Materials

The `resources/` directory contains PDF dictionaries that can inform data entry:
- Blench Onitsha Igbo Dictionary
- Michael Echeruo Igbo Dictionary
- Northcote Igbo Dictionary (Volumes 2 & 5)

These dictionaries indicate word types (v. = verb, adv. = adverb, etc.) which should guide categorization.

## Contributing

When adding data:
1. Follow the established JSON schemas
2. Maintain tone distinctions
3. Use descriptive IDs
4. Link components rather than duplicating data
5. Add one category at a time for easier verification

## Schema Documentation

For detailed schema documentation and examples, see:
- `SCHEMA.md` - Complete schema specifications
- `docs/examples/` - Usage examples (coming soon)

## Future Development

- Expand noun categorization
- Add adverbs, adjectives, and other word classes
- Include dialectal variations
- Add pronunciation guides (IPA)
- Include usage examples and sample sentences
- Create validation scripts for data consistency

---

**Note**: This is a living document. As the repository grows and linguistic understanding deepens, this structure may be refined while maintaining backward compatibility where possible.
