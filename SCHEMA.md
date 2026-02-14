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
      "shifting": "boolean (optional, indicates sound participates in alternation patterns)",
      "alternation_sets": [
        {
          "pattern": "string (pattern name, e.g., 'R/H', 'Y/H', 'F/H/SH')",
          "alternates_with": ["array of strings (consonants in this specific pattern)"],
          "notes": "string (optional, context for this specific alternation)",
          "preferred_in_dialects": ["array of strings (optional, dialects that prefer this variant)"],
          "dialect_distribution": {
            "variant1": ["array of strings (dialects)"],
            "variant2": ["array of strings (dialects)"]
          }
        }
      ],
      "syllabic": "boolean (optional, indicates syllabic consonant that can function as vowel)",
      "functions_as": ["array of strings (optional, e.g., ['consonant', 'vowel'] for syllabic nasals)"],
      "igbo_name": "string (optional, Igbo name for the sound)",
      "notes": "string (optional, general information about the consonant)"
    }
  ],
  "notes": ["array of strings (usage notes)"]
}
```

**Key Fields**:
- `alternation_sets`: Array of distinct alternation patterns this consonant participates in
- `pattern`: Identifies the specific alternation (e.g., "R/H" vs "Y/H" are DIFFERENT patterns)
- `alternates_with`: Lists only the consonants in THIS specific pattern
- `preferred_in_dialects`: *(New)* Lists Igbo dialects that prefer this consonant variant
- `dialect_distribution`: *(New)* Maps each variant in the pattern to dialects that prefer it
- `syllabic`: Indicates if consonant can function as syllable nucleus (like syllabic nasals)
- `functions_as`: For syllabic sounds, lists their dual functions

**Dialect Preference Example**:
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

This structure enables:
- Dialect-specific text generation (e.g., use 'l' for Onitsha, 'r' for Owerri)
- Dialect conversion tools
- Regional variation documentation

**Consonant Types**:
- **Plosive**: b, d, g, gb, gw, k, kp, kw, p, t
- **Fricative**: f, gh, h, s, sh, v, z
- **Affricate**: ch, j
- **Nasal**: m, n, ṅ, nw, ny
- **Syllabic-Nasal** (Pseudo-Vowels): m̩, n̩
- **Lateral**: l
- **Trill**: r
- **Approximant**: w, y

**Syllabic Nasals (M̩/N̩) - Special Case**:

Igbo has **syllabic nasals** (m̩ and n̩) that function as both consonants and vowels. These are called **"myiriụdaume"** (vowel-like) in Igbo.

**Key Characteristics**:
- **Function as syllable nucleus**: Can serve as the core/vowel of a syllable
- **Phonetically nasal**: Still nasals in articulation
- **Distinct from regular M/N**: Regular m and n are only consonants
- **Marked in schema**: Have `"syllabic": true` and `"functions_as": ["consonant", "vowel"]`

**Examples**:
- **mmanụ** [m̩.ma.nʊ] - "oil" (first m is syllabic)
- **mmiri** [m̩.mi.ri] - "water" (first m is syllabic)
- **nnu** [n̩.nu] - "salt" (first n is syllabic)
- **nne** [n̩.ne] - "mother" (first n is syllabic)

This is a distinctive feature of Igbo phonology, allowing nasal sounds to function as vowels in word structure.

**Alternation Patterns**:

Igbo has 19 documented alternation patterns from the Ndebe orthography system. Each pattern is a DISTINCT phonological phenomenon that must be tracked separately.

**CRITICAL DISTINCTION: Pattern Identity**

Each alternation pattern is identified by its full designation (e.g., "R/H", "Y/H", "F/H/SH"). These are NOT interchangeable:

**Example - Multiple H Patterns:**
```json
{
  "letter": "h",
  "alternation_sets": [
    {"pattern": "R/H", "alternates_with": ["r"]},
    {"pattern": "Y/H", "alternates_with": ["y"]},
    {"pattern": "F/H/SH", "alternates_with": ["f", "sh"]}
  ]
}
```

These represent THREE DIFFERENT alternation phenomena:
- R/H: H that alternates specifically with R in certain environments
- Y/H: H that alternates specifically with Y in different environments  
- F/H/SH: H that participates in complex fricative pattern with F and SH

⚠️ **These cannot be freely mixed or treated as equivalent**

**Data Structure**:

Each consonant that participates in alternations has an `alternation_sets` array. Each set specifies:
- `pattern`: The full pattern name (e.g., "N/L/Y", "R/H")
- `alternates_with`: The specific consonants in that pattern only
- `notes`: Context for that specific alternation

**The 19 Patterns:**

**Major Interchanges:**
- **L/R**: Classic lateral-trill interchange (example: mili/miri "water")
- **F/P**: Fricative-plosive alternation
- **S/T**: Alveolar fricative-plosive alternation

**Fricative Patterns:**
- **F/H/SH**: Complex three-way fricative pattern
- **R/H**: R alternating with H
- **R/SH**: R alternating with SH  
- **S/SH**: Alveolar-postalveolar fricative
- **Y/H**: Y alternating with H

**Plosive-Fricative Alternations:**
- **B/V**: Bilabial plosive-labiodental fricative
- **B/W**: Bilabial plosive-approximant
- **G/V**: Velar plosive-labiodental fricative

**Complex Multi-Way Patterns:**
- **N/L/Y**: Three-way nasal-lateral-palatal alternation
- **F/V**: Voiceless-voiced labiodental pair
- **R/F**: Trill-fricative alternation

**Approximant Patterns:**
- **Y/GH**: Palatal-velar fricative alternation
- **W/GH**: Labial-velar-velar fricative alternation

**Affricate Pattern:**
- **J/Z**: Voiced affricate-fricative alternation

**Nasal Mergers:**
- **NY/Ṅ**: Palatal nasal-velar nasal merger
- **NW/Ṅ**: Labialized velar nasal-velar nasal merger

**Usage Notes**:
- Each pattern must be identified and distinguished from others
- Pattern names come from Ndebe orthography documentation
- A consonant may participate in multiple patterns (e.g., H in 3 patterns, F in 4 patterns)
- Each pattern represents distinct phonological conditioning
- Patterns are NOT freely interchangeable for word formation
- Documented variations are observational, not prescriptive rules

**Notes**:
- Igbo includes doubly-articulated sounds like `gb` (labial-velar) and `kp`
- Dotted consonants (e.g., `ṅ`) represent specific phonetic values
- Some consonants are digraphs (two-letter combinations representing single sounds)
- The alternation_sets structure enables precise identification of each pattern

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

**File Location**: `language-data/verbs/prime-roots/prime-verb-roots.json`

**Purpose**: Stores monosyllabic verb roots with tone variants, which are the foundation of most Igbo words.

**Schema**:
```json
{
  "id": "string (unique identifier in format syl_{syllable_group}_{###})",
  "plain_name": "string (the root with tone marking)",
  "main_vowel": "string (the main vowel character)",
  "tone": "string (high|mid|low)",
  "syllable_group": "string (the base syllable without tone)",
  "vowelGroup": "string (vowel harmony group: A|E - determined by first vowel)",
  "phonemes": ["string", "string"] (array of [consonant, vowel]),
  "ndebe": "string (placeholder for future use)",
  "unicode": "string (placeholder for future use)"
}
```

**Example** (showing all three tone variants for 'ma'):
```json
{
  "id": "syl_ma_001",
  "plain_name": "má",
  "main_vowel": "a",
  "tone": "high",
  "syllable_group": "ma",
  "vowelGroup": "A",
  "phonemes": ["m", "a"],
  "ndebe": "",
  "unicode": ""
},
{
  "id": "syl_ma_002",
  "plain_name": "ma",
  "main_vowel": "a",
  "tone": "mid",
  "syllable_group": "ma",
  "vowelGroup": "A",
  "phonemes": ["m", "a"],
  "ndebe": "",
  "unicode": ""
},
{
  "id": "syl_ma_003",
  "plain_name": "mà",
  "main_vowel": "a",
  "tone": "low",
  "syllable_group": "ma",
  "vowelGroup": "A",
  "phonemes": ["m", "a"],
  "ndebe": "",
  "unicode": ""
}
```

**ID Convention**: `syl_{syllable_group}_{###}`
- Each syllable has three entries (high, mid, low tone)
- Example: `syl_ma_001` (high), `syl_ma_002` (mid), `syl_ma_003` (low)
- Sequential numbering: 001 = high tone, 002 = mid tone, 003 = low tone

**Tone Marking**:
- **High tone**: acute accent (á, é, í, ó, ú, ẹ́, ị́, ọ́, ụ́)
- **Mid tone**: no accent (a, e, i, o, u, ẹ, ị, ọ, ụ)
- **Low tone**: grave accent (à, è, ì, ò, ù, ẹ̀, ị̀, ọ̀, ụ̀)
- For vowels without standard tone marks, the same form is used for all tones

**Phonemes**:
- `phonemes` is an array containing the consonant and vowel that make up the syllable
- Handles single consonants (b, m, etc.) and digraphs (gb, kp, gw, sh, ch, etc.)
- Example: "ba" → ["b", "a"], "gba" → ["gb", "a"], "kpị" → ["kp", "ị"]

**Notes**:
- `vowelGroup` indicates the vowel harmony group (A or E) based on the **first vowel** in the root:
  - **A group**: if first vowel is a, ẹ, ị, ọ, or ụ (short/sharp sounds)
  - **E group**: if first vowel is e, i, o, or u (tense vowels with close or rounded articulation)
  - This grouping is used for vowel harmony rules in affixation
- Each syllable has exactly three entries (one for each tone variant)
- All prime roots are stored in a single file: `prime-verb-roots.json`
- Total entries: 270 syllables × 3 tones = 810 entries

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
