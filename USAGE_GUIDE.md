# Igbo Language Repository - Usage Guide

This guide provides practical instructions for working with the Igbo language data repository.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Understanding the Structure](#understanding-the-structure)
3. [Adding New Data](#adding-new-data)
4. [Common Workflows](#common-workflows)
5. [Best Practices](#best-practices)
6. [Examples](#examples)

---

## Getting Started

### Repository Overview

This repository organizes Igbo language data into a hierarchical structure that reflects the morphological nature of the language:

- **Bottom layer**: Syllables (phonetic units with tones)
- **Middle layer**: Morphemes (roots, prefixes, suffixes, particles)
- **Top layer**: Words (complete forms with meanings)

### Key Concepts

**Tonal Distinctions**: Igbo has three tones (high, mid, low). Each tonal variant is a distinct word:
- `má` = high tone (one meaning)
- `ma` = mid tone (different meaning)
- `mà` = low tone (yet another meaning)

**Verbal Nature**: Most Igbo words are verbs or verb-derived, so the repository emphasizes verbal structures.

**Compositionality**: Complex words reference simpler components rather than duplicating information.

---

## Understanding the Structure

### Directory Organization

```
language-data/
├── syllables.json              # All syllables with tones
├── verbs/
│   ├── prime-roots/            # One file per monosyllabic root
│   ├── derived-roots/          # Compound roots
│   ├── auxiliaries/            # Auxiliary verbs
│   ├── prefixes/               # Verbal prefixes (e, o, a, i, etc.)
│   ├── suffixes/               # Verbal suffixes (go, la, ba, rọ, etc.)
│   ├── particles/              # Grammatical particles
│   ├── verb-forms/             # Complete inflected forms
│   └── tenses.json             # Tense/aspect inventory
└── nouns/
    ├── basic.json              # Basic nouns
    └── verbal_nouns.json       # Nouns derived from verbs
```

### How Components Link

```
Verb Form
    ↓ references
Prime Root → references → Syllable (with tone)
Auxiliary → references → Syllables (with tones)
Prefix → references → Syllable (with tone)
Suffix → (stores name with tone)
Particle → (stores name)
```

Example chain:
- Syllable `ma_high` defines the sound [mă] with high tone
- Prime root `ma_001` references `ma_high`
- Verb form `ma_ama_simplePresent` references `ma_001` plus auxiliaries, affixes, etc.

---

## Adding New Data

### Step-by-Step Process

#### 1. Adding a New Verb Root

**Example**: Adding the verb root "ba" (to enter) with high tone

1. **Check if syllable exists** in `syllables.json`:
```bash
grep -i '"id": "ba_high"' language-data/syllables.json
```

2. **If syllable doesn't exist, add it**:
```json
{
  "id": "ba_high",
  "tone": "high",
  "phonemes": ["b", "a"],
  "ndebe": ""
}
```

3. **Determine the next sequential ID**: Check existing prime roots for "ba" to find the next number
```bash
ls language-data/verbs/prime-roots/ba-*.json
# If ba-001.json exists, use ba_002 for the ID
```

4. **Create the prime root file** at `verbs/prime-roots/ba-001.json` (or ba-002.json, etc.):
```json
{
  "id": "ba_001",
  "plain_name": "ba",
  "syllable_id": "ba_high",
  "vowelGroup": "A",
  "gloss": "enter"
}
```

**Important**: The `gloss` field is required to distinguish homophones (same sound, same tone, different meanings).

5. **Document its usage** by creating entries in `verbs/verb-forms/` showing how it's used in context.

#### 1b. Adding Homophones (Same Sound, Same Tone, Different Meanings)

**Example**: Adding multiple meanings of "ma" with high tone

Igbo verb roots can have multiple meanings with the same phonetic form and tone. For example, "má" (high tone) can mean "know", "beautiful", "strike", etc.

1. **Check existing entries**:
```bash
ls language-data/verbs/prime-roots/ma-*.json
# Shows: ma-001.json, ma-002.json, etc.
```

2. **Create a new file with the next sequential number**:
```json
// verbs/prime-roots/ma-004.json
{
  "id": "ma_004",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A",
  "gloss": "wipe/smear"
}
```

3. **File naming convention for homophones**:
- `ma-001.json` → ma_001 (know)
- `ma-002.json` → ma_002 (beautiful)
- `ma-003.json` → ma_003 (strike)
- `ma-004.json` → ma_004 (wipe)

**Scalability Note**: This structure easily handles roots like "gba" which may have 15+ different meanings. Simply create `gba-001.json` through `gba-015.json` (or more), each with a distinct `gloss` field.

#### 2. Adding a Prefix

**Example**: Adding prefix "ọ"

1. **Check if syllable exists** for "ọ" with the appropriate tone.

2. **If not, add syllable**:
```json
{
  "id": "ọ_high",
  "tone": "high",
  "phonemes": ["ọ"],
  "ndebe": ""
}
```

3. **Create prefix file** at `verbs/prefixes/ọ.json`:
```json
{
  "id": "prefix_ọ",
  "name": "ọ",
  "function": "nominalization",
  "syllable_id": "ọ_high"
}
```

#### 3. Adding a Suffix

**Example**: Adding suffix "la"

1. **Create suffix file** at `verbs/suffixes/la.json`:
```json
{
  "id": "suffix_la",
  "name": "la",
  "function": "completive_aspect"
}
```

Note: Suffixes may not always reference syllables directly but should include tone in the name.

#### 4. Adding a Complete Verb Form

**Example**: Creating an inflected verb in simple present tense

1. **Ensure all components exist**: prime root, auxiliary, prefix, suffix, particle

2. **Create verb form file** at `verbs/verb-forms/descriptive-name.json`:
```json
{
  "id": "ba_ama_simplePresent",
  "primeRoot": "ba_001",
  "auxiliary": "ama_001",
  "prefix": "prefix_a",
  "suffixes": ["suffix_la"],
  "particles": ["particle_na"],
  "meaning": {
    "id": "meaning_002",
    "description": "entering"
  },
  "tense": "simplePresent"
}
```

---

## Common Workflows

### Workflow 1: Adding Multiple Verb Roots from a Dictionary

1. **Prepare a list** of verbs with their tones from reference dictionaries
2. **Group by syllable**: Identify which new syllables need to be added
3. **Add syllables in batch** to `syllables.json`
4. **Create prime root files** one per verb root
5. **Document meanings** through verb forms

### Workflow 2: Expanding Tense Coverage

1. **Identify the tense** to add (check `verbs/tenses.json`)
2. **If new, add tense** to `tenses.json`:
```json
"remotePast": "Remote Past"
```
3. **Create verb forms** showing how existing roots appear in this tense
4. **Document auxiliary and affix patterns** for the tense

### Workflow 3: Adding Deverbal Nouns

1. **Identify the source verb** (ensure it exists in prime-roots)
2. **Identify the nominalizing prefix** (e, o, a, i, etc.)
3. **Create entry in `nouns/verbal_nouns.json`**:
```json
{
  "id": "noun_verb_001",
  "name": "ómá",
  "derivedFrom": "ma_001",
  "prefix": "prefix_o",
  "meaning": {
    "id": "meaning_noun_001",
    "description": "knowledge"
  }
}
```

---

## Best Practices

### 1. Consistency is Key
- Always use the same ID format within a category
- Follow established naming conventions
- Maintain the same JSON structure

### 2. Link, Don't Duplicate
- Use references (IDs) rather than copying data
- If a syllable exists, reference it
- Build complex forms from simpler components

### 3. Tone Awareness
- Always mark tone explicitly
- Create separate entries for different tones
- Use Unicode diacritics in the `name` field

### 4. Gloss Field Best Practices
- **Keep it concise**: Use a single primary meaning
- **Be specific**: Choose the most common English equivalent
- **Avoid multiple terms**: Use "beautiful" not "beautiful/beauty"
- **Single word preferred**: "strike" not "strike/hit"
- **Consistency**: Use the same gloss across related forms

### 5. Verify Before Adding
- Check for existing entries to avoid duplicates
- Validate JSON syntax before committing
- Test that all references resolve correctly

### 5. File Naming
- Use descriptive names for verb form files
- **Prime root files**: Use `{root}-{number}.json` format (e.g., `ma-001.json`, `ma-002.json`, `gba-001.json` through `gba-015.json`)
- Use the morpheme itself for prefix/suffix files
- This allows multiple homophones with the same root name

### 6. Documentation
- Include the `meaning` object for verb forms
- Add `function` field for prefixes and suffixes
- Document unusual patterns or exceptions

---

## Examples

### Example 1: Complete Workflow for a New Verb

**Adding "zụ" (to buy) with high tone**

Step 1 - Add syllable:
```json
// In syllables.json
{
  "id": "zụ_high",
  "tone": "high",
  "phonemes": ["z", "ụ"],
  "ndebe": ""
}
```

Step 2 - Add prime root:
```json
// In verbs/prime-roots/zụ-001.json
{
  "id": "zụ_001",
  "plain_name": "zụ",
  "syllable_id": "zụ_high",
  "vowelGroup": "U",
  "gloss": "buy"
}
```

Step 3 - Add verb form:
```json
// In verbs/verb-forms/zụ-present.json
{
  "id": "zụ_na_simplePresent",
  "primeRoot": "zụ_001",
  "auxiliary": null,
  "prefix": null,
  "suffixes": [],
  "particles": ["particle_na"],
  "meaning": {
    "id": "meaning_zụ_001",
    "description": "buying"
  },
  "tense": "simplePresent"
}
```

### Example 2: Handling Homophones (Same Sound + Tone, Different Meanings)

**Multiple "ma" roots with high tone but different meanings**

```json
// In verbs/prime-roots/ma-001.json
{
  "id": "ma_001",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A",
  "gloss": "know"
}

// In verbs/prime-roots/ma-002.json
{
  "id": "ma_002",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A",
  "gloss": "beautiful"
}

// In verbs/prime-roots/ma-003.json
{
  "id": "ma_003",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A",
  "gloss": "strike"
}
```

**Key Points**:
- All three share the same `syllable_id` (ma_high) - same pronunciation and tone
- Each has a unique `id` (ma_001, ma_002, ma_003)
- The `gloss` field distinguishes the meanings
- File names include the ID number (ma-001.json, ma-002.json, ma-003.json)

### Example 3: Distinguishing Homophonous Morphemes (Root vs. Suffix)

**"ba" as verb root vs. "ba" as suffix**

Verb root:
```json
// In verbs/prime-roots/ba-001.json
{
  "id": "ba_001",
  "plain_name": "ba",
  "syllable_id": "ba_high",
  "vowelGroup": "A",
  "gloss": "enter"
}
```

Suffix:
```json
// In verbs/suffixes/ba.json
{
  "id": "suffix_ba",
  "name": "ba",
  "function": "imperative"
}
```

### Example 4: Compound Verb Root

**"kuwa" from "ku" + "wa"**

```json
// In verbs/derived-roots/kuwa.json
{
  "id": "kuwa_001",
  "name": "kuwa",
  "primes": ["ku", "wa"]
}
```

This indicates that "kuwa" is composed of two prime roots.

---

## Validation

Before committing changes, verify:

1. **JSON is valid**:
```bash
python3 -m json.tool language-data/syllables.json > /dev/null
```

2. **No duplicate IDs** within a file:
```bash
grep -o '"id": "[^"]*"' your-file.json | sort | uniq -d
```

3. **Referenced IDs exist** (manual check or script)

---

## Getting Help

- **Schema questions**: See `SCHEMA.md`
- **Language questions**: Consult the PDF dictionaries in `resources/`
- **Structure questions**: See main `README.md`

---

## Next Steps

Once comfortable with adding data:
1. Consider contributing batch additions from dictionaries
2. Help expand coverage of less-common verb roots
3. Develop noun categorization schemas
4. Create validation scripts
5. Add example sentences showing usage

---

**Happy data organizing!** Remember: the goal is to make Igbo easier to analyze and work with computationally while respecting its linguistic structure.
