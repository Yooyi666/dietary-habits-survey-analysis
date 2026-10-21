"""Offline checks for published content; does not inspect private source data."""
from pathlib import Path
import base64
import re

root = Path(__file__).resolve().parents[1]
required = [
    'README.md', '.gitignore', '.github/workflows/quality-checks.yml',
    'breakfast_frequency.Rmd', 'lunch_frequency.Rmd',
    'breakfast_report.html', 'lunch_report.html',
    'assets/breakfast_frequency.png', 'assets/lunch_frequency.png',
    'qa/check_breakfast.R', 'qa/check_lunch.R',
    'docs/METHODOLOGY.md', 'docs/REPRODUCIBILITY.md',
    'docs/PORTFOLIO_SUMMARY.md',
]
for rel in required:
    assert (root / rel).is_file(), f'Missing file: {rel}'

for file in root.rglob('*'):
    if not file.is_file() or '.git' in file.parts:
        continue
    assert file.suffix.lower() not in {'.csv', '.xls', '.xlsx', '.rds', '.rdata'}, f'Private dataset: {file}'
    assert not re.search(r'(?i)(?:^|[_-])(?:task[0-9]|project[0-9])', file.name), f'Outdated file name: {file.name}'

for name, label in [('breakfast_report.html', 'Breakfast Frequency by Employment Category'),
                    ('lunch_report.html', 'Lunch Frequency by Gender')]:
    content=(root/name).read_text(encoding='utf-8')
    assert label in content
    assert 'data:image/png;base64,' in content
    assert '107' in content
    assert not re.search(r'(?i)str\s*\(\s*diet\s*\)', content)
    assert content.count('<figure>') == 1

for name in ['assets/breakfast_frequency.png','assets/lunch_frequency.png']:
    assert (root/name).read_bytes().startswith(b'\x89PNG'), f'Invalid PNG: {name}'

for name in ['breakfast_frequency.Rmd', 'lunch_frequency.Rmd']:
    text=(root/name).read_text(encoding='utf-8')
    assert 'survey_data.csv' in text and 'geom_bar(' in text

print('PORTFOLIO QA: PASS (structure, published previews, local-data exclusions)')
