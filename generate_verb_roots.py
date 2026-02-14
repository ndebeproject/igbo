#!/usr/bin/env python3
"""
Generate all possible monosyllabic verb roots and their infinitives.

This script generates:
1. All monosyllabic verb roots (consonant + vowel combinations)
2. Dialectal variations (e.g., L/R alternations like la/ra, le/re)
3. Infinitives for all verb roots following vowel harmony rules:
   - A-group vowels (a, ẹ, ị, ọ, ụ) → prefix 'ị'
   - E-group vowels (e, i, o, u) → prefix 'i'
"""

import json
from pathlib import Path
from collections import defaultdict


def load_vowels(language_data_dir):
    """Load vowels from vowels.json and return grouped by A/E groups."""
    vowels_file = language_data_dir / 'vowels.json'
    with open(vowels_file, 'r', encoding='utf-8') as f:
        vowels_data = json.load(f)
    
    a_group = [v['letter'] for v in vowels_data['vowelGroups']['A']['vowels']]
    e_group = [v['letter'] for v in vowels_data['vowelGroups']['E']['vowels']]
    
    return a_group, e_group


def load_consonants(language_data_dir):
    """Load consonants and their dialectal alternations from consonants.json."""
    consonants_file = language_data_dir / 'consonants.json'
    with open(consonants_file, 'r', encoding='utf-8') as f:
        consonants_data = json.load(f)
    
    # Get all consonants
    consonants = []
    alternations = defaultdict(list)
    
    for c in consonants_data['consonants']:
        letter = c['letter']
        consonants.append(letter)
        
        # Track dialectal alternations
        if c.get('shifting', False) and 'alternation_sets' in c:
            for alt_set in c['alternation_sets']:
                pattern = alt_set['pattern']
                alternates_with = alt_set.get('alternates_with', [])
                
                # Create bidirectional mapping for major patterns
                # We focus on the most common dialectal variations
                if pattern in ['L/R', 'B/V', 'G/V', 'F/P', 'J/Z', 'S/T', 'Y/H']:
                    for alt in alternates_with:
                        if alt in [x['letter'] for x in consonants_data['consonants']]:
                            # Store the relationship
                            key = tuple(sorted([letter, alt]))
                            if letter not in alternations[alt]:
                                alternations[letter].append(alt)
                            if alt not in alternations[letter]:
                                alternations[alt].append(letter)
    
    return consonants, alternations


def get_vowel_group(vowel, a_group, e_group):
    """Determine which vowel group a vowel belongs to."""
    if vowel in a_group:
        return 'A'
    elif vowel in e_group:
        return 'E'
    else:
        return None


def get_infinitive_prefix(vowel_group):
    """Get the appropriate infinitive prefix based on vowel group."""
    if vowel_group == 'A':
        return 'ị'
    elif vowel_group == 'E':
        return 'i'
    else:
        return None


def generate_verb_roots(consonants, vowels, a_group, e_group):
    """Generate all monosyllabic verb roots (CV combinations)."""
    verb_roots = []
    
    for consonant in consonants:
        for vowel in vowels:
            root = consonant + vowel
            vowel_group = get_vowel_group(vowel, a_group, e_group)
            
            verb_roots.append({
                'root': root,
                'consonant': consonant,
                'vowel': vowel,
                'vowel_group': vowel_group
            })
    
    return verb_roots


def generate_dialectal_variations(verb_roots, alternations):
    """Generate dialectal variations for verb roots."""
    dialectal_roots = []
    seen = set()  # Track unique pairs to avoid duplicates
    
    for root_info in verb_roots:
        consonant = root_info['consonant']
        vowel = root_info['vowel']
        
        # Check if this consonant has dialectal alternations
        if consonant in alternations:
            for alt_consonant in alternations[consonant]:
                alt_root = alt_consonant + vowel
                
                # Create a unique key for this pair (order-independent)
                # Sort the roots to ensure we only create one entry per pair
                pair_key = tuple(sorted([root_info['root'], alt_root]))
                
                if pair_key not in seen:
                    seen.add(pair_key)
                    dialectal_roots.append({
                        'root': f"{root_info['root']} / {alt_root}",
                        'base_root': root_info['root'],
                        'dialectal_root': alt_root,
                        'base_consonant': consonant,
                        'dialectal_consonant': alt_consonant,
                        'vowel': vowel,
                        'vowel_group': root_info['vowel_group']
                    })
    
    return dialectal_roots


def generate_infinitives(verb_roots, a_group, e_group):
    """Generate infinitives for all verb roots."""
    infinitives = []
    
    for root_info in verb_roots:
        root = root_info['root']
        vowel_group = root_info['vowel_group']
        prefix = get_infinitive_prefix(vowel_group)
        
        if prefix:
            infinitive = prefix + root
            infinitives.append({
                'infinitive': infinitive,
                'root': root,
                'prefix': prefix,
                'vowel_group': vowel_group
            })
    
    return infinitives


