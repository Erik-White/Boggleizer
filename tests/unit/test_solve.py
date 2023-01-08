import pytest

from boggleizer.solve import solve, _neighbors


class TestSolve:
    @property
    def dictionary(self):
        return ["test", "astute"]

    @property
    def grid(self):
        return ["abcd", "stuv", "teop", "kjhd"]

    def test_solve(self):
        results = list(solve(self.dictionary, self.grid))

        assert len(results) == len(self.dictionary)
        for result in results:
            assert result[0] in self.dictionary


class TestNeighbours:
    @property
    def grid_size(self):
        return (3, 3)

    def test_neighbours_coordinates(
        self,
    ):
        result = list(_neighbors(self.grid_size, (0, 0)))

        assert result == [(0, 0), (0, 1), (1, 0), (1, 1)]

    @pytest.mark.parametrize(
        "coordinate, expected_neighbours", [((0, 0), 4), ((1, 1), 9), ((1, 2), 6)]
    )
    def test_neighbours_count(self, coordinate, expected_neighbours):
        result = list(_neighbors(self.grid_size, coordinate))

        assert len(result) == expected_neighbours
