import numpy as np
import pytest

import pymole

# Tolerance for numerical comparisons
TOLERANCE = 1e-10

# Test parameters: orders of accuracy
ORDERS = [2, 4, 6]


@pytest.mark.parametrize("k", ORDERS)
def test_laplacian_nullity(k):
    # Determine grid size and spacing
    m = 2 * k + 1
    dx = 1.0 / m

    # Create the 1D Laplacian operator
    L = pymole.core.lap1D(k, m, dx)
    field = np.ones(m + 2)
    laplacian = L @ field
    norm = np.linalg.norm(laplacian)

    assert norm < TOLERANCE, f"Laplacian nullity test failed for k={k}"
