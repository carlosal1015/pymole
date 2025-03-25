import pytest
import pymole
import numpy as np

TOLERANCE = 1e-10

ORDERS = [2, 4, 6, 8]


def test_pymole():
    assert pymole.add_one(1) == 2
