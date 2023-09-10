"""
Conftest for test_examples
"""
import pytest


@pytest.fixture
def mock_example_name():
    """
    Fixture for mock example filename
    """
    return 'mock'
