from __future__ import annotations  # Direct use of types is allowed in Python >= 3.9
from typing import Generator

from marisa_trie import Trie


def solve(dictionary: set[str], grid: list[str]) -> Generator[str, None, None]:
    return _solve(Trie(dictionary), grid)


def _solve(dictionary: Trie, grid: list[str]) -> Generator[str, None, None]:
    """
    Find solutions along with their coordinates.
    Results are generated with row, column coordinates i.e.

    0 1 2 3 x
    0 A B C D
    1 E F G H
    2 I J K L
    3 M N O P
    y
    """
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            yield from _iter_cells(dictionary, grid, letter, ((x, y),))


def _iter_cells(dictionary: Trie, grid: list[str], prefix: str, path: tuple):
    """
    Recursively visit all neighbouring cells and build up words
    """
    if prefix in dictionary:
        yield (prefix, path)

    grid_size = (len(grid), len(grid[0]))

    for (nx, ny) in _neighbors(grid_size, path[-1]):
        if (nx, ny) not in path:
            temp_prefix = prefix + grid[ny][nx]
            if dictionary.keys(temp_prefix):
                yield from _iter_cells(
                    dictionary, grid, temp_prefix, path + ((nx, ny),)
                )


def _neighbors(
    grid_size: tuple[int, int], coordinate: tuple
) -> Generator[tuple[int, int], None, None]:
    """
    Iterate through all the neighbouring cells
    """
    rows, columns = grid_size
    x, y = coordinate

    for nx in range(max(0, x - 1), min(x + 2, columns)):
        for ny in range(max(0, y - 1), min(y + 2, rows)):
            yield (nx, ny)
