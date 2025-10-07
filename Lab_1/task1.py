# Alphabet defined manually by the table
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
L2N = {ch: i for i, ch in enumerate(ALPHABET)}  # Letter → Number
N2L = {i: ch for i, ch in enumerate(ALPHABET)}  # Number → Letter


def validate_text(text: str) -> bool:
    """Check if text contains only Latin letters A–Z/a–z and spaces."""
    for c in text:
        if c == " ":  # spaces are allowed
            continue
        if not (c.isalpha() and c.upper() in ALPHABET):
            return False
    return True


def normalize_text(text: str) -> str:
    """Convert text to uppercase and remove spaces."""
    return text.upper().replace(" ", "")


def caesar_encrypt(plaintext: str, key: int) -> str:
    """Encrypt plaintext using Caesar cipher with shift key."""
    result = []
    for ch in plaintext:
        x = L2N[ch]       # numeric value (0–25)
        y = (x + key) % 26          # shifted value
        result.append(N2L[y])
    return "".join(result)


def caesar_decrypt(ciphertext: str, key: int) -> str:
    """Decrypt ciphertext using Caesar cipher with shift key."""
    result = []
    for ch in ciphertext:
        y = L2N[ch]
        x = (y - key) % 26
        result.append(N2L[x])
    return "".join(result)


def read_key() -> int:
    """Prompt user to enter a valid key (1–25)."""
    while True:
        s = input("Enter the key (1–25): ").strip()
        if s.isdigit():
            k = int(s)
            if 1 <= k <= 25:
                return k
        print("Error: key must be an integer between 1 and 25.")


def main():
    operation = input("Choose operation (encrypt/decrypt): ").strip().lower()
    while operation not in ('encrypt', 'decrypt'):
        operation = input(
            "Invalid operation! Please type 'encrypt' or 'decrypt': ").strip().lower()

    text = input("Enter text (letters only): ").strip()
    while not validate_text(text) or not normalize_text(text):
        text = input(
            "Error: please enter at least one letter A–Z/a–z. Try again: ").strip()

    text = normalize_text(text)
    key = read_key()

    if operation == "encrypt":
        print("Ciphertext:", caesar_encrypt(text, key))
    elif operation == "decrypt":
        print("Decrypted message:", caesar_decrypt(text, key))


if __name__ == "__main__":
    main()
