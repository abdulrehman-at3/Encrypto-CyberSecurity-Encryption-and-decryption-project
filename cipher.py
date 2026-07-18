"""Backward-compatible import for the Caesar cipher."""

from caesar import CaesarCipher, decrypt, encrypt

__all__ = ["CaesarCipher", "encrypt", "decrypt"]
