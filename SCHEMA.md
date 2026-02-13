# Igbo Language Data Schema Documentation

This document defines the JSON schemas used throughout the repository to ensure consistency and facilitate data validation.

## Table of Contents
1. [Phonemes](#phonemes)
   - [Vowels](#vowels)
   - [Consonants](#consonants)
2. [Syllables](#syllables)
3. [Verb Components](#verb-components)
   - [Prime Roots](#prime-roots)
   - [Derived Roots](#derived-roots)
   - [Auxiliaries](#auxiliaries)
   - [Prefixes](#prefixes)
   - [Suffixes](#suffixes)
   - [Particles](#particles)
4. [Verb Forms](#verb-forms)
5. [Tenses](#tenses)
6. [Nouns](#nouns)
7. [Naming Conventions](#naming-conventions)

---

## Phonemes

### Vowels

**File Location**: `language-data/vowels.json`

**Purpose**: Defines the vowel inventory of Igbo, categorized into two harmony groups (A group and E group). This categorization is fundamental for understanding vowel harmony in verb conjugation and word formation.

**Schema**:
```json
{
  "vowelGroups": {
    "A": {
      "name": "string (group name)",
      "description": "string (phonetic description)",
      "vowels": [
        {
          "letter": "string (lowercase form)",
          "uppercase": "string (uppercase form)",
          "ipa": "string (IPA symbol)",
          "description": "string (phonetic description)"
        }
      ]
    },
    "E": {
      "name": "string (group name)",
      "description": "string (phonetic description)",
      "vowels": [...]
    }
  },
  "notes": ["array of strings (usage notes)"]
}
```

**Vowel Groups**:

**A Group** (short and sharp sounds):
- `a` / `A` - Open front unrounded vowel
- `ẹ` / `Ẹ` - Open-mid front unrounded vowel
- `ị` / `Ị` - Near-close front unrounded vowel
- `ọ` / `Ọ` - Open-mid back rounded vowel
- `ụ` / `Ụ` - Near-close back rounded vowel

**E Group** (tense vowels with close or rounded articulation):
- `e` / `E` - Close-mid front unrounded vowel
- `i` / `I` - Close front unrounded vowel
- `o` / `O` - Close-mid back rounded vowel
- `u` / `U` - Close back rounded vowel

**Notes**:
- Vowel harmony: verb roots and affixes must agree in vowel group
- The vowel group of a verb root is determined by the **first vowel** in the root
- A group vowels are characterized by short, sharp articulation
- E group vowels are characterized by tense articulation with close or rounded quality
- This distinction is crucial for proper suffix and prefix selection

---

### Consonants

**File Location**: `language-data/consonants.json`

**Purpose**: Defines the consonant inventory of Igbo, including special notes about sounds that can shift or vary in pronunciation.

**Schema**:
```json
{
  "consonants": [
    {
      "letter": "string (lowercase form)",
      "uppercase": "string (uppercase form)",
      "ipa": "string (IPA symbol)",
      "type": "string (consonant type)",
      "description": "string (phonetic description)",
      "shifting": "boolean (optional, indicates sound can shift)",
      "shifts_to": ["array of strings (optional, sounds it can shift to)"],
      "notes": "string (optional, additional information)"
    }
  ],
  "notes": ["array of strings (usage notes)"]
}
```

**Consonant Types**:
- **Plosive**: b, d, g, gb, gw, k, kp, kw, p, t
- **Fricative**: f, gh, h, s, sh, v, z
- **Affricate**: ch, j
- **Nasal**: m, n, ṅ, nw, ny
- **Lateral**: l
- **Trill**: r
- **Approximant**: w, y

**Shifting Sounds**:
Igbo has extensive consonant variation across dialects, with 19 interchange patterns documented from the Ndebe orthography system:

**Major Interchanges (Common):**
- **L/R**: The consonants `l` and `r` are interchangeable
  - Example: `mili` (water) may be pronounced as `miri`
- **F/P**: The consonants `f` and `p` can be interchangeable
- **S/T**: The consonants `s` and `t` can be interchangeable

**Fricative Variations:**
- **F/H/SH**: Complex pattern where `f`, `h`, and `sh` can shift among each other
- **R/H**: The consonants `r` and `h` can be interchangeable
- **R/SH**: The consonants `r` and `sh` can be interchangeable
- **S/SH**: The consonants `s` and `sh` can be interchangeable
- **Y/H**: The consonants `y` and `h` can be interchangeable

**Plosive-Fricative Shifts:**
- **B/V**: The consonants `b` and `v` can be interchangeable
- **B/W**: The consonants `b` and `w` can be interchangeable
- **G/V**: The consonants `g` and `v` can be interchangeable

**Complex Patterns:**
- **N/L/Y**: Three-way interchange among `n`, `l`, and `y`
- **F/V**: The consonants `f` and `v` can be interchangeable
- **R/F**: The consonants `r` and `f` can be interchangeable

**Approximant Shifts:**
- **Y/GH**: The consonants `y` and `gh` can be interchangeable
- **W/GH**: The consonants `w` and `gh` can be interchangeable

**Affricate Variation:**
- **J/Z**: The consonants `j` and `z` can be interchangeable

**Nasal Mergers:**
- **NY/Ṅ**: Palatal nasal `ny` can merge with velar nasal `ṅ`
- **NW/Ṅ**: Labialized velar nasal `nw` can merge with velar nasal `ṅ`

These variations are recognized and addressed by the Ndebe orthography system, which provides distinct symbols for each variant to maintain clarity in writing.

**Notes**:
- Igbo includes doubly-articulated sounds like `gb` (labial-velar) and `kp`
- Dotted consonants (e.g., `ṅ`) represent specific phonetic values
- Some consonants are digraphs (two-letter combinations representing single sounds)

---

## Syllables

**File Location**: `language-data/syllables.json`

**Purpose**: Defines the phonetic inventory of Igbo syllables with tonal variations. These are the atomic building blocks of all words.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "tone": "string (high|mid|low)",
  "phonemes": ["array of strings (individual sounds)"],
  "ndebe": "string (Ndebe orthography notation, optional)"
}
```

**Example**:
```json
{
  "id": "ma_high",
  "tone": "high",
  "phonemes": ["m", "a"],
  "ndebe": ""
}
```

**ID Convention**: `{syllable}_{tone}`
- Examples: `ma_high`, `ba_mid`, `ku_low`

**Notes**:
- Each tonal variation of a syllable requires a separate entry
- The `ndebe` field is reserved for the traditional Igbo orthography system
- Syllables can be consonant-only (e.g., "nm") or CV (consonant-vowel) patterns

---

## Verb Components

### Prime Roots

**File Location**: `language-data/verbs/prime-roots/{root}.json`

**Purpose**: Stores monosyllabic verb roots, which are the foundation of most Igbo words.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "plain_name": "string (the root without tone marking)",
  "syllable_id": "string (reference to syllables.json)",
  "vowelGroup": "string (vowel harmony group: A|E - determined by first vowel)",
  "gloss": "string (basic English meaning/gloss)"
}
```

**Example**:
```json
{
  "id": "ma_001",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A",
  "gloss": "know"
}
```

**ID Convention**: `{root}_{sequential_number}`
- Example: `ma_001`, `ma_002`, `ma_003` (different meanings, same syllable)
- Example: `ba_001`, `ba_002`, `ba_003`

**Notes**:
- `syllable_id` links to the specific tonal syllable
- `vowelGroup` indicates the vowel harmony group (A or E) based on the **first vowel** in the root:
  - **A group**: if first vowel is a, ẹ, ị, ọ, or ụ (short/sharp sounds)
  - **E group**: if first vowel is e, i, o, or u (tense vowels with close or rounded articulation)
  - This grouping is used for vowel harmony rules in affixation
- `gloss` provides the basic meaning to distinguish homophones
  - Keep glosses concise: use a single primary meaning (e.g., "beautiful" not "beautiful/beauty")
  - Use the most common English equivalent
  - If multiple English words are close, choose one (e.g., "strike" not "strike/hit")
- **IMPORTANT**: Multiple entries can share the same `plain_name` AND the same `syllable_id` (same tone) if they are homophones with different meanings
- For verb roots with multiple meanings (e.g., "gba" with 15+ meanings), create separate entries: `gba_001`, `gba_002`, ..., `gba_015`, etc.

---

### Derived Roots

**File Location**: `language-data/verbs/derived-roots/{root}.json`

**Purpose**: Stores compound verb roots formed by combining multiple prime roots through agglutination or other morphological processes.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "name": "string (the derived root)",
  "primeRootIds": ["array of strings (prime root IDs)"],
  "gloss": "string (basic English meaning/gloss)",
  "type": "string (derivation type, optional - e.g., 'agglutinated', 'compound')"
}
```

**Example**:
```json
{
  "id": "kuwa_001",
  "name": "kuwa",
  "primeRootIds": ["ku_001", "wa_001"],
  "gloss": "break",
  "type": "agglutinated"
}
```

**ID Convention**: `{derivedroot}_{sequential_number}`

**Notes**:
- The `primeRootIds` array lists the component prime root IDs (not plain names) in the order they combine
- Each ID in `primeRootIds` must reference a valid prime root entry
- The `gloss` field provides the meaning of the derived verb, which may not be directly predictable from its component parts
- The optional `type` field indicates how the verb was formed (e.g., "agglutinated" for verbs formed by joining verb roots together)
- Derived roots can be used just like prime roots in verb forms and other constructions

---

### Auxiliaries

**File Location**: `language-data/verbs/auxiliaries/{auxiliary}.json`

**Purpose**: Stores auxiliary verbs that combine with main verbs to express tense, aspect, or mood.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "name": "string (the auxiliary)",
  "syllables": [
    {
      "id": "string (syllable reference)",
      "name": "string (syllable text)",
      "tone": "string (high|mid|low)",
      "orthography": "string (writing system)"
    }
  ]
}
```

**Example**:
```json
{
  "id": "ama_001",
  "name": "ama",
  "syllables": [
    {
      "id": "a_low",
      "name": "a",
      "tone": "low",
      "orthography": "Ndebe"
    },
    {
      "id": "ma_high",
      "name": "ma",
      "tone": "high",
      "orthography": "Ndebe"
    }
  ]
}
```

**ID Convention**: `{auxiliary}_{sequential_number}`

**Notes**:
- Auxiliaries are multi-syllabic
- Each syllable is explicitly marked with its tone
- `orthography` typically indicates "Ndebe" (traditional Igbo script)

---

### Prefixes

**File Location**: `language-data/verbs/prefixes/{prefix}.json`

**Purpose**: Stores verbal prefixes that attach to verb roots or stems.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "name": "string (the prefix)",
  "function": "string (grammatical function, optional)",
  "syllable_id": "string (reference to syllables.json, optional)"
}
```

**Example**:
```json
{
  "id": "prefix_a",
  "name": "a",
  "function": "nominalization",
  "syllable_id": "a_high"
}
```

**ID Convention**: `prefix_{prefix_name}`

**Notes**:
- Prefixes often have grammatical rather than lexical meaning
- Common prefixes include: `a`, `e`, `o`, `i`
- The `function` field describes the grammatical role

---

### Suffixes

**File Location**: `language-data/verbs/suffixes/{suffix}.json`

**Purpose**: Stores verbal suffixes that mark tense, aspect, or derivation.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "name": "string (the suffix with tone marking)",
  "function": "string (grammatical function, optional)"
}
```

**Example**:
```json
{
  "id": "suffix_rọ",
  "name": "rọ",
  "function": "continuous_aspect"
}
```

**ID Convention**: `suffix_{suffix_name}`

**Notes**:
- Suffixes include tone marking in their names (e.g., `rọ` with underdot)
- Common suffixes include: `rọ`, `la`, `go`, `ba`
- A suffix `ba` is distinct from a verb root `ba`

---

### Particles

**File Location**: `language-data/verbs/particles/{particle}.json`

**Purpose**: Stores grammatical particles used with verbs.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "name": "string (the particle)",
  "type": "string (particle type)"
}
```

**Example**:
```json
{
  "id": "particle_na",
  "name": "na",
  "type": "regular"
}
```

**ID Convention**: `particle_{particle_name}`

**Notes**:
- Particles are function words with grammatical meaning
- Common particles include: `na`, `ga`, etc.

---

## Verb Forms

**File Location**: `language-data/verbs/verb-forms/{description}.json`

**Purpose**: Stores complete, inflected verb forms showing how components combine.

**Schema**:
```json
{
  "id": "string (unique identifier)",
  "primeRoot": "string (reference to prime root)",
  "auxiliary": "string (reference to auxiliary, optional)",
  "prefix": "string (reference to prefix, optional)",
  "suffixes": ["array of suffix references"],
  "particles": ["array of particle references"],
  "meaning": {
    "id": "string (meaning identifier)",
    "description": "string (English gloss)"
  },
  "tense": "string (tense/aspect category)"
}
```

**Example**:
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

**ID Convention**: `{root}_{auxiliary}_{tense}` or descriptive name

**Notes**:
- This is the highest level, showing complete word formation
- All component references should point to valid entries in other files
- The `meaning` object provides semantic information
- `tense` should match a key from `tenses.json`

---

## Tenses

**File Location**: `language-data/verbs/tenses.json`

**Purpose**: Defines the tense/aspect categories used in verb forms.

**Schema**:
```json
{
  "tenseKey": "string (descriptive name)"
}
```

**Example**:
```json
{
  "simplePresent": "Simple Present",
  "presentContinuous": "Present Continuous",
  "simpleFuture": "Simple Future",
  "imminentFuture": "Imminent Future",
  "pastContinuous": "Past Continuous",
  "futureContinuous": "Future Continuous",
  "presentPerfect": "Present Perfect",
  "pastPerfect": "Past Perfect"
}
```

**Notes**:
- Keys are camelCase identifiers
- Values are human-readable descriptions
- This list can be expanded as needed

---

## Nouns

### Basic Nouns

**File Location**: `language-data/nouns/basic.json`

**Purpose**: Stores basic nouns (non-deverbal).

**Schema** (To Be Defined):
```json
{
  "id": "string (unique identifier)",
  "name": "string (the noun)",
  "syllables": ["array of syllable references"],
  "meaning": {
    "id": "string",
    "description": "string"
  },
  "class": "string (noun class, optional)"
}
```

**Status**: Schema not yet finalized; file currently empty.

---

### Verbal Nouns

**File Location**: `language-data/nouns/verbal_nouns.json`

**Purpose**: Stores nouns derived from verbs (deverbal nouns).

**Schema** (To Be Defined):
```json
{
  "id": "string (unique identifier)",
  "name": "string (the verbal noun)",
  "derivedFrom": "string (reference to verb root)",
  "prefix": "string (nominalizing prefix)",
  "meaning": {
    "id": "string",
    "description": "string"
  }
}
```

**Status**: Schema not yet finalized; file currently empty.

---

## Naming Conventions

### General Principles

1. **Use underscores** in IDs to separate components: `ma_high`, `prefix_a`
2. **Use sequential numbers** for items that can have multiple variants: `ma_001`, `ma_002`
3. **Be descriptive** but concise in ID naming
4. **Preserve tone marking** in the `name` field using Unicode diacritics

### ID Patterns

| Component Type | ID Pattern | Example |
|---------------|------------|---------|
| Syllable | `{syllable}_{tone}` | `ma_high` |
| Prime Root | `{root}_{number}` | `ma_001` |
| Derived Root | `{root}_{number}` | `kuwa_001` |
| Auxiliary | `{auxiliary}_{number}` | `ama_001` |
| Prefix | `prefix_{name}` | `prefix_a` |
| Suffix | `suffix_{name}` | `suffix_rọ` |
| Particle | `particle_{name}` | `particle_na` |
| Verb Form | `{root}_{aux}_{tense}` or descriptive | `ma_ama_simplePresent` |

### Tone Representation

**In IDs**: Use descriptive words (`high`, `mid`, `low`)
**In Names**: Use Unicode diacritics
- High tone: acute accent (á, é, í, ó, ú)
- Mid tone: no marking (a, e, i, o, u)
- Low tone: grave accent (à, è, ì, ò, ù)

### Special Characters

- Use Unicode for special Igbo characters: `ọ`, `ụ`, `ṅ`, `ị`, etc.
- Represent the underdot consonant with Unicode combining diacritics

---

## Validation Guidelines

When adding new data, verify:

1. ✅ **Unique IDs**: No duplicate IDs within the same category
2. ✅ **Valid References**: All ID references point to existing entries
3. ✅ **Tone Consistency**: Syllables include tone; prime roots link to toned syllables
4. ✅ **Schema Compliance**: All required fields are present
5. ✅ **Naming Conventions**: IDs follow the established patterns
6. ✅ **JSON Validity**: Files parse correctly as JSON

---

## Future Schema Extensions

Planned additions:
- Adverbs schema
- Adjectives schema  
- Pronouns schema
- Ideophones schema
- Sentence structure examples
- Dialectal variation markers
- Etymology fields
- Usage frequency data
- Example sentences

---

**Last Updated**: 2026-02-13  
**Version**: 1.0
