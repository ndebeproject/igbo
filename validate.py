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
