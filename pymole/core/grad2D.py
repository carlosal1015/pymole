import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix

from .grad1D import grad1D


def grad2D(k, m, dx, n, dy):
    """Computes a two-dimensional mimetic gradient operator

    Arguments:
        k (int): Order of accuracy
        m (int): Number of cells along x-axis
        dx (float): Step size along x-axis
        n (int): Number of cells along y-axis
        dy (float): Step size along y-axis

    Returns:
        :obj:`ndarray` containing discrete gradient operator
    """

    Gx = grad1D(k, m, dx)
    Gy = grad1D(k, n, dy)

    Im = csr_matrix((m + 2, m), dtype=float)
    In = csr_matrix((n + 2, n), dtype=float)

    Im[1 : m + 1, :] = sparse.eye(m, m, dtype=float, format="csr")
    In[1 : n + 1, :] = sparse.eye(n, n, dtype=float, format="csr")

    Sx = sparse.kron(In.T, Gx, format="csr")
    Sy = sparse.kron(Gy, Im.T, format="csr")

    return sparse.vstack([Sx, Sy], format="csr")


if __name__ == "__main__":
    print(grad2D(2, 5, 1, 6, 1))
