import pytest
from day_3 import extract_multiplication_instructions


@pytest.mark.parametrize("line,instructions", [
    ("xmul(2,4)%&mul[3,7]!@ ^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
     [("2", "4"), ('5', '5'), ('11', '8'), ('8', '5')]),
    ("mul(a,b)", []),
    ("mul(11,20)", [('11', '20')])
])
def test_find_mul_instructions(line, instructions):
    assert extract_multiplication_instructions(line) == instructions
