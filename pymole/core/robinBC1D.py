import numpy as np
from scipy.sparse import csr_matrix

from .grad1D import grad1D


def robinBC1D(k, m, dx, a, b):
    """Computes a m+2 by m+2 one-dimensional mimetic boundary operator that
    imposes a boundary condition of Robin's type

    Arguments:
        k (int): Order of accuracy
        m (int): Number of cells
        dx (float): Step size
        a (float): Dirichlet Coefficient
        b (float): Neumann Coefficient

    Returns:
        :obj:`ndarray` containing discrete boundary operator of Robin's type
    """

    # Check if a & b are non zeros and proceed accordingly

    A = csr_matrix((m + 2, m + 2), dtype=float)
    A[0, 0] = a
    A[-1, -1] = a

    B = csr_matrix((m + 2, m + 1), dtype=float)
    B[0, 0] = -b
    B[-1, -1] = b

    G = grad1D(k, m, dx)

    return A + np.dot(B, G)


if __name__ == "__main__":
    print(robinBC1D(2, 4, 1, 5, 10))
