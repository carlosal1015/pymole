import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix

from .interpolD1D import interpolD1D


def interpolD3D(m, n, o, c1, c2, c3):
    """Computes a three-dimensional interpolator of 2nd-order

    Arguments:
        m (int): Number of cells along x-axis
        n (int): Number of cells along y-axis
        o (int): Number of cells along z-axis
        c1 (float): Left interpolation coeff.
        c2 (float): Bottom interpolation coeff.
        c3 (float): Front interpolation coeff.

    Returns:
        :obj:`ndarray` containing coefficients of interpolator
    """

    Ix = interpolD1D(m, c1)
    Iy = interpolD1D(n, c2)
    Iz = interpolD1D(o, c3)

    Im = csr_matrix((m + 2, m), dtype=float)
    In = csr_matrix((n + 2, n), dtype=float)
    Io = csr_matrix((o + 2, o), dtype=float)

    Im[1 : m + 1, :] = sparse.eye(m, m, dtype=float, format="csr")
    In[1 : n + 1, :] = sparse.eye(n, n, dtype=float, format="csr")
    Io[1 : o + 1, :] = sparse.eye(o, o, dtype=float, format="csr")

    Sx = sparse.kron(sparse.kron(Io, In), Ix)
    Sy = sparse.kron(sparse.kron(Io, Iy), Im)
    Sz = sparse.kron(sparse.kron(Iz, In), Im)

    return sparse.hstack([Sx, Sy, Sz], format="csr")


if __name__ == "__main__":
    print(interpolD3D(5, 6, 7, 0.5, 0.5, 0.5))
