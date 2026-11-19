"""make.fun entry for news-image-20261119 (19 November 2026).

The repository ships a finished front-page image, entry.png, and this
program delivers it to the grader unchanged. It uses only the Python
3.13 standard library, touches no network, and is deterministic: the
output file is a byte-for-byte copy of the bundled image, so running
the program twice produces identical bytes both times.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
FALLBACK_OUTPUT_DIR = "/output"


def output_directory() -> Path:
    """Where the grader wants the image: $MAKEFUN_OUTPUT_DIR or /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(chosen) if chosen else Path(FALLBACK_OUTPUT_DIR)


def bundled_image() -> Path:
    """The image stored next to this file in the repository."""
    candidate = Path(__file__).resolve().parent / IMAGE_NAME
    if not candidate.is_file():
        raise FileNotFoundError(f"missing bundled image: {candidate}")
    return candidate


def main() -> int:
    source = bundled_image()
    target_dir = output_directory()
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / IMAGE_NAME
    shutil.copyfile(source, target)
    # Guard against a truncated copy: the delivered file must be exactly
    # as long as the bundled one, or the run is a failure, not a bad image.
    expected = source.stat().st_size
    delivered = target.stat().st_size
    if delivered != expected:
        raise RuntimeError(
            f"copy mismatch: wrote {delivered} bytes, expected {expected}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
