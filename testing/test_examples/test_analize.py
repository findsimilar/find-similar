"""
Test for analyze examples
"""
from find_similar.examples.analyze import frequency_analysis, sort_results


def test_frequency_analysis():
    """
    Test frequency_analysis
    """
    frequency = frequency_analysis('mock')
    assert isinstance(frequency, tuple)
    excepted_result = (
        ('mock', 2),
        ('example', 2),
        ('for', 2),
        ('tests', 2),
        ('this', 1),
        ('is', 1),
    )
    assert frequency == excepted_result


def test_sort_results():
    """
    Test sort_results
    """
    results = {
        'one': 1,
        'three': 3,
        'two': 2,
    }
    results = sort_results(results)
    assert isinstance(results, tuple)

    excepted_result = (
        ('three', 3),
        ('two', 2),
        ('one', 1),
    )

    assert results == excepted_result
