#!/usr/bin/env python3
"""
Remove the gloss field from all prime root entries.
"""

import json
from pathlib import Path


def remove_gloss_from_prime_roots(prime_roots_file):
    """Remove gloss field from all prime roots."""
    print(f"Loading {prime_roots_file}...")
    
    with open(prime_roots_file, 'r', encoding='utf-8') as f:
        roots = json.load(f)
    
    print(f"Found {len(roots)} prime roots")
    
    # Remove gloss field from each entry
    updated_roots = []
    for root in roots:
        updated_root = {
            'id': root['id'],
            'plain_name': root['plain_name'],
            'syllable_id': root['syllable_id'],
            'vowelGroup': root['vowelGroup']
        }
        updated_roots.append(updated_root)
    
    # Save back to file
    with open(prime_roots_file, 'w', encoding='utf-8') as f:
        json.dump(updated_roots, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Updated {len(updated_roots)} entries")
    print(f"✓ Saved to {prime_roots_file}")
    
    return updated_roots


def main():
    """Main function."""
    repo_root = Path(__file__).parent
    prime_roots_file = repo_root / 'language-data' / 'verbs' / 'prime-roots' / 'prime-verb-roots.json'
    
    print("=" * 70)
    print("Removing Gloss Field from Prime Roots")
    print("=" * 70)
    print()
    
    updated_roots = remove_gloss_from_prime_roots(prime_roots_file)
    
    print()
    print("Sample entries after update:")
    print("-" * 70)
    for i in [0, 100, 200]:
        if i < len(updated_roots):
            print(json.dumps(updated_roots[i], indent=2, ensure_ascii=False))
    
    print()
    print("✓ Done!")


if __name__ == '__main__':
    main()
