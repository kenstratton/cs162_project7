import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from vege_learning.classes import *

def test_class_inheritance():
    tomato = Tomato()
    watermellon = Watermellon()

    # Whether inheritance relationships are established
    assert issubclass(Tomato, Vegetable)
    assert issubclass(Watermellon, Vegetable)
    # Whether each sub class shows polymorphism 
    assert str(tomato) == "Tomato"
    assert str(watermellon) == "Watermellon"