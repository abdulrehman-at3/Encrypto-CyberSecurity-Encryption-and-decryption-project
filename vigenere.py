"""Vigenere cipher implementation."""


def _key_values(key: str) -> list[int]:
    values = [ord(char.lower()) - ord("a") for char in key if char.isalpha() and char.isascii()]
    if not values:
        raise ValueError("Key must contain at least one letter.")
    return values


def _transform(text: str, key: str, direction: int) -> str:
    values = _key_values(key)
    result = []
    key_index = 0
    for char in text:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = direction * values[key_index % len(values)]
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def encrypt(text: str, key: str) -> str:
    return _transform(text, key, 1)


def decrypt(text: str, key: str) -> str:
    return _transform(text, key, -1)


class VigenereCipher:
    encrypt = staticmethod(encrypt)
    decrypt = staticmethod(decrypt)
