"""AES-256 encryption using PBKDF2-HMAC-SHA256 and a random salt/nonce."""

import base64
try:
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
    from Crypto.Protocol.KDF import PBKDF2
    from Crypto.Random import get_random_bytes
except ModuleNotFoundError:  # Keep Caesar/Vigenere usable without the optional package.
    AES = SHA256 = PBKDF2 = get_random_bytes = None


class AESCipherError(ValueError):
    """Raised when AES input cannot be decrypted or a dependency is missing."""


_SALT_SIZE = 16
_KEY_SIZE = 32
_ITERATIONS = 310_000


def _derive_key(password: str, salt: bytes) -> bytes:
    if PBKDF2 is None:
        raise AESCipherError("AES requires pycryptodome. Install it with: pip install pycryptodome")
    if not password:
        raise AESCipherError("Password cannot be empty.")
    return PBKDF2(password.encode("utf-8"), salt, dkLen=_KEY_SIZE, count=_ITERATIONS, hmac_hash_module=SHA256)


def encrypt(text: str, password: str) -> str:
    if AES is None:
        raise AESCipherError("AES requires pycryptodome. Install it with: pip install pycryptodome")
    salt = get_random_bytes(_SALT_SIZE)
    cipher = AES.new(_derive_key(password, salt), AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode("utf-8"))
    payload = salt + cipher.nonce + tag + ciphertext
    return base64.urlsafe_b64encode(payload).decode("ascii")


def decrypt(token: str, password: str) -> str:
    if AES is None:
        raise AESCipherError("AES requires pycryptodome. Install it with: pip install pycryptodome")
    try:
        payload = base64.urlsafe_b64decode(token.encode("ascii"))
        if len(payload) < 48:
            raise ValueError("Ciphertext is too short.")
        salt, nonce, tag, ciphertext = payload[:16], payload[16:32], payload[32:48], payload[48:]
        cipher = AES.new(_derive_key(password, salt), AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode("utf-8")
    except (ValueError, KeyError, UnicodeDecodeError, TypeError) as error:
        raise AESCipherError("Invalid ciphertext or password.") from error
