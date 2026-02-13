# Contributing to the Igbo Language Repository

Thank you for your interest in contributing to this project! This repository aims to create a comprehensive, structured database of Igbo language components.

## How to Contribute

### Types of Contributions

1. **Adding Language Data**
   - New verb roots and their tonal variations
   - Prefixes and suffixes
   - Complete verb forms with meanings
   - Nouns (basic and deverbal)
   - Particles and auxiliaries

2. **Improving Documentation**
   - Clarifying schemas
   - Adding examples
   - Correcting errors
   - Translating documentation

3. **Developing Tools**
   - Validation scripts
   - Data import/export tools
   - Visualization tools
   - Search and query utilities

4. **Quality Assurance**
   - Verifying data accuracy
   - Checking for duplicates
   - Validating references
   - Testing data integrity

## Getting Started

### Prerequisites

- Basic understanding of JSON format
- Knowledge of Igbo language (for linguistic contributions)
- Familiarity with Git and GitHub

### Setup

1. Fork this repository
2. Clone your fork locally
3. Create a new branch for your contribution
4. Make your changes
5. Test your changes (validate JSON, check references)
6. Submit a pull request

## Contribution Guidelines

### Data Quality Standards

1. **Accuracy**: All linguistic data must be accurate and verifiable
2. **Completeness**: Fill all required fields in the schema
3. **Consistency**: Follow established naming conventions and formats
4. **Tone Marking**: Always specify tone explicitly and correctly
5. **References**: Use IDs to link related components

### JSON Standards

- Use 2-space indentation
- Ensure valid JSON syntax (use a validator)
- Use UTF-8 encoding for special characters
- Follow the schemas defined in `SCHEMA.md`

### Naming Conventions

Follow the conventions in `SCHEMA.md`:
- Syllable IDs: `{syllable}_{tone}` (e.g., `ma_high`)
- Root IDs: `{root}_{number}` (e.g., `ba_001`)
- Prefix IDs: `prefix_{name}` (e.g., `prefix_a`)
- Suffix IDs: `suffix_{name}` (e.g., `suffix_rọ`)

### File Organization

- One prime root per file in `verbs/prime-roots/`
- One auxiliary per file in `verbs/auxiliaries/`
- One prefix per file in `verbs/prefixes/`
- One suffix per file in `verbs/suffixes/`
- Related verb forms can be grouped in files in `verbs/verb-forms/`

## Workflow for Adding Data

### Adding Verb Roots

1. Check if the syllable(s) exist in `syllables.json`
2. Add missing syllables with all three tones
3. Create a new file for the prime root
4. Add verb forms showing usage
5. Link all components using IDs

### Adding Affixes

1. Verify the syllable exists (for prefixes)
2. Create the affix file with appropriate schema
3. Document its grammatical function
4. Create example verb forms using the affix

### Adding Complete Words

1. Ensure all component parts exist
2. Create verb form with all references
3. Include meaning and tense information
4. Verify all IDs resolve correctly

## Quality Checklist

Before submitting a pull request, verify:

- [ ] JSON files are syntactically valid
- [ ] All required schema fields are present
- [ ] IDs follow naming conventions
- [ ] No duplicate IDs exist
- [ ] All ID references resolve to existing entries
- [ ] Tone markings are explicit and correct
- [ ] Unicode characters are used correctly (ọ, ụ, etc.)
- [ ] Meanings are provided for verb forms
- [ ] Changes are documented in commit messages

## Testing Your Contributions

### Validate JSON Syntax

```bash
# Test individual files
python3 -m json.tool language-data/syllables.json > /dev/null

# Test all JSON files
find language-data -name "*.json" -exec python3 -m json.tool {} \; > /dev/null
```

### Check for Duplicate IDs

```bash
# Within a single file
grep -o '"id": "[^"]*"' your-file.json | sort | uniq -d

# Across all files of a type
grep -h '"id":' language-data/verbs/prime-roots/*.json | sort | uniq -d
```

## Pull Request Process

1. **Create a clear title**: "Add verb roots for [ba, da, ga]" or "Fix tone marking in syllables"

2. **Describe your changes**:
   - What you added/changed
   - Why the change was needed
   - Any relevant dictionary sources

3. **Reference issues**: If addressing an issue, mention it: "Closes #123"

4. **Keep PRs focused**: One type of change per PR when possible

5. **Be patient**: Maintainers will review your contribution and may request changes

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the language and data, not personalities
- Welcome newcomers and help them learn

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Spam or off-topic content
- Publishing others' private information

## Sources and References

When adding data, cite your sources:

- Blench Onitsha Igbo Dictionary
- Michael Echeruo Igbo Dictionary
- Northcote Igbo Dictionary
- Other scholarly sources
- Native speaker knowledge (if you are a native speaker)

## Questions?

If you have questions about:
- **Schema**: See `SCHEMA.md`
- **Usage**: See `USAGE_GUIDE.md`
- **Structure**: See `README.md`
- **Other**: Open an issue with the "question" label

## Recognition

Contributors will be acknowledged in the repository. Significant contributions may be highlighted in release notes.

## License

By contributing, you agree that your contributions will be licensed under the same license as this project.

---

## Specific Contribution Opportunities

### High-Priority Needs

1. **Verb Root Expansion**: Add common monosyllabic verb roots
2. **Tense Coverage**: Document verb forms in all tense categories
3. **Noun Development**: Populate the noun categories
4. **Validation Tools**: Create scripts to verify data integrity
5. **Dictionary Mining**: Extract data from PDF dictionaries systematically

### Good First Contributions

- Add 5-10 common verb roots with proper documentation
- Add missing syllables for common consonant-vowel combinations
- Create verb forms for an existing root in multiple tenses
- Fix JSON formatting issues
- Add examples to documentation

### Advanced Contributions

- Develop automated validation scripts
- Create data visualization tools
- Build a web interface for browsing the data
- Implement search functionality
- Develop dictionary import tools

---

Thank you for contributing to the preservation and analysis of the Igbo language!
