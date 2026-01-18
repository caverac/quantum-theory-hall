"""Generate documentation assets (plots and figures)."""

from pathlib import Path

from quantum_theory_hall.chapter01 import plot_average_energy
from quantum_theory_hall.chapter02 import (
    plot_pendulum,
    plot_pendulum_time,
    plot_potential_energy,
)


def main() -> None:
    """Generate all documentation assets."""
    # Ensure output directory exists
    output_dir = Path("docs/assets/generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Chapter 1
    plot_average_energy(output_dir / "average_energy.png")

    # Chapter 2
    plot_potential_energy(output_dir / "potential_energy.png")
    plot_pendulum(output_dir / "pendulum.png")
    plot_pendulum_time(output_dir / "pendulum_time.png")

    print("Asset generation complete.")


if __name__ == "__main__":
    main()
