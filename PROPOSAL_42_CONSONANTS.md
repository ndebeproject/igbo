# Proposal: Reaching 42 Consonants

## Current Situation

We have **30 consonant entries**, but the user mentions "42 consonants". The discrepancy is exactly **12 consonants**.

Interestingly, we have exactly **12 consonants that participate in multiple alternation patterns**:

1. **b** (2 patterns)
2. **f** (4 patterns)
3. **gh** (2 patterns)
4. **h** (3 patterns)
5. **l** (2 patterns) - includes the L/R pattern mentioned by user
6. **ṅ** (2 patterns)
7. **r** (4 patterns) - includes the L/R pattern mentioned by user
8. **s** (2 patterns)
9. **sh** (3 patterns)
10. **v** (3 patterns)
11. **w** (2 patterns)
12. **y** (3 patterns)

## Hypothesis: 30 + 12 = 42

One possible interpretation is:
- **30 base consonants** (current entries)
- **+12 additional entries** representing one dialectal variant for each multi-pattern consonant
- **= 42 total consonants**

## Proposed Approach

### Option 1: Add Dialectal Variant Entries

For each of the 12 multi-pattern consonants, add ONE variant entry representing its most common dialectal realization:

Example for L/R:
```json
{
  "letter": "l",
  "variant": "standard",
  "alternates_to": "r",
  ...
}
{
  "letter": "l-dialect-r",
  "base_form": "r",
  "variant": "dialectal",  
  "used_in": ["certain dialects"],
  "notes": "In some dialects, this is realized as 'r' (L/R alternation)"
}
```

This would give us 30 + 12 = 42 entries.

### Option 2: Treat Each Pattern Participation as a Form

Count each consonant once for each alternation pattern:
- l has 2 patterns → 2 entries
- r has 4 patterns → 4 entries
- f has 4 patterns → 4 entries
- etc.

This gives us 50 total, which is too many.

### Option 3: Selective Pattern Counting

Only count the FIRST additional pattern for multi-pattern consonants:
- l (base) + l-in-L/R = 2 entries (not counting N/L/Y separately)
- This gives us 30 + 12 = 42

## Recommended Action

**Before implementing changes**, we need clarification:

1. **Should we add 12 variant entries?**
   - If yes, what should they represent? (dialect-specific forms, allophonic variants, etc.)
   
2. **Which specific variants should be added?**
   - For L/R: add both? or pick one dialect as standard?
   - For F/P: which variant is considered separate?
   - etc.

3. **How should they be structured in the JSON?**
   - As separate top-level consonant entries?
   - As a "variants" array within each consonant entry?
   - With special naming convention (e.g., "l-standard" vs "l-dialectal")?

## Current State Summary

✅ **What we have (30)**:
- 10 non-alternating: ch, d, gb, gw, k, kp, kw, m, m̩, n̩
- 8 single-pattern: g, j, n, nw, ny, p, t, z
- 12 multi-pattern: b, f, gh, h, l, ṅ, r, s, sh, v, w, y

⚠️ **What might be missing (12)**:
- 12 dialectal variant entries for the multi-pattern consonants?
- Or some other set of 12 consonants not currently documented?

## Next Steps

Please clarify:
- What are the 12 missing consonants?
- Should dialectal variants be separate JSON entries?
- Is there a specific list of 42 consonants we should match against?

Once clarified, we can:
1. Update consonants.json with the missing entries
2. Update validation to expect 42 consonants
3. Update documentation to reflect the new counting methodology
