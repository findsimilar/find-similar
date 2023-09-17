"""
Functions to analyze examples
"""
from find_similar.examples import get_example


def sort_results(results):
    """
    Sort results by value
    :results: dict
    """
    return tuple(
        (
            result for result in sorted(
                results.items(), reverse=True, key=lambda item: item[1]
            )
        )
    )


def frequency_analysis(example_name):
    """
    Frequency analysis for example
    :example_name: Example name
    """
    example = get_example(example_name)
    text_list = example['texts']
    result = {}
    for text in text_list:
        text = text.replace('.', '').replace(',', '')
        words = text.split()
        for word in words:
            word = word.lower()
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return sort_results(result)
