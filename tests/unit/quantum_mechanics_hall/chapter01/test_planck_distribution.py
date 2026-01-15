"""Unit tests for Planck distribution and average energy functionality."""

from pathlib import Path
from unittest.mock import MagicMock, patch

from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np

from quantum_mechanics_hall.chapter01.planck_distribution import (
    average_energy,
    plot_average_energy,
)


class TestAverageEnergy:
    """Test cases for average_energy function."""

    def test_average_energy_formula(self) -> None:
        """Test that the formula is correctly implemented."""
        omega = np.array([1.0, 2.0])
        beta = 0.5
        hbar = 1.0
        result = average_energy(omega, beta, hbar)

        # <E> = hbar*omega / (exp(beta*hbar*omega) - 1)
        x = beta * hbar * omega
        expected = hbar * omega / (np.exp(x) - 1)

        assert np.allclose(result, expected)
        assert np.all(np.isfinite(result))
        assert np.all(result > 0)

    def test_average_energy_classical_limit(self) -> None:
        """Test classical limit for small beta*hbar*omega."""
        omega = np.array([1e-12])
        beta = 1.0
        result = average_energy(omega, beta)
        expected = 1.0 / beta  # Classical limit: kT
        assert np.isclose(result[0], expected, rtol=1e-5)


class TestPlotAverageEnergy:
    """Test cases for plot_average_energy function."""

    def _create_mock_axes(self) -> MagicMock:
        """Create a properly mocked axes object."""
        mock_ax = MagicMock(spec=Axes)
        mock_ax.xaxis = MagicMock()
        mock_ax.yaxis = MagicMock()
        return mock_ax

    def test_plot_saves_figure(self) -> None:
        """Test that the figure is saved when path is provided."""
        with patch("matplotlib.pyplot.subplots") as mock_subplots:
            mock_fig = MagicMock(spec=Figure)
            mock_subplots.return_value = (mock_fig, self._create_mock_axes())

            output_path = Path("test_output.png")
            plot_average_energy(output_path)

            mock_fig.savefig.assert_called_once()

    def test_plot_shows_figure(self) -> None:
        """Test that the figure is shown when no path is provided."""
        with (
            patch("matplotlib.pyplot.subplots") as mock_subplots,
            patch("quantum_mechanics_hall.chapter01.planck_distribution.plt.show") as mock_show,
        ):
            mock_fig = MagicMock(spec=Figure)
            mock_subplots.return_value = (mock_fig, self._create_mock_axes())

            plot_average_energy()

            mock_show.assert_called_once()
            mock_fig.savefig.assert_not_called()
