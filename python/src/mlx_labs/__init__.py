"""mlx-labs — community Python helpers for Multilogin Labs.

Re-exports the same MLX client used in scripts/ for convenience.
"""
from .cli import main

__all__ = ["main"]
__version__ = "0.1.0"
