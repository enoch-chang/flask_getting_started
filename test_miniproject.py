from miniproject import calc_distance
import pytest

def test_calc_distance():

    output_1 = calc_distance([0, 0], [3, 4])
    assert output_1 == 5

    output_2 = calc_distance([0, 0], [5, 12])
    assert output_2 == 13