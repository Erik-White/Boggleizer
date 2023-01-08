import pytest

from boggleizer.main import word_is_applicable


class TestWordIsApplicable:
    @property
    def alphabet(self):
        return "a, b, c, a, b, c"

    @property
    def min_characters(self):
        return 3

    @pytest.mark.parametrize("word", ["aaa", "aabbcc"])
    def test_character_set_valid(self, word):
        result = word_is_applicable(self.alphabet, self.min_characters, word)

        assert not result

    @pytest.mark.parametrize(
        "word",
        [
            None,
            "000",
            "zzz",
            "abcd",
        ],
    )
    def test_character_set_invalid(self, word):
        result = word_is_applicable(self.alphabet, self.min_characters, word)

        assert not result

    @pytest.mark.parametrize("word", [None, 0, "a", "aabbcc"])
    def test_word_length(self, word):
        result = word_is_applicable(self.alphabet, self.min_characters, word)

        assert not result
