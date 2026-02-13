# Handling Homophones: The "gba" Example

This document demonstrates how the repository structure handles verb roots with many meanings using "gba" as an example.

## The Challenge

The verb root "gba" (with high tone) has approximately 15+ different meanings in Igbo, including:
1. run
2. flee
3. shoot (a gun)
4. pour
5. spread
6. kick
7. marry (a woman)
8. pack/gather
9. encompass
10. escape
11. borrow
12. lend
13. make a bet
14. guess
15. encircle
... and more

All of these share:
- Same phonetic form: "gba"
- Same tone: high (gbá)
- Same syllable structure

But they are **distinct words** with different meanings.

## The Solution

### Step 1: Define the Syllable (Once)

```json
// In syllables.json (add if not exists)
{
  "id": "gba_high",
  "tone": "high",
  "phonemes": ["gb", "a"],
  "ndebe": ""
}
```

### Step 2: Create Individual Prime Root Files

Each meaning gets its own file with a unique ID:

```json
// verbs/prime-roots/gba-001.json
{
  "id": "gba_001",
  "plain_name": "gba",
  "syllable_id": "gba_high",
  "vowelGroup": "A",
  "gloss": "run"
}

// verbs/prime-roots/gba-002.json
{
  "id": "gba_002",
  "plain_name": "gba",
  "syllable_id": "gba_high",
  "vowelGroup": "A",
  "gloss": "flee"
}

// verbs/prime-roots/gba-003.json
{
  "id": "gba_003",
  "plain_name": "gba",
  "syllable_id": "gba_high",
  "vowelGroup": "A",
  "gloss": "shoot"
}

// verbs/prime-roots/gba-004.json
{
  "id": "gba_004",
  "plain_name": "gba",
  "syllable_id": "gba_high",
  "vowelGroup": "A",
  "gloss": "pour"
}

// ... continue through gba-015.json and beyond
```

### Step 3: Use in Verb Forms

Each root can then be used independently in verb forms:

```json
// verbs/verb-forms/gba-001-present.json (run)
{
  "id": "gba_001_na_simplePresent",
  "primeRoot": "gba_001",
  "auxiliary": null,
  "prefix": null,
  "suffixes": [],
  "particles": ["particle_na"],
  "meaning": {
    "id": "meaning_gba_001",
    "description": "running"
  },
  "tense": "simplePresent"
}

// verbs/verb-forms/gba-003-present.json (shoot)
{
  "id": "gba_003_na_simplePresent",
  "primeRoot": "gba_003",
  "auxiliary": null,
  "prefix": null,
  "suffixes": [],
  "particles": ["particle_na"],
  "meaning": {
    "id": "meaning_gba_003",
    "description": "shooting"
  },
  "tense": "simplePresent"
}
```

## File Organization

```
verbs/prime-roots/
├── gba-001.json    (run)
├── gba-002.json    (flee)
├── gba-003.json    (shoot)
├── gba-004.json    (pour)
├── gba-005.json    (spread)
├── gba-006.json    (kick)
├── gba-007.json    (marry)
├── gba-008.json    (pack/gather)
├── gba-009.json    (encompass)
├── gba-010.json    (escape)
├── gba-011.json    (borrow)
├── gba-012.json    (lend)
├── gba-013.json    (bet)
├── gba-014.json    (guess)
├── gba-015.json    (encircle)
└── gba-016.json    (additional meanings as discovered)
```

## Benefits of This Approach

### 1. Clarity
Each meaning has its own file and unique ID, making it easy to:
- Find specific meanings
- Reference in verb forms
- Document usage patterns

### 2. Scalability
- No limit on number of homophones
- Can add `gba_016`, `gba_017`, etc. as needed
- No restructuring required as data grows

### 3. Maintainability
- Each file is small and focused
- Changes to one meaning don't affect others
- Easy to add examples and notes per meaning

### 4. Machine Readability
- Clear semantic distinction via `gloss` field
- Unique IDs for programmatic reference
- Structured data for NLP applications

### 5. Dictionary Compatibility
When extracting from dictionaries:
- Each dictionary entry → one file
- Cross-reference between dictionaries easy
- Can track which dictionary provides which meaning

## Finding Roots

To see all meanings of "gba":
```bash
ls language-data/verbs/prime-roots/gba-*.json
```

To search for a specific meaning:
```bash
grep -l '"gloss": "run"' language-data/verbs/prime-roots/gba-*.json
```

## Adding New Homophones

When you find a new meaning for "gba":

1. Check the highest existing number:
   ```bash
   ls language-data/verbs/prime-roots/gba-*.json | tail -1
   # Shows: gba-015.json
   ```

2. Create the next file:
   ```bash
   # Create gba-016.json with the new meaning
   ```

3. Validate:
   ```bash
   python3 validate.py
   ```

## Comparison with Other Approaches

### ❌ Single File with Array
```json
// verbs/prime-roots/gba.json
{
  "roots": [
    {"id": "gba_001", "gloss": "run"},
    {"id": "gba_002", "gloss": "flee"},
    // ... 13 more entries
  ]
}
```
**Problems**: 
- Large files become unwieldy
- Harder to navigate
- Merge conflicts more likely

### ❌ Meaning IDs in File Name
```
gba-run.json, gba-flee.json, gba-shoot.json
```
**Problems**:
- English glosses in file names
- Harder to maintain consistent numbering
- Difficult for non-English speakers

### ✅ Current Approach (Sequential Numbers)
```
gba-001.json, gba-002.json, gba-003.json
```
**Benefits**:
- Language-neutral file names
- Clear ordering
- Easy to reference
- Scalable

## Summary

The repository structure handles homophones elegantly:
- **One syllable** (gba_high) → **many roots** (gba_001 through gba_015+)
- **Gloss field** distinguishes meanings
- **Sequential IDs** ensure scalability
- **One file per meaning** keeps organization clean

This design accommodates the reality of Igbo language where roots like "gba" can have 15+ meanings without any structural limitations or complications.
