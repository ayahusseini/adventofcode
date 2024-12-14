import pytest
from day_9 import Files


@pytest.fixture
def files():
    return Files.from_line("2333133121414131402")


def test_files_quantity_calculation(files):
    d = files.get_file_quantities()
    assert d[0] == 2
    assert d[1] == 3
    assert d[2] == 1
    assert d[9] == 2
    assert d[8] == 4


def test_files_first_idx(files):
    d = files.get_first_index()
    assert d[0] == 0
    assert d[1] == 5


def test_leftmost_gap(files):
    gaps = files.leftmost_gap(ridx=11, minsize=3)
    assert next(gaps) == range(2, 5)
    assert next(gaps) == range(8, 11)


def test_leftmost_gap_smaller(files):
    gaps = files.leftmost_gap(ridx=11, minsize=2)
    assert next(gaps) == range(2, 4)


def test_files_text(files):
    assert str(files) == "00...111...2...333.44.5555.6666.777.888899"


def test_files_attributes(files):
    assert files.num_filled == len(
        "00...111...2...333.44.5555.6666.777.888899".replace('.', ''))
    print(files.disk)


def test_files_gaps(files):
    assert files.count_gaps() == "00...111...2...333.44.5555.6666.777.888899".count(
        '.')


def test_checksum():
    disk = {}
    for idx, char in enumerate("00992111777.44.333....5555.6666.....8888.."):
        if char != '.':
            disk[idx] = int(char)

    files = Files(disk)
    assert files.checksum() == 2858


def test_checksum_2(files):
    disk = {}
    for idx, char in enumerate("0099811188827773336446555566.............."):
        if char != '.':
            disk[idx] = int(char)

    files = Files(disk)

    assert files.checksum() == 1928
