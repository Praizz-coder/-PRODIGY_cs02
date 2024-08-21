import string


colors = {
    "green": "\033[92m",
    "blue": "\033[94m",
    "red": "\033[91m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "reset": "\033[0m"
}


class CaesarCipher:
    def _init_(self):
        self.alphabets = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase
        }

    def _shift_alphabet(self, alphabet, key):
        return alphabet[key:] + alphabet[:key]

    def _create_cipher_map(self, key, mode):
        if mode == 'decrypt':
            key = -key

        shifted_lower = self._shift_alphabet(self.alphabets["lower"], key)
        shifted_upper = self._shift_alphabet(self.alphabets["upper"], key)

        return str.maketrans(
            self.alphabets["lower"] + self.alphabets["upper"],
            shifted_lower + shifted_upper
        )

    def process(self, text, key, mode):
        cipher_map = self._create_cipher_map(key, mode)
        return text.translate(cipher_map)


def get_shift_value():
    while True:
        shift = input(f"{colors['magenta']}Enter the key value (1-25): {colors['reset']}")
        if shift.isdigit() and 1 <= int(shift) <= 25:
            return int(shift)
        print(f"{colors['red']}Invalid input.{colors['reset']} Please enter a number between 1 and 25.")


def main():
    cipher = CaesarCipher()

    print(f"{colors['cyan']}Welcome to the Caesar Cipher Tool!{colors['reset']}")

    while True:
        mode = input(
            f"\nChoose an option:\n"
            f"{colors['green']}[E]{colors['reset']} Encrypt a message\n"
            f"{colors['green']}[D]{colors['reset']} Decrypt a message\n"
            f"{colors['green']}[Q]{colors['reset']} Quit\n"
            f"{colors['blue']}Your choice: {colors['reset']}"
        ).lower()

        if mode == 'q':
            print(f"{colors['yellow']}Goodbye!{colors['reset']}")
            break

        if mode not in ['e', 'd']:
            print(f"{colors['red']}Invalid option! Please choose 'E', 'D', or 'Q'.{colors['reset']}")
            continue

        text = input(f"{colors['magenta']}Enter the message: {colors['reset']}")
        shift = get_shift_value()
        result = cipher.process(text, shift, 'encrypt' if mode == 'e' else 'decrypt')

        action = "Encryption" if mode == 'e' else "Decryption"
        print(f"\n{colors['cyan']}Result of {action}:{colors['reset']}")
        print(f"{colors['green']}{result}{colors['reset']}")
        print(f"{colors['blue']}* * * * * * * * * *{colors['reset']}")


if __name__ == "__main__":
    main()