def generate_dialectal_infinitives(dialectal_roots, a_group, e_group):
    """Generate infinitives for dialectal variations."""
    infinitives = []
    
    for root_info in dialectal_roots:
        base_root = root_info['base_root']
        dialectal_root = root_info['dialectal_root']
        vowel_group = root_info['vowel_group']
        prefix = get_infinitive_prefix(vowel_group)
        
        if prefix:
            base_infinitive = prefix + base_root
            dialectal_infinitive = prefix + dialectal_root
            combined_infinitive = f"{base_infinitive} / {dialectal_infinitive}"
            
            infinitives.append({
                'infinitive': combined_infinitive,
                'base_infinitive': base_infinitive,
                'dialectal_infinitive': dialectal_infinitive,
                'base_root': base_root,
                'dialectal_root': dialectal_root,
                'prefix': prefix,
                'vowel_group': vowel_group
            })
    
    return infinitives


def save_to_file(data, output_file, header):
    """Save data to a text file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {header}\n")
        f.write(f"# Total entries: {len(data)}\n\n")
        
        for item in data:
            if isinstance(item, dict):
                # Format the output nicely
                # Check for infinitive first since infinitives also have 'root' field
                if 'infinitive' in item:
                    f.write(f"{item['infinitive']}\n")
                elif 'root' in item and 'vowel_group' in item:
                    f.write(f"{item['root']}\n")
            else:
                f.write(f"{item}\n")


def main():
    """Main generation function."""
    # Setup paths
    repo_root = Path(__file__).parent
    language_data_dir = repo_root / 'language-data'
    output_dir = repo_root / 'generated'
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 70)
    print("Igbo Monosyllabic Verb Root and Infinitive Generator")
    print("=" * 70)
    print()
    
    # Load vowels and consonants
    print("Loading vowels and consonants...")
    a_group, e_group = load_vowels(language_data_dir)
    all_vowels = a_group + e_group
    consonants, alternations = load_consonants(language_data_dir)
    
    print(f"  A-group vowels: {', '.join(a_group)}")
    print(f"  E-group vowels: {', '.join(e_group)}")
    print(f"  Total vowels: {len(all_vowels)}")
    print(f"  Total consonants: {len(consonants)}")
    print()
    
    # Generate all monosyllabic verb roots
    print("Generating monosyllabic verb roots...")
    verb_roots = generate_verb_roots(consonants, all_vowels, a_group, e_group)
    print(f"  Generated {len(verb_roots)} base verb roots")
    
    # Generate dialectal variations
    print("Generating dialectal variations...")
    dialectal_roots = generate_dialectal_variations(verb_roots, alternations)
    print(f"  Generated {len(dialectal_roots)} dialectal variations")
    
    # Generate infinitives
    print("Generating infinitives for base roots...")
    base_infinitives = generate_infinitives(verb_roots, a_group, e_group)
    print(f"  Generated {len(base_infinitives)} base infinitives")
    
    print("Generating infinitives for dialectal variations...")
    dialectal_infinitives = generate_dialectal_infinitives(dialectal_roots, a_group, e_group)
    print(f"  Generated {len(dialectal_infinitives)} dialectal infinitives")
    print()
    
    # Save outputs
    print("Saving generated data...")
    
    # Save base verb roots
    save_to_file(
        verb_roots,
        output_dir / 'monosyllabic_verb_roots.txt',
        'Monosyllabic Verb Roots (Consonant + Vowel)'
    )
    print(f"  ✓ Saved monosyllabic_verb_roots.txt")
    
    # Save dialectal verb roots
    save_to_file(
        dialectal_roots,
        output_dir / 'dialectal_verb_roots.txt',
        'Dialectal Variations of Monosyllabic Verb Roots'
    )
    print(f"  ✓ Saved dialectal_verb_roots.txt")
    
    # Save base infinitives
    save_to_file(
        base_infinitives,
        output_dir / 'infinitives.txt',
        'Infinitives of Monosyllabic Verb Roots'
    )
    print(f"  ✓ Saved infinitives.txt")
    
    # Save dialectal infinitives
    save_to_file(
        dialectal_infinitives,
        output_dir / 'dialectal_infinitives.txt',
        'Infinitives with Dialectal Variations'
    )
    print(f"  ✓ Saved dialectal_infinitives.txt")
    
    # Print summary
    print()
    print("=" * 70)
    print("Generation Summary")
    print("=" * 70)
    print(f"Base verb roots: {len(verb_roots)}")
    print(f"Dialectal variations: {len(dialectal_roots)}")
    print(f"Base infinitives: {len(base_infinitives)}")
    print(f"Dialectal infinitives: {len(dialectal_infinitives)}")
    print()
    print(f"All files saved to: {output_dir}")
    print()
    
    # Show some examples
    print("Examples:")
    print("-" * 70)
    print("\nBase Verb Roots (first 10):")
    for root in verb_roots[:10]:
        print(f"  {root['root']} (vowel group: {root['vowel_group']})")
    
    print("\nDialectal Variations (first 5):")
    for root in dialectal_roots[:5]:
        print(f"  {root['root']} (vowel group: {root['vowel_group']})")
    
    print("\nBase Infinitives (first 10):")
    for inf in base_infinitives[:10]:
        print(f"  {inf['infinitive']} (from {inf['root']}, vowel group: {inf['vowel_group']})")
    
    print("\nDialectal Infinitives (first 5):")
    for inf in dialectal_infinitives[:5]:
        print(f"  {inf['infinitive']} (vowel group: {inf['vowel_group']})")
    
    print()
    print("✓ Generation complete!")


if __name__ == '__main__':
    main()
