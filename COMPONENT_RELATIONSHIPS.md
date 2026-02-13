# Language Component Relationships

This document explains how the different components of Igbo language data relate to each other.

## Component Hierarchy

```
┌─────────────────────────────────────────────────────┐
│                    SYLLABLES                        │
│              (Phonetic Building Blocks)             │
│                                                     │
│  - Each syllable has 3 tonal variants              │
│  - Examples: ma_high, ma_mid, ma_low               │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ referenced by
                   │
┌──────────────────▼──────────────────────────────────┐
│                  MORPHEMES                          │
│           (Minimal Meaning Units)                   │
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │ PRIME ROOTS (Monosyllabic Verb Roots)      │  │
│  │ - Each root references one syllable        │  │
│  │ - Examples: ma_001, ba_001                 │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │ PREFIXES (Grammatical Markers)             │  │
│  │ - Reference syllables                       │  │
│  │ - Examples: prefix_a, prefix_e             │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │ SUFFIXES (Tense/Aspect Markers)            │  │
│  │ - Store name with tone                      │  │
│  │ - Examples: suffix_rọ, suffix_la           │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │ PARTICLES (Function Words)                  │  │
│  │ - Examples: particle_na                     │  │
│  └─────────────────────────────────────────────┘  │
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │ AUXILIARIES (Multi-syllable Helpers)       │  │
│  │ - Reference multiple syllables              │  │
│  │ - Examples: ama_001                         │  │
│  └─────────────────────────────────────────────┘  │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ combined in
                   │
┌──────────────────▼──────────────────────────────────┐
│                  VERB FORMS                         │
│              (Complete Words)                       │
│                                                     │
│  Combines all components:                          │
│  - Prime Root                                       │
│  - Auxiliary (optional)                             │
│  - Prefix (optional)                                │
│  - Suffixes (optional)                              │
│  - Particles (optional)                             │
│  - Meaning                                          │
│  - Tense                                            │
└─────────────────────────────────────────────────────┘
```

## Data Flow Example

Let's trace how the word "knowing" (in simple present tense) is constructed:

### Step 1: Syllables
```json
// syllables.json contains:
{
  "id": "ma_high",
  "tone": "high",
  "phonemes": ["m", "a"],
  "ndebe": ""
}
```

### Step 2: Prime Root
```json
// verbs/prime-roots/ma.json references the syllable:
{
  "id": "ma_001",
  "plain_name": "ma",
  "syllable_id": "ma_high",  // ← Reference to syllable
  "vowelGroup": "A"
}
```

### Step 3: Auxiliary
```json
// verbs/auxiliaries/ama.json uses syllables:
{
  "id": "ama_001",
  "name": "ama",
  "syllables": [
    {
      "id": "a_low",          // ← Reference to syllable
      "name": "a",
      "tone": "low",
      "orthography": "Ndebe"
    },
    {
      "id": "ma_high",        // ← Reference to syllable
      "name": "ma",
      "tone": "high",
      "orthography": "Ndebe"
    }
  ]
}
```

### Step 4: Prefix
```json
// verbs/prefixes/a.json:
{
  "id": "prefix_a",
  "name": "a",
  "function": "nominalization",
  "syllable_id": "a_high"    // ← Reference to syllable
}
```

### Step 5: Suffix
```json
// verbs/suffixes/ro_dot.json:
{
  "id": "suffix_rọ",
  "name": "rọ",
  "function": "continuous_aspect"
}
```

### Step 6: Particle
```json
// verbs/particles/na.json:
{
  "id": "particle_na",
  "name": "na",
  "type": "regular"
}
```

### Step 7: Complete Verb Form
```json
// verbs/verb-forms/ma-aorist.json combines everything:
{
  "id": "ma_ama_simplePresent",
  "primeRoot": "ma_001",           // ← Reference to prime root
  "auxiliary": "ama_001",          // ← Reference to auxiliary
  "prefix": "prefix_a",            // ← Reference to prefix
  "suffixes": ["suffix_rọ"],       // ← Reference to suffix
  "particles": ["particle_na"],    // ← Reference to particle
  "meaning": {
    "id": "meaning_001",
    "description": "knowing"
  },
  "tense": "simplePresent"         // ← Reference to tense
}
```

