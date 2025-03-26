import numpy as np
import pytest

import pymole

# Tolerance for numerical comparisons
TOLERANCE = 1e-10

# Test parameters: orders of accuracy
ORDERS = [2, 4, 6, 8]


def test_pymole():
    assert pymole.add_one(1) == 2


@pytest.mark.parametrize("k", ORDERS)
def test_divergence_nullity(k):
    # Determine grid size and spacing
    m = 2 * k + 1
    dx = 1.0 / m

    # Create the 1D divergence operator
    D = pymole.core.div1D(k, m, dx)

    field = np.ones(m + 1)
    divergence = D @ field
    norm = np.linalg.norm(divergence)

    assert norm < TOLERANCE, f"Divergence test failed for k={k}"


@pytest.mark.parametrize("k", ORDERS)
def test_gradient_nullity(k):
    # Determine grid size and spacing
    m = 2 * k + 1
    dx = 1.0 / m

    # Create the 1D gradient operator
    G = pymole.core.grad1D(k, m, dx)

    field = np.ones(m + 2)
    gradient = G @ field
    norm = np.linalg.norm(gradient)

    assert norm < TOLERANCE, f"Gradient nullity test failed for k={k}"
