# Import common functions from task1
from task1 import ALPHABET, validate_text, normalize_text


def read_key1() -> int:
    """Read Caesar shift key k1 in [1..25]."""
    while True:
        s = input("Enter k1 (1–25): ").strip()
        if s.isdigit():
            k = int(s)
            if 1 <= k <= 25:
                return k
        print("Error: k1 must be an integer between 1 and 25.")


def validate_k2(keyword: str) -> bool:
    """k2 must be letters only, length >= 7 (before dedup)."""
    if not isinstance(keyword, str) or len(keyword.strip()) < 7:
        return False
    for ch in keyword:
        if not (ch.isalpha() and ch.upper() in ALPHABET):
            return False
    return True


def read_key2() -> str:
    """Read permutation keyword k2 (letters only, length >= 7)."""
    while True:
        s = input("Enter k2 (letters only, length ≥ 7): ").strip()
        if validate_k2(s):
            return s
        print(
            "Error: k2 must contain only letters A–Z/a–z and be at least 7 characters long.")


def build_perm_from_k2(k2: str):
    """
    Build permuted alphabet from keyword:
    - place first occurrences of letters from k2 (uppercased),
    - then append remaining letters from ALPHABET in natural order.
    Returns (perm, L2N, N2L).
    """
    k2u = k2.upper()
    seen = set()
    perm = []
    for ch in k2u:
        if ch in ALPHABET and ch not in seen:
            seen.add(ch)
            perm.append(ch)
    for ch in ALPHABET:
        if ch not in seen:
            perm.append(ch)
    # maps on permuted alphabet
    L2N = {ch: i for i, ch in enumerate(perm)}
    N2L = {i: ch for i, ch in enumerate(perm)}
    return perm, L2N, N2L


def caesar2_encrypt(plaintext: str, k1: int, k2: str) -> str:
    """Encrypt on the permuted alphabet with shift k1."""
    _, L2N, N2L = build_perm_from_k2(k2)
    P = normalize_text(plaintext)
    result = []
    for ch in P:
        x = L2N[ch]           # 0..25 in permuted alphabet
        y = (x + k1) % 26     # shift
        result.append(N2L[y])
    return "".join(result)


def caesar2_decrypt(ciphertext: str, k1: int, k2: str) -> str:
    """Decrypt on the permuted alphabet with shift k1."""
    _, L2N, N2L = build_perm_from_k2(k2)
    C = normalize_text(ciphertext)
    result = []
    for ch in C:
        y = L2N[ch]
        x = (y - k1) % 26
        result.append(N2L[x])
    return "".join(result)


def main():
    operation = input("Choose operation (encrypt/decrypt): ").strip().lower()
    while operation not in ("encrypt", "decrypt"):
        operation = input(
            "Invalid operation! Please type 'encrypt' or 'decrypt': ").strip().lower()

    text = input("Enter text (letters only; spaces allowed): ").strip()
    while not validate_text(text) or not normalize_text(text):
        text = input(
            "Error: please enter at least one letter A–Z/a–z. Try again: ").strip()

    k1 = read_key1()
    k2 = read_key2()

    if operation == "encrypt":
        print("Ciphertext:", caesar2_encrypt(text, k1, k2))
    else:
        print("Decrypted message:", caesar2_decrypt(text, k1, k2))


if __name__ == "__main__":
    main()
