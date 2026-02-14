#!/usr/bin/env python3
"""
Test script for generated monosyllabic verb roots and infinitives.
Verifies that the generation follows the correct rules.
"""

import json
import sys
from pathlib import Path


def test_tone_variants():
    """Test that tone variants are properly generated."""
    print("Testing tone variants...")
    
    verbs_dir = Path(__file__).parent / 'language-data' / 'verbs'
    prime_roots_dir = verbs_dir / 'prime-roots'
    
    with open(prime_roots_dir / 'prime-verb-roots.json', 'r', encoding='utf-8') as f:
        roots = json.load(f)
    
    # Check structure of entries
    sample = roots[0]
    required_fields = ['id', 'plain_name', 'main_vowel', 'tone', 'syllable_group', 'vowelGroup', 'phonemes', 'ndebe', 'unicode']
    for field in required_fields:
        assert field in sample, f"Missing required field: {field}"
    print(f"  ✓ All required fields present: {required_fields}")
    
    # Check 'ma' has all three tones
    ma_roots = [r for r in roots if r['syllable_group'] == 'ma']
    assert len(ma_roots) == 3, f"Expected 3 tone variants for 'ma', got {len(ma_roots)}"
    
    tones = {r['tone'] for r in ma_roots}
    assert tones == {'high', 'mid', 'low'}, f"Expected all three tones, got {tones}"
    
    # Check tone marks
    ma_high = [r for r in ma_roots if r['tone'] == 'high'][0]
    ma_mid = [r for r in ma_roots if r['tone'] == 'mid'][0]
    ma_low = [r for r in ma_roots if r['tone'] == 'low'][0]
    
    assert ma_high['plain_name'] == 'má', f"Expected 'má' for high tone, got {ma_high['plain_name']}"
    assert ma_mid['plain_name'] == 'ma', f"Expected 'ma' for mid tone, got {ma_mid['plain_name']}"
    assert ma_low['plain_name'] == 'mà', f"Expected 'mà' for low tone, got {ma_low['plain_name']}"
    print("  ✓ Tone marks correctly applied (má, ma, mà)")
    
    # Check ID format
    assert ma_high['id'] == 'syl_ma_001', f"Expected 'syl_ma_001', got {ma_high['id']}"
    assert ma_mid['id'] == 'syl_ma_002', f"Expected 'syl_ma_002', got {ma_mid['id']}"
    assert ma_low['id'] == 'syl_ma_003', f"Expected 'syl_ma_003', got {ma_low['id']}"
    print("  ✓ ID format correct (syl_{syllable}_{###})")
    
    # Check phonemes structure - vowels should match plain_name exactly
    assert ma_high['phonemes'] == ['m', 'á'], f"Expected ['m', 'á'], got {ma_high['phonemes']}"
    assert ma_mid['phonemes'] == ['m', 'a'], f"Expected ['m', 'a'], got {ma_mid['phonemes']}"
    assert ma_low['phonemes'] == ['m', 'à'], f"Expected ['m', 'à'], got {ma_low['phonemes']}"
    print("  ✓ Phonemes correctly extracted with tone marks (má, a, mà)")
    
    # Check ndebe and unicode fields exist
    assert 'ndebe' in ma_high, "Missing 'ndebe' field"
    assert 'unicode' in ma_high, "Missing 'unicode' field"
    print("  ✓ Ndebe and unicode fields present")
    
    print()


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
    
    # Check counts - now with tone variants: 270 syllables × 3 tones = 810
    assert len(roots) == 810, f"Expected 810 roots (270 syllables × 3 tones), got {len(roots)}"
    print(f"  ✓ {len(roots)} monosyllabic prime roots (270 syllables × 3 tones)")
    
    # Infinitives should also be tripled
    assert len(infinitives) == 810, f"Expected 810 infinitives, got {len(infinitives)}"
    print(f"  ✓ {len(infinitives)} base infinitives")
    
    # Dialectal variations should also be tripled (63 syllable pairs × 3 tones = 189)
    assert len(dialectal_roots) == 189, f"Expected 189 dialectal roots, got {len(dialectal_roots)}"
    print(f"  ✓ {len(dialectal_roots)} dialectal verb root variations")
    
    assert len(dialectal_infinitives) == 189, f"Expected 189 dialectal infinitives, got {len(dialectal_infinitives)}"
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


