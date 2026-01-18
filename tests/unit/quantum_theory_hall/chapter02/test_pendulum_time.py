"""Unit tests for pendulum time numerical integration."""

from pathlib import Path
from unittest.mock import MagicMock, patch

from matplotlib.axes import Axes
from matplotlib.figure import Figure
import numpy as np

from quantum_theory_hall.chapter02.pendulum_time import omega_t, plot_pendulum_time


class TestOmegaT:
    """Test cases for omega_t function."""

    def test_omega_t_returns_inf_for_zero_delta(self) -> None:
        """Test that omega_t returns inf when delta <= 0."""
        assert omega_t(0.0, np.pi / 4) == np.inf
        assert omega_t(-0.1, np.pi / 4) == np.inf

    def test_omega_t_returns_zero_when_upper_leq_lower(self) -> None:
        """Test that omega_t returns 0 when upper <= lower."""
        # upper = pi - delta, lower = theta_0
        # If delta is close to pi, upper becomes small
        result = omega_t(np.pi - 0.1, 0.2)  # upper = 0.1, lower = 0.2
        assert result == 0.0

    def test_omega_t_positive_result(self) -> None:
        """Test that omega_t returns positive finite value for valid inputs."""
        result = omega_t(0.3, np.pi / 6)
        assert np.isfinite(result)
        assert result > 0

    def test_omega_t_near_boundary(self) -> None:
        """Test omega_t with delta near boundary where integrand approaches singularity."""
        # With very small delta, the integral upper bound approaches pi
        # where cos(theta) -> -1, making cos(theta) + cos(delta) -> 0
        result = omega_t(0.001, np.pi / 6)
        assert np.isfinite(result)
        assert result > 0


class TestPlotPendulumTime:
    """Test cases for plot_pendulum_time function."""

    def _create_mock_axes(self) -> MagicMock:
        """Create a properly mocked axes object."""
        mock_ax = MagicMock(spec=Axes)
        return mock_ax

    def test_plot_saves_figure(self) -> None:
        """Test that the figure is saved when path is provided."""
        with patch("matplotlib.pyplot.subplots") as mock_subplots:
            mock_fig = MagicMock(spec=Figure)
            mock_subplots.return_value = (mock_fig, self._create_mock_axes())

            output_path = Path("test_output.png")
            plot_pendulum_time(output_path)

            mock_fig.savefig.assert_called_once()

    def test_plot_shows_figure(self) -> None:
        """Test that the figure is shown when no path is provided."""
        with (
            patch("matplotlib.pyplot.subplots") as mock_subplots,
            patch("quantum_theory_hall.chapter02.pendulum_time.plt.show") as mock_show,
        ):
            mock_fig = MagicMock(spec=Figure)
            mock_subplots.return_value = (mock_fig, self._create_mock_axes())

            plot_pendulum_time()

            mock_show.assert_called_once()
            mock_fig.savefig.assert_not_called()
