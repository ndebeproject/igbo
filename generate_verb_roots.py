#!/usr/bin/env python3
"""
Generate all possible monosyllabic verb roots and their infinitives in JSON format.

This script generates:
1. All monosyllabic verb roots (consonant + vowel combinations)
2. Dialectal variations (e.g., L/R alternations like la/ra, le/re)
3. Infinitives for all verb roots following vowel harmony rules:
   - A-group vowels (a, ẹ, ị, ọ, ụ) → prefix 'ị'
   - E-group vowels (e, i, o, u) → prefix 'i'

Output format: JSON files following the repository schema conventions.
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
                            # Store the bidirectional relationship
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
    """Generate all monosyllabic verb roots (CV combinations) with tone variants."""
    from expand_tone_variants import find_main_vowel, apply_tone_to_syllable
    
    verb_roots = []
    
    for consonant in consonants:
        for vowel in vowels:
            syllable_group = consonant + vowel
            vowel_group = get_vowel_group(vowel, a_group, e_group)
            main_vowel = find_main_vowel(syllable_group)
            
            # Create three tone variants for each syllable
            for idx, tone in enumerate(['high', 'mid', 'low'], start=1):
                plain_name_with_tone = apply_tone_to_syllable(syllable_group, tone)
                
                verb_roots.append({
                    'syllable_group': syllable_group,
                    'plain_name': plain_name_with_tone,
                    'main_vowel': main_vowel if main_vowel else vowel,
                    'tone': tone,
                    'vowelGroup': vowel_group,
                    'consonant': consonant,  # Temp field for generation
                    'vowel': vowel  # Temp field for generation
                })
    
    return verb_roots


def generate_dialectal_variations(verb_roots, alternations):
    """Generate dialectal variations for verb roots as JSON objects."""
    dialectal_roots = []
    seen = set()  # Track unique pairs to avoid duplicates
    
    for root_info in verb_roots:
        consonant = root_info['consonant']
        vowel = root_info['vowel']
        plain_name = root_info['plain_name']
        vowel_group = root_info['vowelGroup']
        
        # Check if this consonant has dialectal alternations
        if consonant in alternations:
            for alt_consonant in alternations[consonant]:
                alt_root = alt_consonant + vowel
                
                # Create a unique key for this pair (order-independent)
                pair_key = tuple(sorted([plain_name, alt_root]))
                
                if pair_key not in seen:
                    seen.add(pair_key)
                    dialectal_roots.append({
                        'id': f"{plain_name}_{alt_root}_dialectal",
                        'base_form': plain_name,
                        'dialectal_form': alt_root,
                        'combined_form': f"{plain_name} / {alt_root}",
                        'base_consonant': consonant,
                        'dialectal_consonant': alt_consonant,
                        'vowel': vowel,
                        'vowelGroup': vowel_group,
                        'syllable_id': f"{plain_name}_mid",  # Base form syllable
                        'dialectal_syllable_id': f"{alt_root}_mid",
                        'generated': True,
                        'type': 'dialectal_variation'
                    })
    
    return dialectal_roots


def generate_infinitives(verb_roots, a_group, e_group):
    """Generate infinitives for all verb roots as JSON objects."""
    infinitives = []
    
    for root_info in verb_roots:
        plain_name = root_info['plain_name']
        vowel_group = root_info['vowelGroup']
        prefix = get_infinitive_prefix(vowel_group)
        
        if prefix:
            infinitive = prefix + plain_name
            infinitives.append({
                'id': f"{infinitive}_infinitive",
                'infinitive_form': infinitive,
                'base_root': plain_name,
                'prefix': prefix,
                'vowelGroup': vowel_group,
                'syllable_id': f"{infinitive}_mid",  # Infinitive syllable
                'type': 'infinitive'
            })
    
    return infinitives


def generate_dialectal_infinitives(dialectal_roots, a_group, e_group):
    """Generate infinitives for dialectal variations as JSON objects."""
    infinitives = []
    
    for root_info in dialectal_roots:
        base_root = root_info['base_form']
        dialectal_root = root_info['dialectal_form']
        vowel_group = root_info['vowelGroup']
        prefix = get_infinitive_prefix(vowel_group)
        
        if prefix:
            base_infinitive = prefix + base_root
            dialectal_infinitive = prefix + dialectal_root
            combined_infinitive = f"{base_infinitive} / {dialectal_infinitive}"
            
            infinitives.append({
                'id': f"{base_infinitive}_{dialectal_infinitive}_dialectal_inf",
                'infinitive_form': combined_infinitive,
                'base_infinitive': base_infinitive,
                'dialectal_infinitive': dialectal_infinitive,
                'base_root': base_root,
                'dialectal_root': dialectal_root,
                'prefix': prefix,
                'vowelGroup': vowel_group,
                'syllable_id': f"{base_infinitive}_mid",
                'dialectal_syllable_id': f"{dialectal_infinitive}_mid",
                'type': 'dialectal_infinitive'
            })
    
    return infinitives


def save_to_json(data, output_file, metadata=None):
    """Save data to a JSON file following repository conventions."""
    output = {
        'metadata': metadata or {},
        'entries': data
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)


def save_array_to_json(data, output_file):
    """Save data as a JSON array (like syllables.json)."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_existing_prime_roots(prime_roots_file):
    """Load existing prime roots from prime-verb-roots.json."""
    if not prime_roots_file.exists():
        return []
    
    with open(prime_roots_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def merge_and_assign_ids(existing_roots, new_roots):
    """
    Merge existing and new roots, assigning sequential IDs.
    
    - Existing roots keep their IDs and data
    - New roots only added if syllable_group + tone doesn't exist
    - All roots get sequential IDs per syllable_group
    """
    from collections import defaultdict
    
    roots_by_group = defaultdict(list)
    
    # Add existing roots first (they have priority)
    for root in existing_roots:
        syllable_group = root.get('syllable_group', root.get('plain_name', ''))
        roots_by_group[syllable_group].append(root)
    
    # Add new generated roots only if syllable_group + tone doesn't exist
    for root in new_roots:
        syllable_group = root['syllable_group']
        tone = root['tone']
        consonant = root['consonant']
        plain_name = root['plain_name']
        
        # Extract vowel with tone marks from plain_name
        vowel_with_tone = plain_name[len(consonant):]
        
        # Check if this tone variant already exists for this syllable_group
        existing_tones = [r.get('tone') for r in roots_by_group[syllable_group]]
        
        if tone not in existing_tones:
            # Create clean root without temp fields
            clean_root = {
                'plain_name': root['plain_name'],
                'main_vowel': root['main_vowel'],
                'tone': root['tone'],
                'syllable_group': root['syllable_group'],
                'vowelGroup': root['vowelGroup'],
                'phonemes': [consonant, vowel_with_tone],
                'ndebe': '',
                'unicode': ''
            }
            roots_by_group[syllable_group].append(clean_root)
    
    # Assign sequential IDs per syllable_group, ordered by tone
    all_roots = []
    tone_order = {'high': 1, 'mid': 2, 'low': 3}
    
    for syllable_group in sorted(roots_by_group.keys()):
        entries = roots_by_group[syllable_group]
        # Sort by tone
        entries.sort(key=lambda x: tone_order.get(x.get('tone', 'mid'), 2))
        
        for idx, root in enumerate(entries, start=1):
            root['id'] = f"syl_{syllable_group}_{idx:03d}"
            all_roots.append(root)
    
    return all_roots


def save_prime_root_to_file(root_data, prime_roots_dir):
    """Save a single prime root as an individual JSON file."""
    plain_name = root_data['plain_name']
    filename = f"{plain_name}-generated.json"
    filepath = prime_roots_dir / filename
    
    # Create a clean version without extra metadata fields for the file
    clean_data = {
        'id': root_data['id'],
        'plain_name': root_data['plain_name'],
        'syllable_id': root_data['syllable_id'],
        'vowelGroup': root_data['vowelGroup'],
        'gloss': root_data['gloss']
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(clean_data, f, ensure_ascii=False, indent=2)
    
    return filepath


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
    
    # Save outputs to JSON
    print("Saving generated data to JSON...")
    
    # Create output directories
    verbs_dir = language_data_dir / 'verbs'
    prime_roots_dir = verbs_dir / 'prime-roots'
    
    # Load existing prime roots and merge with new ones
    prime_roots_file = prime_roots_dir / 'prime-verb-roots.json'
    print(f"Loading existing prime roots from {prime_roots_file.name}...")
    existing_roots = load_existing_prime_roots(prime_roots_file)
    print(f"  Found {len(existing_roots)} existing roots")
    
    print("Merging and assigning sequential IDs...")
    all_prime_roots = merge_and_assign_ids(existing_roots, verb_roots)
    print(f"  Total prime roots after merge: {len(all_prime_roots)}")
    
    # Save consolidated prime roots
    save_array_to_json(all_prime_roots, prime_roots_file)
    print(f"  ✓ Saved prime-verb-roots.json ({len(all_prime_roots)} prime roots)")
    
    # Save dialectal verb roots as a collection (they reference prime roots)
    save_array_to_json(
        dialectal_roots,
        verbs_dir / 'generated-dialectal-roots.json'
    )
    print(f"  ✓ Saved generated-dialectal-roots.json ({len(dialectal_roots)} entries)")
    
    # Save base infinitives as a collection (they are derived forms, not prime roots)
    save_array_to_json(
        base_infinitives,
        verbs_dir / 'generated-infinitives.json'
    )
    print(f"  ✓ Saved generated-infinitives.json ({len(base_infinitives)} entries)")
    
    # Save dialectal infinitives
    save_array_to_json(
        dialectal_infinitives,
        verbs_dir / 'generated-dialectal-infinitives.json'
    )
    print(f"  ✓ Saved generated-dialectal-infinitives.json ({len(dialectal_infinitives)} entries)")
    
    # Print summary
    print()
    print("=" * 70)
    print("Generation Summary")
    print("=" * 70)
    print(f"Prime roots (monosyllabic): {len(all_prime_roots)} in prime-verb-roots.json")
    print(f"Dialectal variations: {len(dialectal_roots)} (collection file)")
    print(f"Base infinitives: {len(base_infinitives)} (collection file)")
    print(f"Dialectal infinitives: {len(dialectal_infinitives)} (collection file)")
    print()
    print(f"Files saved in:")
    print(f"  - Prime roots: {prime_roots_file}")
    print(f"  - Collections: {verbs_dir}/generated-*.json")
    print()
    
    # Show some examples
    print("Examples:")
    print("-" * 70)
    print("\nPrime Roots (first 10 from prime-verb-roots.json):")
    for root in all_prime_roots[:10]:
        print(f"  {root['plain_name']} → ID: {root['id']}, vowel group: {root['vowelGroup']}")
    
    print("\nDialectal Variations (first 5):")
    for root in dialectal_roots[:5]:
        print(f"  {root['combined_form']} (vowel group: {root['vowelGroup']})")
    
    print("\nBase Infinitives (first 10):")
    for inf in base_infinitives[:10]:
        print(f"  {inf['infinitive_form']} (from {inf['base_root']}, vowel group: {inf['vowelGroup']})")
    
    print("\nDialectal Infinitives (first 5):")
    for inf in dialectal_infinitives[:5]:
        print(f"  {inf['infinitive_form']} (vowel group: {inf['vowelGroup']})")
    
    print()
    print("✓ Generation complete!")
    print()
    print("Note: All prime roots saved in prime-verb-roots.json with sequential IDs.")
    print("Infinitives and dialectal variations saved as separate collection files.")


if __name__ == '__main__':
    main()
