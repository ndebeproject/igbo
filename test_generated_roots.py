#!/usr/bin/env python3
"""
Test script for generated monosyllabic verb roots and infinitives.
Verifies that the generation follows the correct rules.
"""

import sys
from pathlib import Path


def test_problem_statement_examples():
    """Test examples from the problem statement."""
    print("Testing problem statement examples...")
    
    generated_dir = Path(__file__).parent / 'generated'
    
    # Read files
    with open(generated_dir / 'monosyllabic_verb_roots.txt', 'r', encoding='utf-8') as f:
        roots = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    with open(generated_dir / 'infinitives.txt', 'r', encoding='utf-8') as f:
        infinitives = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    with open(generated_dir / 'dialectal_verb_roots.txt', 'r', encoding='utf-8') as f:
        dialectal_roots = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    with open(generated_dir / 'dialectal_infinitives.txt', 'r', encoding='utf-8') as f:
        dialectal_infinitives = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    # Test 1: ma (A-group) → ịma
    assert 'ma' in roots, "Root 'ma' not found"
    assert 'ịma' in infinitives, "Infinitive 'ịma' not found"
    print("  ✓ ma → ịma (A-group)")
    
    # Test 2: go (E-group) → igo
    assert 'go' in roots, "Root 'go' not found"
    assert 'igo' in infinitives, "Infinitive 'igo' not found"
    print("  ✓ go → igo (E-group)")
    
    # Test 3: la / ra dialectal variation
    assert 'la / ra' in dialectal_roots, "Dialectal root 'la / ra' not found"
    assert 'ịla / ịra' in dialectal_infinitives, "Dialectal infinitive 'ịla / ịra' not found"
    print("  ✓ la / ra → ịla / ịra (L/R dialectal)")
    
    # Test 4: le / re dialectal variation
    assert 'le / re' in dialectal_roots, "Dialectal root 'le / re' not found"
    assert 'ile / ire' in dialectal_infinitives, "Dialectal infinitive 'ile / ire' not found"
    print("  ✓ le / re → ile / ire (L/R dialectal)")
    
    print()


def test_vowel_harmony():
    """Test that vowel harmony rules are correctly applied."""
    print("Testing vowel harmony...")
    
    generated_dir = Path(__file__).parent / 'generated'
    
    with open(generated_dir / 'infinitives.txt', 'r', encoding='utf-8') as f:
        infinitives = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    # A-group vowels should have ị prefix
    a_group_tests = [
        ('ba', 'ịba'),
        ('bẹ', 'ịbẹ'),
        ('bị', 'ịbị'),
        ('bọ', 'ịbọ'),
        ('bụ', 'ịbụ'),
    ]
    
    for root, expected_inf in a_group_tests:
        assert expected_inf in infinitives, f"A-group infinitive '{expected_inf}' not found"
    print("  ✓ A-group vowels (a, ẹ, ị, ọ, ụ) use ị prefix")
    
    # E-group vowels should have i prefix
    e_group_tests = [
        ('be', 'ibe'),
        ('bi', 'ibi'),
        ('bo', 'ibo'),
        ('bu', 'ibu'),
    ]
    
    for root, expected_inf in e_group_tests:
        assert expected_inf in infinitives, f"E-group infinitive '{expected_inf}' not found"
    print("  ✓ E-group vowels (e, i, o, u) use i prefix")
    
    print()


def test_counts():
    """Test that the expected number of entries exist."""
    print("Testing counts...")
    
    generated_dir = Path(__file__).parent / 'generated'
    
    # Read files
    with open(generated_dir / 'monosyllabic_verb_roots.txt', 'r', encoding='utf-8') as f:
        roots = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    with open(generated_dir / 'infinitives.txt', 'r', encoding='utf-8') as f:
        infinitives = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    with open(generated_dir / 'dialectal_verb_roots.txt', 'r', encoding='utf-8') as f:
        dialectal_roots = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    with open(generated_dir / 'dialectal_infinitives.txt', 'r', encoding='utf-8') as f:
        dialectal_infinitives = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    # Check counts
    assert len(roots) == 270, f"Expected 270 roots, got {len(roots)}"
    print(f"  ✓ {len(roots)} monosyllabic verb roots (30 consonants × 9 vowels)")
    
    assert len(infinitives) == 270, f"Expected 270 infinitives, got {len(infinitives)}"
    print(f"  ✓ {len(infinitives)} base infinitives")
    
    assert len(dialectal_roots) == 63, f"Expected 63 dialectal roots, got {len(dialectal_roots)}"
    print(f"  ✓ {len(dialectal_roots)} dialectal verb root variations")
    
    assert len(dialectal_infinitives) == 63, f"Expected 63 dialectal infinitives, got {len(dialectal_infinitives)}"
    print(f"  ✓ {len(dialectal_infinitives)} dialectal infinitive variations")
    
    # Check for no duplicates
    assert len(roots) == len(set(roots)), "Duplicate roots found"
    assert len(infinitives) == len(set(infinitives)), "Duplicate infinitives found"
    assert len(dialectal_roots) == len(set(dialectal_roots)), "Duplicate dialectal roots found"
    assert len(dialectal_infinitives) == len(set(dialectal_infinitives)), "Duplicate dialectal infinitives found"
    print("  ✓ No duplicates in any file")
    
    print()


def test_dialectal_patterns():
    """Test that major dialectal patterns are represented."""
    print("Testing dialectal patterns...")
    
    generated_dir = Path(__file__).parent / 'generated'
    
    with open(generated_dir / 'dialectal_verb_roots.txt', 'r', encoding='utf-8') as f:
        dialectal_roots = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
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
            assert example in dialectal_roots, f"Pattern {pattern_name} example '{example}' not found"
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
