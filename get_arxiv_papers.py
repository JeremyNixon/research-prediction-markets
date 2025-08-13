import arxiv

import json
from datetime import datetime, date


OUTPUT_FILENAME = 'arxiv_papers.json'
MAX_RESULTS = 100

# Construct query
current_date = (lambda now: f'{now.year}{now.month}{now.day}')(datetime.now())
CUTOFF_DATE = '20250101'
BENCHMARKS = [
    # 'IFEval',
    # 'BBH',
    # 'MATH',
    # 'GPQA',
    # 'MUSR',
    'MMLU',
    'MMLU-PRO',
    # 'AMC23'
    # 'GPQA-DIAMOND',
    # 'AGIEVAL',
    # 'SUPERGPQA',
    # 'HotpotQA',
    # 'DROP',
    # 'HumanEval',
    # 'MBPP',
    # 'GSM8K',
    # 'MATH',
    # 'MATH-500',
    # 'AIME',
    # 'HLE',
]
FULL_QUERY = ''.join([
    # category
    "cat:cs.LG AND ",
    # date
    f"submittedDate:[{CUTOFF_DATE} TO {current_date}] AND ",
    # benchmarks
    " OR ".join(f'abs:{b}' for b in BENCHMARKS),
])

# Fetch results
client = arxiv.Client()
search = arxiv.Search(
    query = FULL_QUERY,
    max_results = MAX_RESULTS,
    sort_by = arxiv.SortCriterion.SubmittedDate,
)
results = client.results(search)


# Convert to JSON
def clean_for_json(obj):
    if isinstance(obj, dict):
        return {k: clean_for_json(v) for k, v in obj.items() if k != "_raw"}
    elif isinstance(obj, list):
        return [clean_for_json(i) for i in obj]
    elif isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif hasattr(obj, '__dict__'):
        return clean_for_json(vars(obj))
    else:
        return obj


papers = [clean_for_json(result) for result in results]
json_output = json.dumps(papers, indent=2)


# Write to disk
with open(OUTPUT_FILENAME, 'w') as f:
    f.write(json_output)
