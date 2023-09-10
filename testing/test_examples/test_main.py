"""
Test examples/main.py
"""
import pytest
from find_similar.examples import examples_set, get_example


EXISTING_EXAMPLES = {
    'films-demo'
}


def test_examples_set(mock_example_name):
    """
    Test examples_set
    """
    expected_set = EXISTING_EXAMPLES.union({mock_example_name})
    assert examples_set() == expected_set


def test_get_example(mock_example_name):
    """
    Test get_example
    """
    example = get_example(mock_example_name)
    assert isinstance(example, dict)
    assert 'text' in example
    assert 'texts' in example
    assert example['text'] == 'Mock'
    assert example['texts'] == ['Mock example', 'This is for tests']


def test_get_example_wrong_name():
    """
    Test get_example with wrong name
    """
    with pytest.raises(FileNotFoundError):
        get_example('wrong_name')
