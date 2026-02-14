#!/usr/bin/env python3
"""
Expand prime roots to include tone variants (high, mid, low).

For each syllable, create three entries with different tones.
Apply tone marks to vowels where applicable.
"""

import json
from pathlib import Path


# Tone marking for Igbo vowels
VOWEL_TONES = {
    'a': {'high': 'á', 'mid': 'a', 'low': 'à'},
    'e': {'high': 'é', 'mid': 'e', 'low': 'è'},
    'i': {'high': 'í', 'mid': 'i', 'low': 'ì'},
    'o': {'high': 'ó', 'mid': 'o', 'low': 'ò'},
    'u': {'high': 'ú', 'mid': 'u', 'low': 'ù'},
    'ẹ': {'high': 'ẹ́', 'mid': 'ẹ', 'low': 'ẹ̀'},
    'ị': {'high': 'ị́', 'mid': 'ị', 'low': 'ị̀'},
    'ọ': {'high': 'ọ́', 'mid': 'ọ', 'low': 'ọ̀'},
    'ụ': {'high': 'ụ́', 'mid': 'ụ', 'low': 'ụ̀'},
}


def find_main_vowel(syllable):
    """Find the main vowel in a syllable."""
    for char in syllable:
        if char in VOWEL_TONES:
            return char
    return None


def apply_tone_to_syllable(syllable, tone):
    """Apply tone marking to a syllable."""
    main_vowel = find_main_vowel(syllable)
    
    if not main_vowel:
        # No recognizable vowel, return as-is
        return syllable
    
    if main_vowel not in VOWEL_TONES:
        # Vowel doesn't have tone variants, return as-is
        return syllable
    
    # Get the toned vowel
    toned_vowel = VOWEL_TONES[main_vowel][tone]
    
    # Replace the vowel in the syllable
    result = syllable.replace(main_vowel, toned_vowel, 1)
    return result


def expand_root_with_tones(root):
    """Expand a single root into three tone variants."""
    syllable_group = root['plain_name']
    vowel_group = root['vowelGroup']
    main_vowel = find_main_vowel(syllable_group)
    
    variants = []
    
    for idx, tone in enumerate(['high', 'mid', 'low'], start=1):
        plain_name_with_tone = apply_tone_to_syllable(syllable_group, tone)
        
        variant = {
            'id': f"syl_{syllable_group}_{idx:03d}",
            'plain_name': plain_name_with_tone,
            'main_vowel': main_vowel if main_vowel else syllable_group[-1],
            'tone': tone,
            'syllable_group': syllable_group,
            'vowelGroup': vowel_group
        }
        variants.append(variant)
    
    return variants


def expand_all_roots(input_file, output_file):
    """Expand all prime roots with tone variants."""
    print(f"Loading {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        roots = json.load(f)
    
    print(f"Found {len(roots)} roots")
    
    # Group by syllable to avoid duplicates
    syllables_seen = {}
    for root in roots:
        syllable = root['plain_name']
        if syllable not in syllables_seen:
            syllables_seen[syllable] = root
    
    print(f"Unique syllables: {len(syllables_seen)}")
    
    # Expand each unique syllable
    expanded_roots = []
    for syllable, root in sorted(syllables_seen.items()):
        variants = expand_root_with_tones(root)
        expanded_roots.extend(variants)
    
    print(f"Expanded to {len(expanded_roots)} entries (with tone variants)")
    
    # Save to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(expanded_roots, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Saved to {output_file}")
    
    return expanded_roots


def main():
    """Main function."""
    repo_root = Path(__file__).parent
    input_file = repo_root / 'language-data' / 'verbs' / 'prime-roots' / 'prime-verb-roots.json'
    output_file = repo_root / 'language-data' / 'verbs' / 'prime-roots' / 'prime-verb-roots.json'
    
    print("=" * 70)
    print("Expanding Prime Roots with Tone Variants")
    print("=" * 70)
    print()
    
    expanded = expand_all_roots(input_file, output_file)
    
    print()
    print("Sample entries:")
    print("-" * 70)
    
    # Show examples for 'ma' syllable
    ma_entries = [e for e in expanded if e['syllable_group'] == 'ma']
    for entry in ma_entries:
        print(json.dumps(entry, indent=2, ensure_ascii=False))
    
    print()
    print("Sample entries for 'ba' syllable:")
    ba_entries = [e for e in expanded if e['syllable_group'] == 'ba']
    for entry in ba_entries:
        print(json.dumps(entry, indent=2, ensure_ascii=False))
    
    print()
    print("✓ Done!")


if __name__ == '__main__':
    main()
