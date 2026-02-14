#!/usr/bin/env python3
"""
Consolidate all prime roots (manual and generated) into a single file.
- Merge manual prime root files with generated prime roots
- Assign sequential IDs per root following pattern: root_001, root_002, etc.
- Remove "generated" property
- Save to prime-verb-roots.json
"""

import json
from pathlib import Path
from collections import defaultdict

def load_manual_prime_roots(prime_roots_dir):
    """Load individual manual prime root JSON files."""
    manual_roots = []
    
    # Known manual files
    manual_files = ['ku-001.json', 'ma-001.json', 'ma-002.json', 'ma-003.json', 'wa-001.json']
    
    for filename in manual_files:
        filepath = prime_roots_dir / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                root = json.load(f)
                manual_roots.append(root)
                print(f"  Loaded {filename}: {root['id']}")
    
    return manual_roots


def load_generated_prime_roots(prime_roots_dir):
    """Load generated prime roots from generated-prime-roots.json."""
    generated_file = prime_roots_dir / 'generated-prime-roots.json'
    
    if not generated_file.exists():
        print("  No generated-prime-roots.json found")
        return []
    
    with open(generated_file, 'r', encoding='utf-8') as f:
        roots = json.load(f)
        print(f"  Loaded {len(roots)} generated roots")
        return roots


def consolidate_and_renumber(manual_roots, generated_roots):
    """
    Consolidate all roots and assign sequential IDs.
    
    For each plain_name:
    - Manual roots keep their meanings and tones
    - Generated roots get assigned the next available number
    - IDs follow pattern: root_001, root_002, etc.
    """
    # Group by plain_name
    roots_by_name = defaultdict(list)
    
    # Add manual roots first (they have priority)
    for root in manual_roots:
        plain_name = root['plain_name']
        # Remove any extra fields, keep only schema fields
        clean_root = {
            'id': root['id'],  # Will be renumbered later
            'plain_name': root['plain_name'],
            'syllable_id': root['syllable_id'],
            'vowelGroup': root['vowelGroup'],
            'gloss': root['gloss']
        }
        roots_by_name[plain_name].append(('manual', clean_root))
    
    # Add generated roots
    for root in generated_roots:
        plain_name = root['plain_name']
        # Check if this root already exists as manual
        existing = [r for r in roots_by_name[plain_name] if r[0] == 'manual']
        
        if not existing:
            # Only add generated root if no manual version exists
            clean_root = {
                'id': '',  # Will be assigned
                'plain_name': root['plain_name'],
                'syllable_id': root['syllable_id'],
                'vowelGroup': root['vowelGroup'],
                'gloss': root['gloss']
            }
            roots_by_name[plain_name].append(('generated', clean_root))
    
    # Now assign sequential IDs per plain_name
    all_roots = []
    
    for plain_name in sorted(roots_by_name.keys()):
        entries = roots_by_name[plain_name]
        
        for idx, (source, root) in enumerate(entries, start=1):
            root['id'] = f"{plain_name}_{idx:03d}"
            all_roots.append(root)
            print(f"  {source:9s}: {root['id']:15s} - {root['gloss']}")
    
    return all_roots


def save_consolidated_file(roots, output_file):
    """Save all roots to prime-verb-roots.json."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(roots, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Saved {len(roots)} prime roots to {output_file}")


def main():
    """Main consolidation process."""
    repo_root = Path(__file__).parent
    prime_roots_dir = repo_root / 'language-data' / 'verbs' / 'prime-roots'
    
    print("=" * 70)
    print("Consolidating Prime Roots")
    print("=" * 70)
    print()
    
    # Load all roots
    print("Loading manual prime roots...")
    manual_roots = load_manual_prime_roots(prime_roots_dir)
    
    print(f"\nLoading generated prime roots...")
    generated_roots = load_generated_prime_roots(prime_roots_dir)
    
    print(f"\nConsolidating and renumbering...")
    print(f"Manual roots: {len(manual_roots)}")
    print(f"Generated roots: {len(generated_roots)}")
    print(f"Checking for overlaps and assigning IDs...\n")
    
    all_roots = consolidate_and_renumber(manual_roots, generated_roots)
    
    # Save to new file
    output_file = prime_roots_dir / 'prime-verb-roots.json'
    save_consolidated_file(all_roots, output_file)
    
    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total prime roots: {len(all_roots)}")
    print(f"Output file: {output_file}")
    print()
    print("Next steps:")
    print("1. Review prime-verb-roots.json")
    print("2. Delete old individual files if satisfied")
    print("3. Update generation script")
    print("4. Update tests")


if __name__ == '__main__':
    main()
