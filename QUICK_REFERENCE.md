# Quick Reference Guide

## Directory Structure at a Glance

```
language-data/
├── syllables.json              # All syllables with 3 tones each
├── verbs/
│   ├── prime-roots/            # Monosyllabic verb roots (ba.json, ma.json, etc.)
│   ├── derived-roots/          # Compound roots (kuwa.json, etc.)
│   ├── auxiliaries/            # Auxiliary verbs (ama.json, etc.)
│   ├── prefixes/               # Verbal prefixes (a.json, e.json, o.json, i.json)
│   ├── suffixes/               # Verbal suffixes (ro_dot.json, etc.)
│   ├── particles/              # Grammatical particles (na.json, etc.)
│   ├── verb-forms/             # Complete inflected forms
│   └── tenses.json             # Tense definitions
└── nouns/
    ├── basic.json              # Basic nouns
    └── verbal_nouns.json       # Deverbal nouns
```

## Common Tasks

### Validate All Data
```bash
python3 validate.py
```

### Add a New Verb Root
1. Add syllable(s) to `syllables.json` (if missing)
2. Create `verbs/prime-roots/{root}.json`
3. Create verb forms in `verbs/verb-forms/`

### Add a Prefix or Suffix
1. For prefix: Add to `verbs/prefixes/{prefix}.json`
2. For suffix: Add to `verbs/suffixes/{suffix}.json`

### Check JSON Validity
```bash
python3 -m json.tool your-file.json
```

## Key Facts About Igbo

| Feature | Description |
|---------|-------------|
| **Tones** | 3 tones: high (á), mid (a), low (à) |
| **Verb Roots** | Mostly monosyllabic (ma, ba, ku, etc.) |
| **Word Type** | Heavily verbal language |
| **Prefixes** | e, o, a, i (nominalization) |
| **Suffixes** | go, la, ba, rọ (tense/aspect) |

## Tone Diacritics

| Tone | Mark | Example |
|------|------|---------|
| High | á é í ó ú | má |
| Mid | a e i o u | ma |
| Low | à è ì ò ù | mà |

## Schema Quick Reference

### Syllable
```json
{
  "id": "ma_high",
  "tone": "high",
  "phonemes": ["m", "a"],
  "ndebe": ""
}
```

### Prime Root
```json
{
  "id": "ma_001",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A"
}
```

### Prefix
```json
{
  "id": "prefix_a",
  "name": "a",
  "function": "nominalization",
  "syllable_id": "a_high"
}
```

### Suffix
```json
{
  "id": "suffix_rọ",
  "name": "rọ",
  "function": "continuous_aspect"
}
```

### Verb Form
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

## ID Naming Patterns

| Type | Pattern | Example |
|------|---------|---------|
| Syllable | `{syllable}_{tone}` | `ma_high` |
| Prime Root | `{root}_{number}` | `ma_001` |
| Prefix | `prefix_{name}` | `prefix_a` |
| Suffix | `suffix_{name}` | `suffix_rọ` |
| Particle | `particle_{name}` | `particle_na` |
| Auxiliary | `{aux}_{number}` | `ama_001` |

## Resources

- **Full Documentation**: See `README.md`
- **Schema Details**: See `SCHEMA.md`
- **Usage Examples**: See `USAGE_GUIDE.md`
- **Contributing**: See `CONTRIBUTING.md`
- **Dictionaries**: See `resources/` directory

## Getting Help

1. Check the documentation files above
2. Open an issue on GitHub
3. Review the reference dictionaries in `resources/`

---

**Remember**: 
- Always specify tone
- Use IDs to link components
- Validate before committing
- One component per file (for most categories)
