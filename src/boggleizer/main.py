import re
from marisa_trie import Trie

dictionary_path = "csw19.txt"
grid_size = 4 # Assume rows and columns are equal

# Boggle constants
word_min_characters = 3
scores = [0, 0, 0, 1, 1, 2, 3, 5, 11]

# Input board
letters = "abcdefghijklmnop".upper()


"""
Check if a word is long enough and can fit in to the available letters
"""
def word_is_applicable(alphabet: str, word: str) -> bool:
    length_is_correct = len(alphabet) >= len(word) > word_min_characters

    return length_is_correct and all(letter in set(alphabet) for letter in set(word))


"""
Loads the relevant words from a reference dictionary based on available letters
"""
def load_dictionary(dictionary_path: str, alphabet: str) -> tuple[str, int]:
    dictionary = open(dictionary_path).read().splitlines()
    words = set(word for word in dictionary if word_is_applicable(alphabet, word))

    return (words, len(dictionary))


"""
Iterate through all the neighbouring cells
"""
def neighbors(grid_size: tuple[int, int], coordinate: tuple) -> tuple[int, int]:
    rows, columns = grid_size
    x, y = coordinate

    for nx in range(max(0, x - 1), min(x + 2, columns)):
        for ny in range(max(0, y - 1), min(y + 2, rows)):
            yield (nx, ny)


"""
Recursively visit all neighbouring cells and build up words
"""
def iter_cells(dictionary: Trie, grid_size: tuple[int, int], prefix: str, path: tuple):
    if prefix in dictionary:
        yield (prefix, path)

    for (nx, ny) in neighbors(grid_size, path[-1]):
        if (nx, ny) not in path:
            temp_prefix = prefix + grid[ny][nx]
            if dictionary.keys(temp_prefix):
                yield from iter_cells(dictionary, grid_size, temp_prefix, path + ((nx, ny), ))


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
def solve(dictionary: Trie, grid: list[str]) -> list[str]:
    grid_size = (len(grid), len(grid[0]))
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            yield from iter_cells(dictionary, grid_size, letter, ((x, y), ))


words, dictionary_total = load_dictionary(dictionary_path, letters)

print(f"{len(words)} relevant words ({len(words) / dictionary_total:.1%}) loaded, from a total dictionary of {dictionary_total}")

# Generate the board and find solutions
grid = [letters[i : i + grid_size] for i in range(0, len(letters), grid_size)]
solutions = list(solve(Trie(words), grid))

for result in sorted(solutions, key = lambda x: x[0]):
    print(result)

print(f"{len(solutions)} solutions found")
