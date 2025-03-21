import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix

from .interpol1D import interpol1D


def interpol3D(m, n, o, c1, c2, c3):
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

    Ix = interpol1D(m, c1)
    Iy = interpol1D(n, c2)
    Iz = interpol1D(o, c3)

    Im = csr_matrix((m + 2, m), dtype=float)
    In = csr_matrix((n + 2, n), dtype=float)
    Io = csr_matrix((o + 2, o), dtype=float)

    Im[1 : m + 1, :] = sparse.eye(m, m, dtype=float, format="csr")
    In[1 : n + 1, :] = sparse.eye(n, n, dtype=float, format="csr")
    Io[1 : o + 1, :] = sparse.eye(o, o, dtype=float, format="csr")

    Sx = sparse.kron(sparse.kron(Io.T, In.T), Ix)
    Sy = sparse.kron(sparse.kron(Io.T, Iy), Im.T)
    Sz = sparse.kron(sparse.kron(Iz, In.T), Im.T)

    return sparse.vstack([Sx, Sy, Sz], format="csr")


if __name__ == "__main__":
    print(interpol3D(5, 6, 7, 0.5, 0.5, 0.5))
