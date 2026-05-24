import sys
from pathlib import Path

sys.path.insert(0, str(Path('rag-policy-assistant').resolve()))
from answer import answer

def test_out_of_stock_answer_has_citation():
    result = answer('What happens if an item is out of stock?')
    assert result['citations']
    assert result['citations'][0]['source'] == 'substitutions.md'