def test_phonemes():
    """Test that phonemes are correctly extracted for all roots."""
    print("Testing phonemes extraction...")
    
    verbs_dir = Path(__file__).parent / 'language-data' / 'verbs'
    prime_roots_dir = verbs_dir / 'prime-roots'
    
    with open(prime_roots_dir / 'prime-verb-roots.json', 'r', encoding='utf-8') as f:
        roots = json.load(f)
    
    # Test specific examples with different consonant types (mid tone)
    test_cases = {
        'ba': ['b', 'a'],      # Single consonant
        'ma': ['m', 'a'],      # Single consonant
        'gba': ['gb', 'a'],    # Digraph consonant
        'kpa': ['kp', 'a'],    # Digraph consonant
        'gwa': ['gw', 'a'],    # Digraph consonant
        'shọ': ['sh', 'ọ'],    # Digraph consonant with special vowel
        'chẹ': ['ch', 'ẹ'],    # Digraph consonant with special vowel
    }
    
    for syllable_group, expected_phonemes in test_cases.items():
        roots_for_syllable = [r for r in roots if r['syllable_group'] == syllable_group and r['tone'] == 'mid']
        if roots_for_syllable:
            root = roots_for_syllable[0]
            assert root['phonemes'] == expected_phonemes, \
                f"Expected phonemes {expected_phonemes} for '{syllable_group}', got {root['phonemes']}"
    
    print("  ✓ Single consonants correctly extracted (b, m, etc.)")
    print("  ✓ Digraph consonants correctly extracted (gb, kp, gw, sh, ch)")
    
    # Test that tone marks are preserved in vowels
    tone_test_cases = [
        ('ba', 'high', ['b', 'á']),
        ('ba', 'mid', ['b', 'a']),
        ('ba', 'low', ['b', 'à']),
        ('bẹ', 'high', ['b', 'ẹ́']),
        ('bẹ', 'low', ['b', 'ẹ̀']),
        ('kpị', 'high', ['kp', 'ị́']),
        ('kpị', 'low', ['kp', 'ị̀']),
    ]
    
    for syllable_group, tone, expected_phonemes in tone_test_cases:
        roots_for_syllable = [r for r in roots if r['syllable_group'] == syllable_group and r['tone'] == tone]
        if roots_for_syllable:
            root = roots_for_syllable[0]
            assert root['phonemes'] == expected_phonemes, \
                f"Expected phonemes {expected_phonemes} for '{syllable_group}' ({tone}), got {root['phonemes']}"
    
    print("  ✓ Vowel tone marks correctly preserved (á, à, ẹ́, ẹ̀, ị́, ị̀)")
    
    # Verify all roots have phonemes matching plain_name
    mismatches = []
    for root in roots:
        plain_name = root['plain_name']
        consonant = root['phonemes'][0]
        vowel_in_phonemes = root['phonemes'][1]
        vowel_in_plain = plain_name[len(consonant):]
        
        if vowel_in_phonemes != vowel_in_plain:
            mismatches.append((root['id'], plain_name, root['phonemes']))
    
    assert len(mismatches) == 0, f"Found {len(mismatches)} mismatches between plain_name and phonemes vowels"
    print("  ✓ All phonemes vowels match exactly with plain_name vowels")
    
    # Verify all roots have phonemes
    all_have_phonemes = all('phonemes' in r for r in roots)
    assert all_have_phonemes, "Some roots missing 'phonemes' field"
    
    # Verify all phonemes are lists of 2 elements
    all_valid_structure = all(isinstance(r['phonemes'], list) and len(r['phonemes']) == 2 for r in roots)
    assert all_valid_structure, "Some phonemes have invalid structure (should be list of 2 elements)"
    
    print("  ✓ All roots have phonemes field")
    print("  ✓ All phonemes have correct structure [consonant, vowel]")
    
    print()


def main():
    """Run all tests."""
    print("=" * 70)
    print("Testing Generated Verb Roots and Infinitives")
    print("=" * 70)
    print()
    
    try:
        test_tone_variants()
        test_problem_statement_examples()
        test_vowel_harmony()
        test_counts()
        test_dialectal_patterns()
        test_phonemes()
        
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
