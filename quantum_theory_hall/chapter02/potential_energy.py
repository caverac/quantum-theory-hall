"""Potential energy illustrations for classical mechanics concepts."""

from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np

from quantum_theory_hall.utils.assets import register_asset, save_figure_if_changed


@register_asset("potential_energy.png")
def plot_potential_energy(*, path: Path | None = None) -> None:
    """
    Plot an arbitrary potential energy V(x) illustrating the classical turning points.

    Shows a potential well where V(x) < E0 for x in [x0, x1], demonstrating
    the classically allowed region for a particle with energy E0.

    Parameters
    ----------
    path : Path | None, optional
        Path to save the figure, by default None. If None, the plot is shown instead.
    """
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(1, 1, figsize=(6.5, 4.5))

    # Create an arbitrary potential with a well shape
    x = np.linspace(-1.5, 2.0, 500)

    # Arbitrary potential: combination of polynomial terms for an asymmetric well
    V = 0.3 * (x + 0.5) ** 4 - 1.2 * (x + 0.5) ** 2 + 0.10 * (x + 0.5) ** 3 + 1.0

    # Energy level E0 that intersects the potential at two points
    E0 = 1.10

    # Plot the potential
    ax.plot(x, V, "k-", lw=2)

    # Plot the energy level E0
    ax.axhline(y=E0, color="gray", ls="--", lw=1.5)

    # Mark x0 and x1 on the x-axis (inside the allowed region)
    ymin = -0.2
    x0 = -1.2
    x1 = 1.2
    ax.plot([x0, x0], [ymin, E0], color="gray", ls="--", lw=1)
    ax.plot([x1, x1], [ymin, E0], color="gray", ls="--", lw=1)

    # Labels
    ax.text(
        x0,
        ymin - 0.02,
        r"$x_0$",
        ha="center",
        va="top",
    )
    ax.text(
        x1,
        ymin - 0.02,
        r"$x_1$",
        ha="center",
        va="top",
    )
    ax.text(
        2.0,
        E0 + 0.05,
        r"$E_0$",
        ha="left",
        va="bottom",
    )
    ax.text(
        1.5,
        1.5,
        r"$V(x)$",
        ha="left",
        va="bottom",
    )

    # Axis labels
    ax.set_xlabel(
        r"$x$",
    )
    ax.set_ylabel(
        "Energy",
    )

    # Remove numbered ticks, keep axis lines
    ax.set_xticks([])
    ax.set_yticks([])

    # Set axis limits
    ax.set_xlim(-1.5, 2.0)
    ax.set_ylim(ymin, 1.6)

    # Remove top and right spines for cleaner look
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    if path:
        save_figure_if_changed(
            fig,
            path,
            dpi=150,
            facecolor="white",
            edgecolor="none",
        )
        plt.close(fig)
    else:
        plt.show()
