from solve import solve

dictionary_path = "csw19.txt"
grid_size = 4  # Assume rows and columns are equal

# Boggle constants
word_min_characters = 3
scores = [0, 0, 0, 1, 1, 2, 3, 5, 11]

# Input board
letters = "abcdefghijklmnop".upper()


def word_is_applicable(alphabet: str, word: str) -> bool:
    """
    Check if a word is long enough and can fit in to the available letters
    """
    length_is_correct = len(alphabet) >= len(word) > word_min_characters

    return length_is_correct and all(letter in set(alphabet) for letter in set(word))


def load_dictionary(dictionary_path: str, alphabet: str) -> tuple[set[str], int]:
    """
    Loads the relevant words from a reference dictionary based on available letters
    """
    dictionary = open(dictionary_path).read().splitlines()
    applicable_subset = set(
        word for word in dictionary if word_is_applicable(alphabet, word)
    )

    return (applicable_subset, len(dictionary))


dictionary, dictionary_total = load_dictionary(dictionary_path, letters)

print(
    f"{len(dictionary)} relevant words ({len(dictionary) / dictionary_total:.1%})"
    f" loaded,  from a total dictionary of {dictionary_total}"
)

# Generate the board and find solutions
grid = [letters[i : i + grid_size] for i in range(0, len(letters), grid_size)]
solutions = list(solve(dictionary, grid))

for result in sorted(solutions, key=lambda x: x[0]):
    print(result)

print(f"{len(solutions)} solutions found")
