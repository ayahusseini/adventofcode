import pytest
from day_7 import search


@pytest.mark.parametrize("nums, target", [
    ([15, 6], 156),
    ([6, 8, 6, 15], 7290),
    ([6, 8, 6], 686),
    ([17, 8, 14], 192)
])
def test_search_with_concatenate(nums, target):
    assert search(nums, target, True)
    assert not search(nums, target, False)
