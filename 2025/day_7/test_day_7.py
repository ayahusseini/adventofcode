import numpy as np
import pytest

from day_7 import TEST_FILE, load_file, is_diag, get_next_to_splitter


@pytest.fixture
def mock_input():
    return load_file(TEST_FILE)


@pytest.mark.parametrize(
    "arr, expected",
    [
        # 1. No splitters
        (np.array([[False, False, False]]), np.array([[0, 0, 0]])),
        # 2. Single splitter in the middle
        (np.array([[False, True, False]]), np.array([[1, 0, 1]])),
        # 3. Splitter at start
        (np.array([True, False, False]), np.array([[0, 1, 0]])),
        # 4. Splitter at end
        (np.array([[False, False, True]]), np.array([[0, 1, 0]])),
        # 5. Two separated splitters
        (np.array([[True, False, True, False]]), np.array([[0, 1, 0, 1]])),
        # 6. Adjacent splitters
        (np.array([[True, True, False]]), np.array([[0, 0, 1]])),
        # 7. Multiple splitters in larger array
        (
            np.array([[False, True, False, True, False, False, True]]),
            np.array([[1, 0, 1, 0, 1, 1, 0]]),
        ),
        # 8. Multiple splitters in multi-row array
        (
            np.array([[0, 0, 1], [1, 1, 0], [1, 1, 1], [1, 0, 1]]),
            np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 1, 0]]),
        ),
    ],
)
def test_get_next_to_splitter(arr, expected):
    result = get_next_to_splitter(arr)
    np.testing.assert_array_equal(result, expected)


@pytest.mark.parametrize(
    "idx1, idx2, expected",
    [
        # True cases (direct diagonal)
        ((0, 0), (1, 1), True),
        ((1, 1), (0, 0), True),
        ((5, 3), (4, 2), True),
        ((2, 7), (3, 6), True),
        ((0, 0), (-1, 1), True),
        ((0, 0), (1, -1), True),
        ((0, 0), (-1, -1), True),
        # False cases – same row or same column
        ((0, 0), (0, 1), False),
        ((3, 3), (4, 3), False),
        ((5, 5), (5, 5), False),
        # False cases – diagonal but not *directly* (distance > 1)
        ((0, 0), (2, 2), False),
        ((4, 4), (6, 6), False),
        # False cases – only one coordinate differs by 1
        ((1, 1), (2, 3), False),
        ((3, 5), (4, 7), False),
    ],
)
def test_is_diag(idx1, idx2, expected):
    assert is_diag(idx1, idx2) == expected
