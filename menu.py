"""Interactive menus for CipherVault."""

import caesar
import vigenere
import aes_cipher
from utils import banner, clear_screen, pause, read_non_empty, read_shift


def _run_algorithm(name: str) -> None:
    while True:
        clear_screen()
        banner(name, "Encrypt, decrypt, or go back")
        print("1. Encrypt\n2. Decrypt\n3. Back")
        choice = input("\nChoice: ").strip()
        if choice == "3":
            return
        if choice not in {"1", "2"}:
            print("Invalid choice.")
            pause()
            continue

        try:
            text = read_non_empty("Enter Text: " if choice == "1" else "Enter Cipher Text: ")
            if name == "Caesar Cipher":
                key = read_shift()
                result = caesar.encrypt(text, key) if choice == "1" else caesar.decrypt(text, key)
            elif name == "Vigenere Cipher":
                key = read_non_empty("Enter Key: ")
                result = vigenere.encrypt(text, key) if choice == "1" else vigenere.decrypt(text, key)
            else:
                key = read_non_empty("Enter Password: ")
                result = aes_cipher.encrypt(text, key) if choice == "1" else aes_cipher.decrypt(text, key)
            print("\nEncrypted:" if choice == "1" else "\nDecrypted:", result)
        except (ValueError, aes_cipher.AESCipherError) as error:
            print(f"\nError: {error}")
        pause()


def run() -> None:
    algorithms = {"1": "Caesar Cipher", "2": "Vigenere Cipher", "3": "AES-256"}
    while True:
        clear_screen()
        banner("CIPHER VAULT", "Multi-Algorithm Encryption Tool")
        print("Select Encryption Algorithm\n")
        print("[1] Caesar Cipher\n\n[2] Vigenere Cipher\n\n[3] AES-256\n\n[4] Exit")
        choice = input("\nChoice: ").strip()
        if choice == "4":
            print("Goodbye!")
            return
        if choice in algorithms:
            _run_algorithm(algorithms[choice])
        else:
            print("Invalid choice.")
            pause()
