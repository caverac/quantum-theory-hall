#!/usr/bin/env python3
"""Run tests only for modified files."""

from pathlib import Path
import subprocess
import sys


def get_test_file_for_source(source_file: Path) -> Path | None:
    """Map a source file to its corresponding test file."""
    # Handle test files directly
    if source_file.name.startswith("test_"):
        return source_file

    # Map source files to test files
    # quantum_theory_hall/chapter02/pendulum.py -> tests/unit/quantum_theory_hall/chapter02/test_pendulum.py
    if source_file.suffix != ".py":
        return None

    parts = source_file.parts
    if "quantum_theory_hall" not in parts:
        return None

    # Find the index of quantum_theory_hall
    idx = parts.index("quantum_theory_hall")
    relative_parts = parts[idx:]

    # Build test path
    test_path = Path("tests/unit") / Path(*relative_parts)
    test_path = test_path.with_name(f"test_{test_path.name}")

    if test_path.exists():
        return test_path

    return None


def main() -> int:
    """Run tests for modified files."""
    if len(sys.argv) < 2:
        print("No files provided")
        return 0

    files = [Path(f) for f in sys.argv[1:]]
    test_files: set[Path] = set()

    for file in files:
        test_file = get_test_file_for_source(file)
        if test_file and test_file.exists():
            test_files.add(test_file)

    if not test_files:
        print("No test files found for modified files")
        return 0

    print(f"Running tests: {', '.join(str(f) for f in test_files)}")

    # Run pytest without coverage to avoid the fail-under threshold
    result = subprocess.run(
        [sys.executable, "-m", "pytest", *[str(f) for f in test_files], "-v", "--no-cov"],
        check=False,
    )

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
