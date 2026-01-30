"""Unit tests for pendulum sketch plot."""

from pathlib import Path
from unittest.mock import MagicMock, patch

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from quantum_theory_hall.chapter02.pendulum import plot_pendulum


class TestPlotPendulum:
    """Test cases for plot_pendulum function."""

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
            plot_pendulum(path=output_path)

            mock_fig.savefig.assert_called_once()

    def test_plot_shows_figure(self) -> None:
        """Test that the figure is shown when no path is provided."""
        with (
            patch("matplotlib.pyplot.subplots") as mock_subplots,
            patch("quantum_theory_hall.chapter02.pendulum.plt.show") as mock_show,
        ):
            mock_fig = MagicMock(spec=Figure)
            mock_subplots.return_value = (mock_fig, self._create_mock_axes())

            plot_pendulum()

            mock_show.assert_called_once()
            mock_fig.savefig.assert_not_called()
