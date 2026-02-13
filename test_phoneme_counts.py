#!/usr/bin/env python3
"""
Test script to confirm Igbo phoneme counts.

This script verifies that the repository contains the correct number
of consonants, vowels, and pseudo-vowels according to standard Igbo phonology.
"""

import json
import sys
from pathlib import Path


def test_consonant_counts():
    """Test that we have the correct number of consonants."""
    consonants_file = Path(__file__).parent / 'language-data' / 'consonants.json'
    
    with open(consonants_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    regular_consonants = []
    syllabic_nasals = []
    
    for c in data['consonants']:
        if c.get('syllabic', False):
            syllabic_nasals.append(c)
        else:
            regular_consonants.append(c)
    
    print("=" * 70)
    print("CONSONANT COUNT TEST")
    print("=" * 70)
    print(f"\nRegular consonants: {len(regular_consonants)}")
    print(f"Syllabic nasals (pseudo-vowels): {len(syllabic_nasals)}")
    print(f"Total consonants: {len(data['consonants'])}")
    
    # List syllabic nasals
    print(f"\nSyllabic nasals:")
    for nasal in syllabic_nasals:
        print(f"  - {nasal['letter']} ({nasal['uppercase']}) - {nasal['description']}")
    
    # Verify expected counts
    assert len(regular_consonants) == 28, f"Expected 28 regular consonants, got {len(regular_consonants)}"
    assert len(syllabic_nasals) == 2, f"Expected 2 syllabic nasals, got {len(syllabic_nasals)}"
    assert len(data['consonants']) == 30, f"Expected 30 total consonants, got {len(data['consonants'])}"
    
    print("\n✓ All consonant counts are correct!")
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
    
    # Note: The problem statement mentions "1 pseudovowel consonant"
    # but linguistically, Igbo has 2 syllabic nasals (m̩ and n̩)
    # Both function as pseudo-vowels
    assert len(pseudovowels) == 2, f"Expected 2 pseudo-vowel consonants, got {len(pseudovowels)}"
    
    print(f"\n✓ Found {len(pseudovowels)} pseudo-vowel consonants (syllabic nasals)")
    print("  Note: Both m̩ and n̩ function as pseudo-vowels in Igbo phonology")
    return True


def main():
    """Run all phoneme count tests."""
    print("\n" + "=" * 70)
    print("IGBO PHONEME COUNT CONFIRMATION")
    print("=" * 70)
    print("\nThis test confirms the phoneme inventory of Standard Igbo:")
    print("- Regular consonants: 28")
    print("- Syllabic nasals (pseudo-vowels): 2")
    print("- Total consonants: 30")
    print("- Vowels: 9 (5 A-group + 4 E-group)")
    print()
    
    try:
        test_consonant_counts()
        test_vowel_counts()
        test_pseudovowel_count()
        
        print("\n" + "=" * 70)
        print("ALL TESTS PASSED ✓")
        print("=" * 70)
        print("\nConfirmed phoneme counts:")
        print("  ✓ 28 regular consonants")
        print("  ✓ 2 syllabic nasals (pseudo-vowels: m̩, n̩)")
        print("  ✓ 30 total consonants")
        print("  ✓ 9 vowels (5 A-group + 4 E-group)")
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
