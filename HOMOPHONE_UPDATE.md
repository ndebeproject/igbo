# Homophone Handling Update

## New Problem Identified

The initial structure didn't adequately address a critical aspect of Igbo: **homophones and homonyms** where the same syllable with the same tone can have multiple distinct meanings.

### Original Issue
- Structure assumed one meaning per tonal syllable
- Documentation said "Multiple entries can share the same `plain_name` if they have different tones"
- But didn't address: "Multiple entries can share the same `plain_name` AND the same tone"

### Real-World Examples
- `má` (high tone) = "know", "beautiful", "strike", "wipe", etc.
- `gbá` (high tone) = 15+ different meanings (run, flee, shoot, pour, spread, kick, marry, etc.)

## Solution Implemented

### 1. Schema Enhancement

**Added `gloss` field to prime roots**:
```json
{
  "id": "ma_001",
  "plain_name": "ma",
  "syllable_id": "ma_high",
  "vowelGroup": "A",
  "gloss": "know"              // NEW FIELD
}
```

### 2. Multiple Files Per Syllable

File naming convention updated to support homophones:
```
verbs/prime-roots/
├── ma-001.json  (má = know)
├── ma-002.json  (má = beautiful)
├── ma-003.json  (má = strike)
├── gba-001.json (gbá = run)
├── gba-002.json (gbá = flee)
├── gba-003.json (gbá = shoot)
...
├── gba-015.json (gbá = 15th meaning)
```

### 3. Documentation Updates

Updated all documentation to explain homophone handling:

- **README.md**: Added section 4 "Homophones and Homonyms"
- **SCHEMA.md**: Updated prime root schema with `gloss` field and homophone notes
- **USAGE_GUIDE.md**: Added section 1b "Adding Homophones" with detailed examples
- **QUICK_REFERENCE.md**: Added homophone row to key facts table
- **COMPONENT_RELATIONSHIPS.md**: Added "Handling Homophones and Homonyms" section
- **HANDLING_HOMOPHONES.md**: NEW comprehensive guide using "gba" as example

### 4. Example Data

Created concrete examples:
```
ma-001.json: ma_001 (ma_high, gloss: "know")
ma-002.json: ma_002 (ma_high, gloss: "beautiful")
ma-003.json: ma_003 (ma_high, gloss: "strike")
```

### 5. Validation Enhancement

Updated `validate.py` to:
- Check for required `gloss` field in prime roots
- Validate prime root schema automatically
- Report missing fields clearly

## Benefits

### Scalability Solved
- ✅ Can handle roots with 15+ meanings (like "gba")
- ✅ No limit on number of homophones
- ✅ Sequential numbering: gba_001 through gba_999+
- ✅ File organization remains simple

### Clarity Achieved
- Each meaning has its own file and unique ID
- `gloss` field provides immediate semantic distinction
- Easy to find specific meanings
- Clear for both humans and machines

### Maintainability
- Small, focused files
- Changes to one meaning don't affect others
- Easy to add new homophones without restructuring

### Dictionary Compatibility
- Each dictionary entry maps to one file
- Cross-references between dictionaries are straightforward
- Can track provenance (which dictionary provides which meaning)

## File Changes

### Modified Files
1. **language-data/verbs/prime-roots/ma.json** → **ma-001.json**
   - Renamed for consistency
   - Added `gloss: "know"`

2. **SCHEMA.md**
   - Updated prime root schema
   - Added homophone examples
   - Clarified ID conventions

3. **USAGE_GUIDE.md**
   - Added section 1b on homophones
   - Updated examples with gloss field
   - Clarified file naming

4. **README.md**
   - Added section 4 on homophones
   - Explained sequential numbering

5. **QUICK_REFERENCE.md**
   - Added homophone handling notes
   - Updated prime root example

6. **COMPONENT_RELATIONSHIPS.md**
   - Added major section on homophones
   - Included scalability guarantee

7. **validate.py**
   - Added gloss field requirement
   - Added prime root schema validation

### New Files
1. **language-data/verbs/prime-roots/ma-002.json**
   - Example: má = beautiful

2. **language-data/verbs/prime-roots/ma-003.json**
   - Example: má = strike

3. **HANDLING_HOMOPHONES.md**
   - Comprehensive guide
   - "gba" example with 15+ meanings
   - File organization best practices

## Validation Results

All 16 JSON files validated successfully ✓
- 3 prime root files (ma-001, ma-002, ma-003)
- All with required `gloss` field
- Schema compliance verified

## Design Pattern

```
Single Syllable Definition
    ↓
Multiple Root Entries (Homophones)
    ↓
Unique IDs for Each Meaning
    ↓
Used Independently in Verb Forms
```

Example:
```
ma_high (syllable)
  ├─→ ma_001 (know)    → verb forms for "knowing"
  ├─→ ma_002 (beautiful) → verb forms for "being beautiful"
  └─→ ma_003 (strike)   → verb forms for "striking"
```

## Backward Compatibility

- Existing structure preserved
- New field added (gloss)
- File renaming (ma.json → ma-001.json) maintains convention
- All existing references still work

## Forward Compatibility

The structure now supports:
- Unlimited homophones per syllable
- Easy addition of new meanings
- Clear semantic distinctions
- Scalable to thousands of entries

## Next Steps for Data Entry

When adding verb roots:
1. Check if syllable exists
2. Check highest existing number for that root (e.g., ma-003.json)
3. Create next file (e.g., ma-004.json)
4. Include required gloss field
5. Validate with `python3 validate.py`

## Conclusion

The homophone handling issue is **fully resolved**. The structure can now:
- ✅ Handle multiple meanings per syllable+tone
- ✅ Scale to roots with 15+ meanings
- ✅ Maintain clarity and organization
- ✅ Support systematic data entry
- ✅ Validate automatically

The repository is ready for bulk data entry without scalability concerns.
