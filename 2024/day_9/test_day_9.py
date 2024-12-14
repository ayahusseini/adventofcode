import pytest
from day_9 import Files


@pytest.fixture
def files():
    return Files.from_line("2333133121414131402")


def test_files_text(files):
    assert files.disk_space == "00...111...2...333.44.5555.6666.777.888899"


def test_checksum():
    files = Files("0099811188827773336446555566..............")
    assert files.checksum() == 1928


def test_checksum_2():
    files = Files("00992111777.44.333....5555.6666.....8888..")
    assert files.checksum() == 2858
