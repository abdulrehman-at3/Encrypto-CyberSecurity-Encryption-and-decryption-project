"""Small user-interface helpers for CipherVault."""

import os


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pause(message: str = "Press Enter to continue...") -> None:
    input(message)


def banner(title: str, subtitle: str = "") -> None:
    line = "=" * 52
    print(line)
    print(title.center(52))
    if subtitle:
        print(subtitle.center(52))
    print(line)


def read_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def read_shift() -> int:
    while True:
        try:
            return int(input("Enter Shift: ").strip())
        except ValueError:
            print("Please enter a whole number.")
