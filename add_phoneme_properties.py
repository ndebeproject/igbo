#!/usr/bin/env python3
"""
Add phonemes, ndebe, and unicode properties to prime verb roots.

For each root, extract the consonant and vowel from the syllable_group
to create the phonemes array.
"""

import json
from pathlib import Path


def load_phonemes():
    """Load all valid vowels and consonants."""
    repo_root = Path(__file__).parent
    
    # Load vowels
    with open(repo_root / 'language-data' / 'vowels.json', 'r', encoding='utf-8') as f:
        vowels_data = json.load(f)
    
    all_vowels = []
    for group in vowels_data['vowelGroups'].values():
        for vowel in group['vowels']:
            all_vowels.append(vowel['letter'])
    
    # Load consonants
    with open(repo_root / 'language-data' / 'consonants.json', 'r', encoding='utf-8') as f:
        consonants_data = json.load(f)
    
    all_consonants = [c['letter'] for c in consonants_data['consonants']]
    
    # Sort consonants by length (longest first) to handle digraphs correctly
    all_consonants.sort(key=len, reverse=True)
    
    return all_consonants, all_vowels


def extract_phonemes_from_plain_name(plain_name, syllable_group, consonants):
    """
    Extract consonant and vowel from plain_name (to preserve tone marks).
    
    The consonant structure is taken from syllable_group, but the vowel
    is extracted from plain_name to preserve tone marks.
    
    Returns: (consonant, vowel_with_tone) tuple
    """
    # Try to find the consonant by matching longest first in syllable_group
    for consonant in consonants:
        if syllable_group.startswith(consonant):
            # Now extract the vowel from plain_name (which has tone marks)
            vowel_with_tone = plain_name[len(consonant):]
            return consonant, vowel_with_tone
    
    # Fallback: if no match found, assume first char is consonant
    # (shouldn't happen with valid data)
    if len(plain_name) > 1:
        return plain_name[0], plain_name[1:]
    
    return plain_name, ""


def add_new_properties(input_file, output_file):
    """Add phonemes, ndebe, and unicode properties to all roots."""
    print(f"Loading {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        roots = json.load(f)
    
    print(f"Found {len(roots)} roots")
    
    # Load phonemes
    consonants, vowels = load_phonemes()
    print(f"Loaded {len(consonants)} consonants and {len(vowels)} vowels")
    
    # Process each root
    updated_roots = []
    for root in roots:
        syllable_group = root['syllable_group']
        plain_name = root['plain_name']
        
        # Extract phonemes from plain_name to preserve tone marks
        consonant, vowel_with_tone = extract_phonemes_from_plain_name(
            plain_name, syllable_group, consonants
        )
        
        # Create updated root with new properties
        updated_root = {
            'id': root['id'],
            'plain_name': root['plain_name'],
            'main_vowel': root['main_vowel'],
            'tone': root['tone'],
            'syllable_group': root['syllable_group'],
            'vowelGroup': root['vowelGroup'],
            'phonemes': [consonant, vowel_with_tone],
            'ndebe': '',
            'unicode': ''
        }
        
        updated_roots.append(updated_root)
    
    print(f"Updated {len(updated_roots)} entries")
    
    # Save to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(updated_roots, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Saved to {output_file}")
    
    return updated_roots


def main():
    """Main function."""
    repo_root = Path(__file__).parent
    input_file = repo_root / 'language-data' / 'verbs' / 'prime-roots' / 'prime-verb-roots.json'
    output_file = repo_root / 'language-data' / 'verbs' / 'prime-roots' / 'prime-verb-roots.json'
    
    print("=" * 70)
    print("Adding Phonemes, Ndebe, and Unicode Properties")
    print("=" * 70)
    print()
    
    updated = add_new_properties(input_file, output_file)
    
    print()
    print("Sample entries:")
    print("-" * 70)
    
    # Show examples
    samples = ['ba', 'ma', 'gba', 'kpị', 'shọ', 'gwa']
    for sample in samples:
        entries = [e for e in updated if e['syllable_group'] == sample]
        if entries:
            print(f"\n{sample}:")
            for e in entries[:1]:  # Just show first tone variant
                print(json.dumps(e, indent=2, ensure_ascii=False))
    
    print()
    print("✓ Done!")


if __name__ == '__main__':
    main()
