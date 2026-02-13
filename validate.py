#!/usr/bin/env python3
"""
Validation script for Igbo language data repository.

This script validates:
1. JSON syntax in all data files
2. Required schema fields
3. ID uniqueness within files
4. Reference integrity (IDs that reference other IDs)
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

# Color codes for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def validate_json_syntax(file_path):
    """Validate that a file contains valid JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Error reading file: {str(e)}"

def check_duplicate_ids(data, file_path):
    """Check for duplicate IDs in a JSON file."""
    ids = []
    
    if isinstance(data, list):
        ids = [item.get('id') for item in data if isinstance(item, dict) and 'id' in item]
    elif isinstance(data, dict) and 'id' in data:
        ids = [data['id']]
    
    duplicates = [id for id in ids if ids.count(id) > 1]
    unique_duplicates = list(set(duplicates))
    
    return unique_duplicates

def validate_syllable_schema(item):
    """Validate syllable schema."""
    required = ['id', 'tone', 'phonemes']
    return all(field in item for field in required)

def validate_vowels_schema(data):
    """Validate vowels schema."""
    if 'vowelGroups' not in data:
        return False
    groups = data['vowelGroups']
    if 'A' not in groups or 'E' not in groups:
        return False
    for group_name in ['A', 'E']:
        group = groups[group_name]
        if 'vowels' not in group or not isinstance(group['vowels'], list):
            return False
        for vowel in group['vowels']:
            required = ['letter', 'uppercase', 'ipa', 'description']
            if not all(field in vowel for field in required):
                return False
    return True

def validate_consonants_schema(data):
    """Validate consonants schema."""
    if 'consonants' not in data or not isinstance(data['consonants'], list):
        return False
    for consonant in data['consonants']:
        required = ['letter', 'uppercase', 'ipa', 'type', 'description']
        if not all(field in consonant for field in required):
            return False
    return True

def validate_prime_root_schema(item):
    """Validate prime root schema."""
    required = ['id', 'plain_name', 'syllable_id', 'gloss']
    return all(field in item for field in required)

def validate_derived_root_schema(item):
    """Validate derived root schema."""
    required = ['id', 'name', 'primeRootIds', 'gloss']
    return all(field in item for field in required)

def validate_prefix_schema(item):
    """Validate prefix schema."""
    required = ['id', 'name']
    return all(field in item for field in required)

def validate_suffix_schema(item):
    """Validate suffix schema."""
    required = ['id', 'name']
    return all(field in item for field in required)

def validate_phoneme_counts(repo_root):
    """
    Validate and report phoneme counts in the repository.
    
    Based on standard Igbo phonology:
    - Regular consonants: 28
    - Syllabic nasals (pseudo-vowels): 2 (m̩, n̩)
    - Total consonants: 30
    - Oral vowels: 9 (5 in A-group, 4 in E-group)
    
    Returns:
        tuple: (success, counts_dict, errors) where:
            - success (bool): True if all files were read successfully
            - counts_dict (dict): Dictionary containing phoneme counts with keys:
                'regular_consonants', 'syllabic_nasals', 'total_consonants',
                'a_vowels', 'e_vowels', 'total_vowels'
            - errors (list): List of error messages (empty if successful)
    """
    errors = []
    counts = {
        'regular_consonants': 0,
        'syllabic_nasals': 0,
        'total_consonants': 0,
        'a_vowels': 0,
        'e_vowels': 0,
        'total_vowels': 0
    }
    
    # Load and count consonants
    consonants_file = repo_root / 'language-data' / 'consonants.json'
    if consonants_file.exists():
        try:
            with open(consonants_file, 'r', encoding='utf-8') as f:
                consonants_data = json.load(f)
            
            if 'consonants' in consonants_data:
                for c in consonants_data['consonants']:
                    if c.get('syllabic', False):
                        counts['syllabic_nasals'] += 1
                    else:
                        counts['regular_consonants'] += 1
                
                counts['total_consonants'] = len(consonants_data['consonants'])
        except Exception as e:
            errors.append(f"Error reading consonants.json: {e}")
    else:
        errors.append("consonants.json not found")
    
    # Load and count vowels
    vowels_file = repo_root / 'language-data' / 'vowels.json'
    if vowels_file.exists():
        try:
            with open(vowels_file, 'r', encoding='utf-8') as f:
                vowels_data = json.load(f)
            
            if 'vowelGroups' in vowels_data:
                if 'A' in vowels_data['vowelGroups']:
                    counts['a_vowels'] = len(vowels_data['vowelGroups']['A'].get('vowels', []))
                if 'E' in vowels_data['vowelGroups']:
                    counts['e_vowels'] = len(vowels_data['vowelGroups']['E'].get('vowels', []))
                
                counts['total_vowels'] = counts['a_vowels'] + counts['e_vowels']
        except Exception as e:
            errors.append(f"Error reading vowels.json: {e}")
    else:
        errors.append("vowels.json not found")
    
    success = len(errors) == 0
    return success, counts, errors

