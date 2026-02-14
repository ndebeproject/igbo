#!/usr/bin/env python3
"""
Test script for generated monosyllabic verb roots and infinitives.
Verifies that the generation follows the correct rules.
"""

import json
import sys
from pathlib import Path


def test_problem_statement_examples():
    """Test examples from the problem statement."""
    print("Testing problem statement examples...")
    
    verbs_dir = Path(__file__).parent / 'language-data' / 'verbs'
    prime_roots_dir = verbs_dir / 'prime-roots'
    
    # Read JSON files
    with open(prime_roots_dir / 'prime-verb-roots.json', 'r', encoding='utf-8') as f:
        roots = json.load(f)
    
    with open(verbs_dir / 'generated-infinitives.json', 'r', encoding='utf-8') as f:
        infinitives = json.load(f)
    
    with open(verbs_dir / 'generated-dialectal-roots.json', 'r', encoding='utf-8') as f:
        dialectal_roots = json.load(f)
    
    with open(verbs_dir / 'generated-dialectal-infinitives.json', 'r', encoding='utf-8') as f:
        dialectal_infinitives = json.load(f)
    
    # Create lookup dictionaries - note: may have multiple entries per plain_name
    roots_by_name = {}
    for r in roots:
        if r['plain_name'] not in roots_by_name:
            roots_by_name[r['plain_name']] = []
        roots_by_name[r['plain_name']].append(r)
    
    infinitives_by_form = {i['infinitive_form']: i for i in infinitives}
    dialectal_by_form = {d['combined_form']: d for d in dialectal_roots}
    dialectal_inf_by_form = {d['infinitive_form']: d for d in dialectal_infinitives}
    
    # Test 1: ma (A-group) → ịma
    assert 'ma' in roots_by_name, "Root 'ma' not found"
    assert any(r['vowelGroup'] == 'A' for r in roots_by_name['ma']), "ma should be A-group"
    assert 'ịma' in infinitives_by_form, "Infinitive 'ịma' not found"
    print("  ✓ ma → ịma (A-group)")
    
    # Test 2: go (E-group) → igo
    assert 'go' in roots_by_name, "Root 'go' not found"
    assert any(r['vowelGroup'] == 'E' for r in roots_by_name['go']), "go should be E-group"
    assert 'igo' in infinitives_by_form, "Infinitive 'igo' not found"
    print("  ✓ go → igo (E-group)")
    
    # Test 3: la / ra dialectal variation
    assert 'la / ra' in dialectal_by_form, "Dialectal root 'la / ra' not found"
    assert 'ịla / ịra' in dialectal_inf_by_form, "Dialectal infinitive 'ịla / ịra' not found"
    print("  ✓ la / ra → ịla / ịra (L/R dialectal)")
    
    # Test 4: le / re dialectal variation
    assert 'le / re' in dialectal_by_form, "Dialectal root 'le / re' not found"
    assert 'ile / ire' in dialectal_inf_by_form, "Dialectal infinitive 'ile / ire' not found"
    print("  ✓ le / re → ile / ire (L/R dialectal)")
    
    print()


def test_vowel_harmony():
    """Test that vowel harmony rules are correctly applied."""
    print("Testing vowel harmony...")
    
    verbs_dir = Path(__file__).parent / 'language-data' / 'verbs'
    
    with open(verbs_dir / 'generated-infinitives.json', 'r', encoding='utf-8') as f:
        infinitives = json.load(f)
    
    infinitives_by_form = {i['infinitive_form']: i for i in infinitives}
    
    # A-group vowels should have ị prefix
    a_group_tests = [
        ('ba', 'ịba'),
        ('bẹ', 'ịbẹ'),
        ('bị', 'ịbị'),
        ('bọ', 'ịbọ'),
        ('bụ', 'ịbụ'),
    ]
    
    for root, expected_inf in a_group_tests:
        assert expected_inf in infinitives_by_form, f"A-group infinitive '{expected_inf}' not found"
        assert infinitives_by_form[expected_inf]['vowelGroup'] == 'A', f"{expected_inf} should be A-group"
        assert infinitives_by_form[expected_inf]['prefix'] == 'ị', f"{expected_inf} should have ị prefix"
    print("  ✓ A-group vowels (a, ẹ, ị, ọ, ụ) use ị prefix")
    
    # E-group vowels should have i prefix
    e_group_tests = [
        ('be', 'ibe'),
        ('bi', 'ibi'),
        ('bo', 'ibo'),
        ('bu', 'ibu'),
    ]
    
    for root, expected_inf in e_group_tests:
        assert expected_inf in infinitives_by_form, f"E-group infinitive '{expected_inf}' not found"
        assert infinitives_by_form[expected_inf]['vowelGroup'] == 'E', f"{expected_inf} should be E-group"
        assert infinitives_by_form[expected_inf]['prefix'] == 'i', f"{expected_inf} should have i prefix"
    print("  ✓ E-group vowels (e, i, o, u) use i prefix")
    
    print()


