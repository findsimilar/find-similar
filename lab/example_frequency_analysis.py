"""
Get one example and make frequency analysis
"""
import sys

sys.path.append("../")

from find_similar.examples.analyze import frequency_analysis  # pylint: disable=wrong-import-position


try:
    _, example_name = sys.argv  # pylint: disable=unbalanced-tuple-unpacking
# TODO: except more concrete exception
except Exception:  # pylint: disable=broad-exception-caught
    print(
        "Please specify an example name"
    )
    sys.exit(0)

print(frequency_analysis(example_name))
