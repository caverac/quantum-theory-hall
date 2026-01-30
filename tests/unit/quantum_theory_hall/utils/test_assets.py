"""Unit tests for asset generation utilities."""

from pathlib import Path

from matplotlib import pyplot as plt

from quantum_theory_hall.utils.assets import (
    figures_are_equal,
    get_registered_assets,
    register_asset,
    save_figure_if_changed,
)


class TestRegisterAsset:
    """Test cases for register_asset decorator."""

    def test_register_asset_adds_to_registry(self) -> None:
        """Test that decorated functions are added to registry."""
        # Get initial count
        initial_assets = get_registered_assets()
        initial_count = len(initial_assets)

        @register_asset("test_asset.png")
        def test_plot(*, path: Path | None = None) -> None:  # pylint: disable=unused-argument
            pass

        assets = get_registered_assets()
        assert len(assets) == initial_count + 1
        assert "test_asset.png" in assets

    def test_register_asset_returns_function_unchanged(self) -> None:
        """Test that decorator returns the original function."""

        def original_func(*, path: Path | None = None) -> None:  # pylint: disable=unused-argument
            return None

        decorated = register_asset("another_test.png")(original_func)
        assert decorated is original_func


class TestGetRegisteredAssets:
    """Test cases for get_registered_assets function."""

    def test_get_registered_assets_returns_copy(self) -> None:
        """Test that returned dict is a copy."""
        assets1 = get_registered_assets()
        assets2 = get_registered_assets()
        assert assets1 is not assets2


class TestFiguresAreEqual:
    """Test cases for figures_are_equal function."""

    def test_figures_are_equal_returns_false_for_nonexistent(self, tmp_path: Path) -> None:
        """Test that comparison returns False when file doesn't exist."""
        fig, _ = plt.subplots()
        result = figures_are_equal(tmp_path / "nonexistent.png", fig)
        plt.close(fig)
        assert result is False

    def test_figures_are_equal_returns_true_for_identical(self, tmp_path: Path) -> None:
        """Test that comparison returns True for identical figures."""
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 2, 3])

        output_path = tmp_path / "test.png"
        fig.savefig(output_path, dpi=100)

        result = figures_are_equal(output_path, fig, dpi=100)
        plt.close(fig)
        assert result is True

    def test_figures_are_equal_returns_false_for_different(self, tmp_path: Path) -> None:
        """Test that comparison returns False for different figures."""
        # Create and save first figure
        fig1, ax1 = plt.subplots()
        ax1.plot([1, 2, 3], [1, 2, 3])
        output_path = tmp_path / "test.png"
        fig1.savefig(output_path, dpi=100)
        plt.close(fig1)

        # Create different figure
        fig2, ax2 = plt.subplots()
        ax2.plot([1, 2, 3], [3, 2, 1])  # Different data

        result = figures_are_equal(output_path, fig2, dpi=100)
        plt.close(fig2)
        assert result is False

    def test_figures_are_equal_returns_false_for_different_shape(self, tmp_path: Path) -> None:
        """Test that comparison returns False for different figure sizes."""
        # Create and save first figure
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        ax1.plot([1, 2, 3], [1, 2, 3])
        output_path = tmp_path / "test.png"
        fig1.savefig(output_path, dpi=100)
        plt.close(fig1)

        # Create figure with different size
        fig2, ax2 = plt.subplots(figsize=(6, 6))
        ax2.plot([1, 2, 3], [1, 2, 3])

        result = figures_are_equal(output_path, fig2, dpi=100)
        plt.close(fig2)
        assert result is False


class TestSaveFigureIfChanged:
    """Test cases for save_figure_if_changed function."""

    def test_save_figure_if_changed_writes_new_file(self, tmp_path: Path) -> None:
        """Test that new files are written."""
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 2, 3])

        output_path = tmp_path / "new.png"
        result = save_figure_if_changed(fig, output_path, dpi=100)
        plt.close(fig)

        assert result is True
        assert output_path.exists()

    def test_save_figure_if_changed_skips_identical(self, tmp_path: Path) -> None:
        """Test that identical figures are skipped."""
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 2, 3])

        output_path = tmp_path / "existing.png"
        # First save
        fig.savefig(output_path, dpi=100)
        mtime_before = output_path.stat().st_mtime

        # Attempt to save again
        result = save_figure_if_changed(fig, output_path, dpi=100)
        plt.close(fig)

        assert result is False
        assert output_path.stat().st_mtime == mtime_before

    def test_save_figure_if_changed_writes_different(self, tmp_path: Path) -> None:
        """Test that different figures are written."""
        # Save first figure
        fig1, ax1 = plt.subplots()
        ax1.plot([1, 2, 3], [1, 2, 3])
        output_path = tmp_path / "changing.png"
        fig1.savefig(output_path, dpi=100)
        plt.close(fig1)

        # Save different figure
        fig2, ax2 = plt.subplots()
        ax2.plot([1, 2, 3], [3, 2, 1])

        result = save_figure_if_changed(fig2, output_path, dpi=100)
        plt.close(fig2)

        assert result is True

    def test_save_figure_if_changed_creates_parent_dirs(self, tmp_path: Path) -> None:
        """Test that parent directories are created."""
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [1, 2, 3])

        output_path = tmp_path / "nested" / "dir" / "test.png"
        result = save_figure_if_changed(fig, output_path, dpi=100)
        plt.close(fig)

        assert result is True
        assert output_path.exists()
