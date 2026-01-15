"""Generate documentation assets (plots and figures)."""

from pathlib import Path

from quantum_mechanics_hall.chapter01 import plot_average_energy


def main() -> None:
    """Generate all documentation assets."""
    # Ensure output directory exists
    output_dir = Path("docs/assets/generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Chapter 1
    plot_average_energy(output_dir / "average_energy.png")

    print("Asset generation complete.")


if __name__ == "__main__":
    main()
