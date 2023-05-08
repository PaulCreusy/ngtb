import numpy as np
import pyximport
pyximport.install()
from basics import find_first

def compute_reduce_cost(d_J, d_I, A_I_invert, A_J):
    return d_J - A_J.T @ A_I_invert.T @ d_I

def extract_for_iteration(c, L, I, J):
    A_I = L[:, I]
    A_J = L[:, J]
    d_J = c[J, :]
    d_I = c[I, :]
    return A_I, A_J, d_J, d_I


def simplex(c: np.array, L: np.array, b: np.array, x0: np.array):
    # Initialize I and J
    I = np.where(x0 != 0)[0]
    J = np.array([i for i in range(len(c)) if not(i in I)])
    x = x0

    # Compute the reduce cost of the first iteration
    A_I, A_J, d_J, d_I = extract_for_iteration(c, L, I, J)
    A_I_invert = np.linalg.inv(A_I)

    r = compute_reduce_cost(d_J, d_I, A_I_invert, A_J)

    while not((r >= 0).all()):
        # Choose j applying Bland rule
        j = J[find_first(r, lambda x: x < 0)]

        # Extract a_j
        a_j = L[:, [j]]
        print("a_j", a_j)

        # Compute delta_j
        delta_j = A_I_invert @ a_j

        print("delta_j", delta_j)

        # Detect if the problem is bounded
        if (delta_j <= 0).all():
            raise ValueError("The problem is unbounded.")

        # Extract I_j
        I_j = np.where(delta_j > 0)[0]
        print("I_j", I[I_j])

        z = x[I[I_j], :] / delta_j
        i_j = np.argmin(z)
        print("z", z)
        print("i_j", I[i_j])
        z_j = z[i_j]

        x[I] = x[I] - z_j * delta_j
        x[j] = z[i_j]
        print("x", x)

        I = np.array([i for i in I if i != I[i_j]] + [J[j]])
        print("I", I)

        J = np.array([i for i in range(len(c)) if not(i in I)])
        print("J", J)

        # Compute matrixes needed for the iteration
        A_I, A_J, d_J, d_I = extract_for_iteration(c, L, I, J)
        print("A_I", A_I)
        A_I_invert = np.linalg.inv(A_I)
        print("A_I invert", A_I_invert)

        # Update reduce cost
        r = compute_reduce_cost(d_J, d_I, A_I_invert, A_J)
        print("r", r)
        print("\n------------------\n")

    return x