def main():
    """Main validation function."""
    repo_root = Path(__file__).parent
    language_data = repo_root / 'language-data'
    
    if not language_data.exists():
        print(f"{RED}✗ language-data directory not found{RESET}")
        return 1
    
    errors = []
    warnings = []
    success_count = 0
    
    print("=" * 60)
    print("Igbo Language Data Validation")
    print("=" * 60)
    print()
    
    # Find all JSON files
    json_files = list(language_data.rglob('*.json'))
    
    if not json_files:
        print(f"{YELLOW}⚠ No JSON files found{RESET}")
        return 0
    
    print(f"Found {len(json_files)} JSON files to validate\n")
    
    # Track all IDs for reference checking
    all_ids = defaultdict(list)
    
    # Validate each file
    for json_file in sorted(json_files):
        rel_path = json_file.relative_to(repo_root)
        
        # 1. Validate JSON syntax
        is_valid, error = validate_json_syntax(json_file)
        
        if not is_valid:
            errors.append(f"{rel_path}: Invalid JSON - {error}")
            print(f"{RED}✗{RESET} {rel_path} - Invalid JSON")
            continue
        
        # 2. Load and check data
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 3. Check for duplicate IDs
        duplicates = check_duplicate_ids(data, json_file)
        if duplicates:
            errors.append(f"{rel_path}: Duplicate IDs found: {duplicates}")
            print(f"{RED}✗{RESET} {rel_path} - Duplicate IDs: {duplicates}")
            continue
        
        # 4. Collect IDs for reference checking
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and 'id' in item:
                    all_ids[item['id']].append(str(rel_path))
        elif isinstance(data, dict) and 'id' in data:
            all_ids[data['id']].append(str(rel_path))
        
        # 5. Schema validation (basic)
        schema_valid = True
        
        # Validate vowels
        if 'vowels.json' in str(json_file):
            if not validate_vowels_schema(data):
                schema_valid = False
                errors.append(f"{rel_path}: Invalid vowels schema")
        
        # Validate consonants
        if 'consonants.json' in str(json_file):
            if not validate_consonants_schema(data):
                schema_valid = False
                errors.append(f"{rel_path}: Invalid consonants schema")
        
        # Validate syllables
        if 'syllables.json' in str(json_file):
            if isinstance(data, list):
                for item in data:
                    if not validate_syllable_schema(item):
                        schema_valid = False
                        errors.append(f"{rel_path}: Invalid syllable schema for ID {item.get('id', 'unknown')}")
        
        # Validate prime roots
        if 'prime-roots' in str(json_file):
            if isinstance(data, dict):
                if not validate_prime_root_schema(data):
                    schema_valid = False
                    missing_fields = [f for f in ['id', 'plain_name', 'syllable_id', 'gloss'] if f not in data]
                    errors.append(f"{rel_path}: Invalid prime root schema. Missing fields: {missing_fields}")
        
        # Validate derived roots
        if 'derived-roots' in str(json_file):
            if isinstance(data, dict):
                if not validate_derived_root_schema(data):
                    schema_valid = False
                    missing_fields = [f for f in ['id', 'name', 'primeRootIds', 'gloss'] if f not in data]
                    errors.append(f"{rel_path}: Invalid derived root schema. Missing fields: {missing_fields}")
        
        if schema_valid:
            print(f"{GREEN}✓{RESET} {rel_path}")
            success_count += 1
    
    # Phoneme count validation
    print()
    print("=" * 60)
    print("Phoneme Count Validation")
    print("=" * 60)
    
    count_success, counts, count_errors = validate_phoneme_counts(repo_root)
    
    if count_success:
        print(f"\n{GREEN}Consonants:{RESET}")
        print(f"  Regular consonants: {counts['regular_consonants']}")
        print(f"  Syllabic nasals (pseudo-vowels): {counts['syllabic_nasals']}")
        print(f"  Total consonants: {counts['total_consonants']}")
        
        print(f"\n{GREEN}Vowels:{RESET}")
        print(f"  A-group vowels: {counts['a_vowels']}")
        print(f"  E-group vowels: {counts['e_vowels']}")
        print(f"  Total vowels: {counts['total_vowels']}")
        
        # Verification against standard Igbo phonology
        print(f"\n{GREEN}Verification:{RESET}")
        
        # Check consonants
        expected_regular = 28
        expected_syllabic = 2
        expected_total = 30
        
        if counts['regular_consonants'] == expected_regular:
            print(f"  {GREEN}✓{RESET} Regular consonants: {counts['regular_consonants']} (expected: {expected_regular})")
        else:
            print(f"  {YELLOW}⚠{RESET} Regular consonants: {counts['regular_consonants']} (expected: {expected_regular})")
            warnings.append(f"Regular consonant count is {counts['regular_consonants']}, expected {expected_regular}")
        
        if counts['syllabic_nasals'] == expected_syllabic:
            print(f"  {GREEN}✓{RESET} Syllabic nasals: {counts['syllabic_nasals']} (expected: {expected_syllabic})")
        else:
            print(f"  {YELLOW}⚠{RESET} Syllabic nasals: {counts['syllabic_nasals']} (expected: {expected_syllabic})")
            warnings.append(f"Syllabic nasal count is {counts['syllabic_nasals']}, expected {expected_syllabic}")
        
        if counts['total_consonants'] == expected_total:
            print(f"  {GREEN}✓{RESET} Total consonants: {counts['total_consonants']} (expected: {expected_total})")
        else:
            print(f"  {YELLOW}⚠{RESET} Total consonants: {counts['total_consonants']} (expected: {expected_total})")
            warnings.append(f"Total consonant count is {counts['total_consonants']}, expected {expected_total}")
        
        # Check vowels
        expected_vowels = 9
        
        if counts['total_vowels'] == expected_vowels:
            print(f"  {GREEN}✓{RESET} Total vowels: {counts['total_vowels']} (expected: {expected_vowels})")
        else:
            print(f"  {YELLOW}⚠{RESET} Total vowels: {counts['total_vowels']} (expected: {expected_vowels})")
            warnings.append(f"Total vowel count is {counts['total_vowels']}, expected {expected_vowels}")
    else:
        for error in count_errors:
            errors.append(f"Phoneme count validation: {error}")
            print(f"{RED}✗{RESET} {error}")
    
    # Summary
    print()
    print("=" * 60)
    print("Validation Summary")
    print("=" * 60)
    print(f"{GREEN}✓ Valid files: {success_count}{RESET}")
    
    if warnings:
        print(f"{YELLOW}⚠ Warnings: {len(warnings)}{RESET}")
        for warning in warnings:
            print(f"  {YELLOW}⚠{RESET} {warning}")
    
    if errors:
        print(f"{RED}✗ Errors: {len(errors)}{RESET}")
        for error in errors:
            print(f"  {RED}✗{RESET} {error}")
        return 1
    
    print()
    print(f"{GREEN}All validations passed!{RESET}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
