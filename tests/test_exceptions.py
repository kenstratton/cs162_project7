import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from vege_learning.exceptions import *
from vege_learning.classes import *

def test_exceptions():
    tomato = Tomato()
    papper = Papper()
    temp_error = TempError(tomato, papper.best_temp)
    water_error = WaterPercentError(tomato, papper.best_temp)

    # Whether exceptions react to an irregular input
    with pytest.raises(TempError):
        evaluate_temp(tomato, papper.best_temp)
    with pytest.raises(WaterPercentError):
        evaluate_water(tomato, papper.water)

    # Whether exceptions output expectedly
    assert handle_temp_error(tomato, papper.best_temp) == temp_error.message
    assert handle_water_error(tomato, papper.best_temp) == water_error.message