## Component Types and Their Roles

### 1. Syllables
- **Role**: Atomic phonetic units
- **Tonal**: Yes (3 variants each)
- **Referenced by**: Prime roots, prefixes, auxiliaries
- **File**: Single `syllables.json` array

### 2. Prime Roots
- **Role**: Monosyllabic verb roots (lexical core)
- **Tonal**: Yes (via syllable reference)
- **References**: Syllables
- **Files**: One per root in `verbs/prime-roots/`

### 3. Derived Roots
- **Role**: Compound verb roots
- **Tonal**: Inherited from components
- **References**: Prime root names
- **Files**: One per root in `verbs/derived-roots/`

### 4. Prefixes
- **Role**: Grammatical markers (often nominalization)
- **Tonal**: Yes (via syllable reference)
- **References**: Syllables
- **Files**: One per prefix in `verbs/prefixes/`

### 5. Suffixes
- **Role**: Tense/aspect/derivation markers
- **Tonal**: Yes (in name field)
- **References**: None
- **Files**: One per suffix in `verbs/suffixes/`

### 6. Particles
- **Role**: Grammatical function words
- **Tonal**: Usually fixed
- **References**: None
- **Files**: One per particle in `verbs/particles/`

### 7. Auxiliaries
- **Role**: Support verbs for tense/aspect
- **Tonal**: Yes (multi-syllabic with tone)
- **References**: Multiple syllables
- **Files**: One per auxiliary in `verbs/auxiliaries/`

### 8. Verb Forms
- **Role**: Complete, inflected words
- **Tonal**: Inherited from components
- **References**: All component types
- **Files**: One or more forms per file in `verbs/verb-forms/`

## Reference Chain Example

```
Verb Form: "má àmá rọ" (knowing - continuous present)
    ↓
├─→ primeRoot: "ma_001"
│       ↓
│   └─→ syllable_id: "ma_high"
│           ↓
│       Phonemes: ["m", "a"] with HIGH tone
│
├─→ auxiliary: "ama_001"
│       ↓
│   ├─→ syllables[0]: "a_low" (à)
│   └─→ syllables[1]: "ma_high" (má)
│
├─→ suffix: "suffix_rọ"
│       ↓
│   Name: "rọ" (with underdot)
│
└─→ tense: "simplePresent"
        ↓
    From tenses.json: "Simple Present"
```

## Design Benefits

### 1. No Duplication
- Syllables defined once, referenced many times
- Tonal variants stored at syllable level
- Component reuse across words

### 2. Consistency
- All ma_high references point to same definition
- Changes to syllables propagate to all words

### 3. Modularity
- Add new roots without modifying syllables
- Add new verb forms without duplicating morphemes
- Easy to expand each category independently

### 4. Scalability
- Can add hundreds of roots efficiently
- Reference system keeps files manageable
- Clear separation of concerns

### 5. Linguistic Accuracy
- Reflects actual morphological structure
- Captures compositionality
- Maintains tonal distinctions

## File Relationships Diagram

```
syllables.json (shared phonetic inventory)
     ↑
     │ referenced by
     │
     ├─→ verbs/prime-roots/*.json
     ├─→ verbs/prefixes/*.json
     └─→ verbs/auxiliaries/*.json
     
                  ↑
                  │ referenced by
                  │
         verbs/verb-forms/*.json
                  ↑
                  │ also references
                  │
         ├─→ verbs/suffixes/*.json
         ├─→ verbs/particles/*.json
         └─→ verbs/tenses.json
```

## Best Practices for Maintaining Relationships

1. **Always verify syllables exist** before creating roots or prefixes
2. **Use consistent ID naming** to make references predictable
3. **Document the meaning** at the verb form level (highest level)
4. **Link through IDs** not names (IDs are unique, names may not be)
5. **Validate references** using the validation script

## Adding New Components Checklist

- [ ] Check if required syllables exist
- [ ] Add missing syllables if needed
- [ ] Create morpheme file(s)
- [ ] Use correct ID format
- [ ] Reference existing IDs
- [ ] Create verb form showing usage
- [ ] Validate JSON
- [ ] Test references resolve

---

This component-based structure allows the repository to scale to thousands of entries while maintaining clarity and avoiding redundancy.
