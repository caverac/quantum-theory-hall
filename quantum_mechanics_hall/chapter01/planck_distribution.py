"""Problem 1.2: Planck distribution and average energy of a quantum oscillator."""

import logging
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
import numpy.typing as npt

logger = logging.getLogger(__name__)


def average_energy(omega: npt.NDArray[np.float64], beta: float, hbar: float = 1.0) -> npt.NDArray[np.float64]:
    """
    Compute the average energy of a quantum harmonic oscillator.

    Parameters
    ----------
    omega : np.ndarray
        Angular frequency values.
    beta : float
        Inverse temperature (1/kT).
    hbar : float, optional
        Reduced Planck constant, by default 1.0.

    Returns
    -------
    np.ndarray
        Average energy values.
    """
    x = beta * hbar * omega
    # Avoid division by zero for small x
    with np.errstate(divide="ignore", invalid="ignore"):
        result: npt.NDArray[np.float64] = hbar * omega / (np.exp(x) - 1)
        result = np.where(x < 1e-10, 1.0 / beta, result)  # Classical limit
    return np.asarray(result, dtype=np.float64)


def plot_average_energy(path: Path | None = None) -> None:
    """
    Plot average energy vs frequency for different temperatures.

    Parameters
    ----------
    path : Path | None, optional
        Path to save the figure, by default None. If None, the plot is shown instead.
    """
    fig: Figure
    axs: Axes
    fig, axs = plt.subplots(
        1,
        1,
        figsize=(6.5, 5),
        sharex=True,
    )

    fig.subplots_adjust(
        left=0.12,
        right=0.92,
        bottom=0.12,
        top=0.92,
        wspace=0.05,
        hspace=0.05,
    )

    axs.set_xlabel(r"$\hbar\omega / k_B T$")
    axs.set_ylabel(r"$\langle E \rangle / k_B T$")
    axs.set_xscale("log")
    axs.set_yscale("log")
    axs.set_xlim(0.1, 10)
    axs.set_ylim(0.01, 10)

    # configure ticks
    axs.tick_params(which="minor", length=3, color="gray", direction="in")
    axs.tick_params(which="major", length=6, direction="in")
    axs.tick_params(top=True, right=True, which="both")

    # Dimensionless variable: x = beta * hbar * omega = hbar*omega / kT
    x = np.logspace(-1, 1, 500)

    # Quantum result: <E>/(kT) = x / (e^x - 1)
    y_quantum = x / (np.exp(x) - 1)
    axs.plot(x, y_quantum, "-k", lw=2, label="Quantum")

    # Classical limit: <E>/(kT) = 1 (equipartition)
    axs.axhline(y=1, color="gray", ls="--", lw=1.5, label="Classical")

    # Add annotations
    axs.text(0.2, 1.3, "Classical limit", ha="center", va="bottom", fontsize=10, color="gray")

    axs.legend(loc="upper right", frameon=False)

    if path:
        fig.savefig(
            path,
            dpi=150,
            bbox_inches="tight",
            facecolor="white",
            edgecolor="none",
        )
    else:
        plt.show()
