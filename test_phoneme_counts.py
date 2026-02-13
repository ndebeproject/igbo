#!/usr/bin/env python3
"""
Test script to confirm Igbo phoneme counts.

This script verifies that the repository contains the correct number
of consonants, vowels, and pseudo-vowels according to standard Igbo phonology
including dialectal variations.
"""

import json
import sys
from pathlib import Path


def test_consonant_counts():
    """Test that we have the correct number of consonants including dialectal variants."""
    consonants_file = Path(__file__).parent / 'language-data' / 'consonants.json'
    
    with open(consonants_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    regular_consonants = []
    syllabic_nasals = []
    
    # Major dialectal alternation patterns
    major_dialect_patterns = [
        'L/R', 'B/V', 'G/V', 'F/H/SH', 'S/SH', 'Y/H',
        'N/L/Y', 'J/Z', 'S/T', 'F/P', 'B/W', 'W/GH'
    ]
    
    for c in data['consonants']:
        if c.get('syllabic', False):
            syllabic_nasals.append(c)
        else:
            regular_consonants.append(c)
    
    # Count major dialectal variant patterns present
    patterns_found = set()
    for c in data['consonants']:
        for alt_set in c.get('alternation_sets', []):
            pattern = alt_set.get('pattern', '')
            if pattern in major_dialect_patterns:
                patterns_found.add(pattern)
    
    base_count = len(data['consonants'])
    dialectal_count = len(patterns_found)
    total_with_dialects = base_count + dialectal_count
    
    print("=" * 70)
    print("CONSONANT COUNT TEST (WITH DIALECTAL VARIANTS)")
    print("=" * 70)
    print(f"\nBase consonant forms: {base_count}")
    print(f"  - Regular consonants: {len(regular_consonants)}")
    print(f"  - Syllabic nasals (pseudo-vowels): {len(syllabic_nasals)}")
    print(f"\nMajor dialectal variant forms: {dialectal_count}")
    print(f"  Patterns found: {sorted(patterns_found)}")
    print(f"\nTotal (including dialectal variants): {total_with_dialects}")
    
    # List syllabic nasals
    print(f"\nSyllabic nasals (pseudo-vowels):")
    for nasal in syllabic_nasals:
        print(f"  - {nasal['letter']} ({nasal['uppercase']}) - {nasal['description']}")
    
    # Verify expected counts
    assert len(regular_consonants) == 28, f"Expected 28 regular consonants, got {len(regular_consonants)}"
    assert len(syllabic_nasals) == 2, f"Expected 2 syllabic nasals, got {len(syllabic_nasals)}"
    assert base_count == 30, f"Expected 30 base consonants, got {base_count}"
    assert dialectal_count == 12, f"Expected 12 major dialectal variants, got {dialectal_count}"
    assert total_with_dialects == 42, f"Expected 42 total consonants with dialectal variants, got {total_with_dialects}"
    
    print("\n✓ All consonant counts are correct!")
    print(f"  ✓ 42 consonants confirmed (30 base + 12 dialectal variants)")
    return True


def test_vowel_counts():
    """Test that we have the correct number of vowels."""
    vowels_file = Path(__file__).parent / 'language-data' / 'vowels.json'
    
    with open(vowels_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Safely extract vowel data with error handling
    if 'vowelGroups' not in data:
        raise ValueError("Missing 'vowelGroups' key in vowels.json")
    
    vowel_groups = data['vowelGroups']
    
    if 'A' not in vowel_groups:
        raise ValueError("Missing 'A' group in vowelGroups")
    if 'E' not in vowel_groups:
        raise ValueError("Missing 'E' group in vowelGroups")
    
    a_vowels = vowel_groups['A'].get('vowels', [])
    e_vowels = vowel_groups['E'].get('vowels', [])
    total_vowels = len(a_vowels) + len(e_vowels)
    
    print("\n" + "=" * 70)
    print("VOWEL COUNT TEST")
    print("=" * 70)
    print(f"\nA-group vowels: {len(a_vowels)}")
    print(f"  {[v['letter'] for v in a_vowels]}")
    print(f"\nE-group vowels: {len(e_vowels)}")
    print(f"  {[v['letter'] for v in e_vowels]}")
    print(f"\nTotal vowels: {total_vowels}")
    
    # Verify expected counts
    assert len(a_vowels) == 5, f"Expected 5 A-group vowels, got {len(a_vowels)}"
    assert len(e_vowels) == 4, f"Expected 4 E-group vowels, got {len(e_vowels)}"
    assert total_vowels == 9, f"Expected 9 total vowels, got {total_vowels}"
    
    print("\n✓ All vowel counts are correct!")
    return True


def test_pseudovowel_count():
    """Test that we have the correct pseudo-vowel consonants."""
    consonants_file = Path(__file__).parent / 'language-data' / 'consonants.json'
    
    with open(consonants_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Count pseudo-vowels (syllabic nasals) - using consistent criteria
    # A consonant is a pseudo-vowel if it has the 'syllabic' property set to True
    pseudovowels = [c for c in data['consonants'] if c.get('syllabic', False)]
    
    print("\n" + "=" * 70)
    print("PSEUDO-VOWEL COUNT TEST")
    print("=" * 70)
    print(f"\nPseudo-vowel consonants (syllabic nasals): {len(pseudovowels)}")
    
    for pv in pseudovowels:
        print(f"  - {pv['letter']} ({pv['uppercase']}) - {pv['description']}")
        functions = pv.get('functions_as', [])
        if functions:
            print(f"    Functions as: {functions}")
    
    # There are 2 syllabic nasals (m̩ and n̩) that function as pseudo-vowels
    # They are counted as 1 pseudovowel category containing 2 members
    assert len(pseudovowels) == 2, f"Expected 2 pseudo-vowel consonants, got {len(pseudovowels)}"
    
    print(f"\n✓ Found {len(pseudovowels)} pseudo-vowel consonants (syllabic nasals)")
    print("  Note: Both m̩ and n̩ function as pseudo-vowels in Igbo phonology")
    print("  They are counted as 1 pseudovowel consonant category")
    return True


def main():
    """Run all phoneme count tests."""
    print("\n" + "=" * 70)
    print("IGBO PHONEME COUNT CONFIRMATION")
    print("=" * 70)
    print("\nThis test confirms the phoneme inventory of Standard Igbo:")
    print("- Base consonants: 30 (28 regular + 2 syllabic nasals)")
    print("- Major dialectal variants: 12 (L/R, B/V, etc.)")
    print("- Total consonants (with dialectal variants): 42")
    print("- Vowels: 9 (5 A-group + 4 E-group)")
    print("- Pseudovowel consonant category: 1 (containing 2 syllabic nasals)")
    print()
    
    try:
        test_consonant_counts()
        test_vowel_counts()
        test_pseudovowel_count()
        
        print("\n" + "=" * 70)
        print("ALL TESTS PASSED ✓")
        print("=" * 70)
        print("\nConfirmed phoneme counts:")
        print("  ✓ 42 consonants (30 base + 12 dialectal variants)")
        print("    - 28 regular consonants")
        print("    - 2 syllabic nasals (pseudo-vowels: m̩, n̩)")
        print("    - 12 major dialectal variant forms")
        print("  ✓ 9 vowels (5 A-group + 4 E-group)")
        print("  ✓ 1 pseudovowel consonant category (2 syllabic nasals)")
        print("\nSee PHONEME_COUNTS.md for detailed documentation.")
        print()
        
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
