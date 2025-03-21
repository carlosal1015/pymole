import numpy as np
from scipy.sparse import csr_matrix


def interpolD1D(m, c):
    """Computes a m+2 by m+1 one-dimensional interpolator of 2nd-order

    Arguments:
        m (int): Number of cells
        c (float): Left interpolation coeff.

    Returns:
        :obj:`ndarray` containing coefficients of interpolator
    """

    assert m >= 4, "m must be >= 4, given: {}".format(m)
    assert (c >= 0) and (c <= 1), "0 <= c <= 1, given: {}".format(c)

    """
    Dimensions of I
    """
    n_rows = m + 2
    n_cols = m + 1

    I = csr_matrix((n_rows, n_cols), dtype=float)

    I[0, 0] = 1.0
    I[-1, -1] = 1.0

    """
    Average between two continuous cells
    """
    avg = np.array([c, 1.0 - c], dtype=float)

    j = 0
    for i in range(1, n_cols):
        I[i, j : j + 2] = avg
        j = j + 1

    return I


if __name__ == "__main__":
    print(interpolD1D(5, 0.5))
