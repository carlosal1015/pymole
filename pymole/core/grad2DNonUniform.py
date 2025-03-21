import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix

from .grad1DNonUniform import grad1DNonUniform


def grad2DNonUniform(k, xticks, yticks):
    """Returns a two-dimensional non-uniform mimetic gradient operator

    Arguments:
        k (int): Order of accuracy
        xticks (:obj:`ndarray`): Centers' ticks (x-axis)
        yticks (:obj:`ndarray`): Centers' ticks (y-axis)
                                 (including the boundaries!)

    Returns:
        :obj:`ndarray` containing discrete gradient operator
    """

    Gx = grad1DNonUniform(k, xticks)
    Gy = grad1DNonUniform(k, yticks)

    m = Gx.shape[0] - 1
    n = Gy.shape[0] - 1

    Im = csr_matrix((m + 2, m), dtype=float)
    In = csr_matrix((n + 2, n), dtype=float)

    Im[1 : m + 1, :] = sparse.eye(m, m, dtype=float, format="csr")
    In[1 : n + 1, :] = sparse.eye(n, n, dtype=float, format="csr")

    Sx = sparse.kron(In.T, Gx, format="csr")
    Sy = sparse.kron(Gy, Im.T, format="csr")

    return sparse.vstack([Sx, Sy], format="csr")


if __name__ == "__main__":
    xticks = np.array([0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.45])
    yticks = np.array([0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.45, 0.5])
    print(grad2DNonUniform(2, xticks, yticks))
