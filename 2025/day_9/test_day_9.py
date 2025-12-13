import pytest

from day_9 import load_file, TEST_FILE


def test_load():
    """Test that we can load the test file."""
    data = load_file(TEST_FILE)
    assert len(data) > 0
