import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix

from .grad1D import grad1D


def grad3D(k, m, dx, n, dy, o, dz):
    """Computes a three-dimensional mimetic gradient operator

    Arguments:
        k (int): Order of accuracy
        m (int): Number of cells along x-axis
        dx (float): Step size along x-axis
        n (int): Number of cells along y-axis
        dy (float): Step size along y-axis
        o (int): Number of cells along z-axis
        dz (float): Step size along z-axis

    Returns:
        :obj:`ndarray` containing discrete gradient operator
    """

    Gx = grad1D(k, m, dx)
    Gy = grad1D(k, n, dy)
    Gz = grad1D(k, o, dz)

    Im = csr_matrix((m + 2, m), dtype=float)
    In = csr_matrix((n + 2, n), dtype=float)
    Io = csr_matrix((o + 2, o), dtype=float)

    Im[1 : m + 1, :] = sparse.eye(m, m, dtype=float, format="csr")
    In[1 : n + 1, :] = sparse.eye(n, n, dtype=float, format="csr")
    Io[1 : o + 1, :] = sparse.eye(o, o, dtype=float, format="csr")

    Sx = sparse.kron(sparse.kron(Io.T, In.T), Gx)
    Sy = sparse.kron(sparse.kron(Io.T, Gy), Im.T)
    Sz = sparse.kron(sparse.kron(Gz, In.T), Im.T)

    return sparse.vstack([Sx, Sy, Sz], format="csr")


if __name__ == "__main__":
    print(grad3D(2, 5, 1, 6, 1, 7, 1))
