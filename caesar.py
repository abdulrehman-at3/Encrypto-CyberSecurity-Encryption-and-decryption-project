"""Caesar cipher implementation."""


def encrypt(text: str, shift: int) -> str:
    """Shift alphabetic characters by *shift*, preserving case and symbols."""
    shift %= 26
    result = []
    for char in text:
        if "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(char)
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)

class CaesarCipher:
    encrypt = staticmethod(encrypt)
    decrypt = staticmethod(decrypt)
