"""Pendulum sketch for classical mechanics illustrations."""

from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.patches import Arc, Circle, Wedge
import numpy as np

from quantum_theory_hall.utils.assets import register_asset, save_figure_if_changed


@register_asset("pendulum.png")
def plot_pendulum(*, path: Path | None = None) -> None:
    """
    Plot a pendulum sketch showing angles delta and theta_0.

    Shows:
    - A circle indicating the pendulum's path
    - Angle delta measured from vertical (y+)
    - Angle theta_0 measured from vertical (y-)
    - The region between delta and theta_0 filled with light blue

    Parameters
    ----------
    path : Path | None, optional
        Path to save the figure, by default None. If None, the plot is shown instead.
    """
    fig: Figure
    ax: Axes
    fig, ax = plt.subplots(1, 1, figsize=(4, 4))

    # Pendulum parameters
    L = 1.0  # Length of pendulum
    pivot = (0, 0)  # Pivot point at origin

    # Angles (in degrees for matplotlib)
    delta_deg = 30
    theta_0_deg = 45

    # Draw the circular path of the pendulum
    circle = Circle(pivot, L, fill=False, color="black", linestyle="-", linewidth=1.5)
    ax.add_patch(circle)

    # Draw the vertical reference lines
    # y+ (upward)
    ax.plot([0, 0], [0, L * 1.15], "k--", lw=1)
    # y- (downward)
    ax.plot([0, 0], [0, -L * 1.15], "k--", lw=1)

    # Fill the region between delta and theta_0
    angle_delta_std = 90 - delta_deg
    angle_theta0_std = -90 + theta_0_deg

    # Create a wedge to fill the region
    wedge = Wedge(
        pivot,
        L,
        angle_theta0_std,
        angle_delta_std,
        facecolor="lightblue",
        edgecolor="none",
        alpha=0.5,
    )
    ax.add_patch(wedge)

    # Draw the pendulum positions
    x_delta = L * np.sin(np.radians(delta_deg))
    y_delta = L * np.cos(np.radians(delta_deg))
    ax.plot([0, x_delta], [0, y_delta], "k-", lw=2)
    ax.plot(x_delta, y_delta, "ko", markersize=10)

    # Position at theta_0 (from y-)
    x_theta0 = L * np.sin(np.radians(theta_0_deg))
    y_theta0 = -L * np.cos(np.radians(theta_0_deg))
    ax.plot([0, x_theta0], [0, y_theta0], "k-", lw=2)
    ax.plot(x_theta0, y_theta0, "ko", markersize=10)

    # Draw angle arcs with arrows
    arc_r_delta = 0.4
    arc_delta = Arc(
        pivot,
        arc_r_delta,
        arc_r_delta,
        angle=0,
        theta1=90 - delta_deg,
        theta2=90,
        color="black",
        lw=1.5,
    )
    ax.add_patch(arc_delta)

    # Arrow at end of delta arc (pointing clockwise, toward smaller angle)
    delta_end_angle = np.radians(90 - delta_deg)
    arrow_delta_x = (arc_r_delta / 2) * np.cos(delta_end_angle)
    arrow_delta_y = (arc_r_delta / 2) * np.sin(delta_end_angle)
    # Tangent direction (clockwise = negative angular direction)
    arrow_delta_dx = np.sin(delta_end_angle) * 0.06
    arrow_delta_dy = -np.cos(delta_end_angle) * 0.06
    ax.annotate(
        "",
        xy=(arrow_delta_x + arrow_delta_dx, arrow_delta_y + arrow_delta_dy),
        xytext=(arrow_delta_x, arrow_delta_y),
        arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 1.5},
    )

    # Arc for theta_0 (from y-)
    arc_r_theta0 = 0.3
    arc_theta0 = Arc(
        pivot,
        arc_r_theta0,
        arc_r_theta0,
        angle=0,
        theta1=-90,
        theta2=-90 + theta_0_deg,
        color="black",
        lw=1.5,
    )
    ax.add_patch(arc_theta0)

    # Arrow at end of theta_0 arc (pointing counterclockwise, toward larger angle)
    theta0_end_angle = np.radians(-90 + theta_0_deg)
    arrow_theta0_x = (arc_r_theta0 / 2) * np.cos(theta0_end_angle)
    arrow_theta0_y = (arc_r_theta0 / 2) * np.sin(theta0_end_angle)
    # Tangent direction (counterclockwise = positive angular direction)
    arrow_theta0_dx = -np.sin(theta0_end_angle) * 0.06
    arrow_theta0_dy = np.cos(theta0_end_angle) * 0.06
    ax.annotate(
        "",
        xy=(arrow_theta0_x + arrow_theta0_dx, arrow_theta0_y + arrow_theta0_dy),
        xytext=(arrow_theta0_x, arrow_theta0_y),
        arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 1.5},
    )

    # Arc for theta(0) = pi - delta (from y- to delta position)
    # This spans from -90 degrees to (90 - delta_deg) in standard coords
    arc_r_theta_init = 0.7
    arc_theta_init = Arc(
        pivot,
        arc_r_theta_init,
        arc_r_theta_init,
        angle=0,
        theta1=-90,
        theta2=90 - delta_deg,
        color="black",
        lw=1.5,
    )
    ax.add_patch(arc_theta_init)

    # Arrow at end of theta(0) arc
    theta_init_end_angle = np.radians(90 - delta_deg)
    arrow_theta_init_x = (arc_r_theta_init / 2) * np.cos(theta_init_end_angle)
    arrow_theta_init_y = (arc_r_theta_init / 2) * np.sin(theta_init_end_angle)
    arrow_theta_init_dx = -np.sin(theta_init_end_angle) * 0.06
    arrow_theta_init_dy = np.cos(theta_init_end_angle) * 0.06
    ax.annotate(
        "",
        xy=(arrow_theta_init_x + arrow_theta_init_dx, arrow_theta_init_y + arrow_theta_init_dy),
        xytext=(arrow_theta_init_x, arrow_theta_init_y),
        arrowprops={"arrowstyle": "-|>", "color": "black", "lw": 1.5},
    )

    # Labels
    # Delta label
    ax.text(
        0.15,
        0.35,
        r"$\delta$",
        ha="center",
        va="center",
    )

    # Theta_0 label
    ax.text(
        0.12,
        -0.22,
        r"$\theta_0$",
        ha="center",
        va="center",
    )

    # y label
    ax.text(
        0.08,
        L * 1.1,
        r"$y$",
        ha="left",
        va="center",
    )
    # theta(0) = pi - delta label (next to its arc)
    ax.text(
        0.35,
        0.05,
        r"$\theta(0) = \pi - \delta$",
        ha="left",
        va="center",
    )

    # Mark the pivot point
    ax.plot(0, 0, "ko", markersize=6)

    # Set equal aspect ratio and limits
    ax.set_aspect("equal")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)

    # Remove axes
    ax.axis("off")

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