def test_counts():
    """Test that the expected number of entries exist."""
    print("Testing counts...")
    
    verbs_dir = Path(__file__).parent / 'language-data' / 'verbs'
    prime_roots_dir = verbs_dir / 'prime-roots'
    
    # Read JSON files
    with open(prime_roots_dir / 'prime-verb-roots.json', 'r', encoding='utf-8') as f:
        roots = json.load(f)
    
    with open(verbs_dir / 'generated-infinitives.json', 'r', encoding='utf-8') as f:
        infinitives = json.load(f)
    
    with open(verbs_dir / 'generated-dialectal-roots.json', 'r', encoding='utf-8') as f:
        dialectal_roots = json.load(f)
    
    with open(verbs_dir / 'generated-dialectal-infinitives.json', 'r', encoding='utf-8') as f:
        dialectal_infinitives = json.load(f)
    
    # Check counts - now includes manual + generated (272 total: 270 generated + 2 manual that don't overlap)
    assert len(roots) == 272, f"Expected 272 roots (270 generated + 2 manual non-overlapping), got {len(roots)}"
    print(f"  ✓ {len(roots)} monosyllabic prime roots (includes manual + generated)")
    
    assert len(infinitives) == 270, f"Expected 270 infinitives, got {len(infinitives)}"
    print(f"  ✓ {len(infinitives)} base infinitives")
    
    assert len(dialectal_roots) == 63, f"Expected 63 dialectal roots, got {len(dialectal_roots)}"
    print(f"  ✓ {len(dialectal_roots)} dialectal verb root variations")
    
    assert len(dialectal_infinitives) == 63, f"Expected 63 dialectal infinitives, got {len(dialectal_infinitives)}"
    print(f"  ✓ {len(dialectal_infinitives)} dialectal infinitive variations")
    
    # Check for no duplicate IDs
    root_ids = [r['id'] for r in roots]
    assert len(root_ids) == len(set(root_ids)), "Duplicate root IDs found"
    
    inf_ids = [i['id'] for i in infinitives]
    assert len(inf_ids) == len(set(inf_ids)), "Duplicate infinitive IDs found"
    
    dial_ids = [d['id'] for d in dialectal_roots]
    assert len(dial_ids) == len(set(dial_ids)), "Duplicate dialectal root IDs found"
    
    dial_inf_ids = [d['id'] for d in dialectal_infinitives]
    assert len(dial_inf_ids) == len(set(dial_inf_ids)), "Duplicate dialectal infinitive IDs found"
    
    print("  ✓ No duplicate IDs in any file")
    
    print()


def test_dialectal_patterns():
    """Test that major dialectal patterns are represented."""
    print("Testing dialectal patterns...")
    
    verbs_dir = Path(__file__).parent / 'language-data' / 'verbs'
    
    with open(verbs_dir / 'generated-dialectal-roots.json', 'r', encoding='utf-8') as f:
        dialectal_roots = json.load(f)
    
    dialectal_by_form = {d['combined_form']: d for d in dialectal_roots}
    
    # Check for major patterns
    patterns = {
        'L/R': ['la / ra', 'le / re'],
        'B/V': ['ba / va', 'be / ve'],
        'G/V': ['ga / va', 'go / vo'],
        'F/P': ['fa / pa', 'fo / po'],
        'J/Z': ['ja / za', 'jo / zo'],
        'S/T': ['sa / ta', 'so / to'],
        'H/Y': ['ha / ya', 'ho / yo'],
    }
    
    for pattern_name, examples in patterns.items():
        for example in examples:
            assert example in dialectal_by_form, f"Pattern {pattern_name} example '{example}' not found"
        print(f"  ✓ {pattern_name} pattern represented")
    
    print()


def main():
    """Run all tests."""
    print("=" * 70)
    print("Testing Generated Verb Roots and Infinitives")
    print("=" * 70)
    print()
    
    try:
        test_problem_statement_examples()
        test_vowel_harmony()
        test_counts()
        test_dialectal_patterns()
        
        print("=" * 70)
        print("All tests passed! ✓")
        print("=" * 70)
        return 0
    except AssertionError as e:
        print()
        print("=" * 70)
        print(f"Test failed: {e}")
        print("=" * 70)
        return 1
    except Exception as e:
        print()
        print("=" * 70)
        print(f"Error: {e}")
        print("=" * 70)
        return 1


if __name__ == '__main__':
    sys.exit(main())
