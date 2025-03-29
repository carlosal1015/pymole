import numpy as np
import pytest

import pymole

# Tolerance for numerical comparisons
TOLERANCE = 1e-10

# Test parameters: orders of accuracy
ORDERS = [2, 4, 6, 8]


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
