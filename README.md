# CipherVault

CipherVault is a command-line encryption toolkit with one consistent interface for:

- Caesar Cipher
- Vigenère Cipher
- AES-256 (password-derived key, authenticated AES-GCM)

## Run

Install the AES dependency:

```bash
pip install pycryptodome
```

Then start the application:

```bash
python main.py
```

AES ciphertext includes a random salt, nonce, and authentication tag in a URL-safe Base64 token. A wrong password or modified token is rejected.

## Test

```bash
python -m unittest discover -v
```
