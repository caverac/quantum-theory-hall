"""Numerical integration of pendulum swing time."""

from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np
from scipy import integrate

from quantum_theory_hall.utils.assets import register_asset, save_figure_if_changed


def omega_t(delta: float, theta_0: float) -> float:
    """
    Compute omega * t(delta) by numerical integration.

    The time for the pendulum to swing from theta(0) = pi - delta to theta_0 is:

    t(delta) = (1 / sqrt(2) * omega) * integral_{theta_0}^{pi - delta} dtheta / sqrt(cos(theta) + cos(delta))

    So omega * t(delta) = (1 / sqrt(2)) * integral_{theta_0}^{pi - delta} dtheta / sqrt(cos(theta) + cos(delta))

    Parameters
    ----------
    delta : float
        Initial angle from the upward vertical (in radians).
    theta_0 : float
        Final angle from the downward vertical (in radians).

    Returns
    -------
    float
        The dimensionless quantity omega * t(delta).
    """
    if delta <= 0:
        return np.inf

    def integrand(theta: float) -> float:
        val = np.cos(theta) + np.cos(delta)
        if val <= 0:  # pragma: no cover
            return np.inf
        return 1.0 / float(np.sqrt(val))

    lower = theta_0
    upper = np.pi - delta

    if upper <= lower:
        return 0.0

    result, _ = integrate.quad(integrand, lower, upper)
    return result / float(np.sqrt(2))


@register_asset("pendulum_time.png")
def plot_pendulum_time(*, path: Path | None = None) -> None:
    """
    Plot omega * t(delta) vs delta for different values of theta_0.

    Parameters
    ----------
    path : Path | None, optional
        Path to save the figure, by default None. If None, the plot is shown instead.
    """
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(1, 1, figsize=(6.5, 5))

    fig.subplots_adjust(
        left=0.12,
        right=0.92,
        bottom=0.12,
        top=0.92,
    )

    # Different values of theta_0
    theta_0_values = [np.pi / 6, np.pi / 4, np.pi / 3]
    labels = [r"$\theta_0 = \pi/6$", r"$\theta_0 = \pi/4$", r"$\theta_0 = \pi/3$"]
    colors = ["black", "blue", "red"]
    styles = ["-", "--", "-."]

    # Delta values: constrained to delta < pi/4, use log spacing for better resolution near 0
    delta_values = np.logspace(-3, np.log10(np.pi / 4 - 0.01), 200)

    for theta_0, label, color, style in zip(theta_0_values, labels, colors, styles):
        omega_t_values = [omega_t(d, theta_0) for d in delta_values]
        ax.plot(delta_values, omega_t_values, style, color=color, lw=2, label=label)

    # Reference line: ln(1/delta)
    ln_ref = np.log(1.0 / delta_values)
    ax.plot(delta_values, ln_ref, ":", color="gray", lw=1.5, label=r"$\ln(1/\delta)$")

    ax.set_xlabel(r"$\delta$")
    ax.set_ylabel(r"$\omega t(\delta)$")
    ax.set_xscale("log")
    ax.set_xlim(1e-3, np.pi / 4)
    ax.set_ylim(0, 10)

    # Configure ticks
    ax.tick_params(which="minor", length=3, color="gray", direction="in")
    ax.tick_params(which="major", length=6, direction="in")
    ax.tick_params(top=True, right=True, which="both")

    ax.legend(loc="upper right", frameon=False)

    if path:
        save_figure_if_changed(
            fig,
            path,
            dpi=150,
            bbox_inches="tight",
            facecolor="white",
            edgecolor="none",
        )
        plt.close(fig)
    else:
        plt.show()
