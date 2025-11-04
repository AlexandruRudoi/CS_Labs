from des_tables import PC2, SHIFT_SCHEDULE
from des_utils import permute, left_shift, split_key, bits_to_hex


def generate_round_key(K_plus, round_num, verbose=True):
    """
    Generate round key Ki for given round number

    Parameters:
    - K_plus: 56-bit key after PC-1
    - round_num: round number (1-16)
    - verbose: if True, print all intermediate steps

    Returns:
    - Ki: 48-bit round key
    """
    if verbose:
        print(f"\n{'='*80}")
        print(f"GENERATING ROUND KEY K{round_num}")
        print(f"{'='*80}")

    # Step 1: Split K+ into C0 and D0
    if verbose:
        print(f"\nStep 1: Split K+ into C0 and D0 (28 bits each)")

    C, D = split_key(K_plus)

    if verbose:
        print(f"C0 = {C} (hex: {bits_to_hex(C)})")
        print(f"D0 = {D} (hex: {bits_to_hex(D)})")

    # Step 2: Apply shifts for rounds 1 to i
    if verbose:
        print(
            f"\nStep 2: Apply left circular shifts for rounds 1 to {round_num}")
        print(f"Shift schedule: {SHIFT_SCHEDULE}")

    for r in range(1, round_num + 1):
        shifts = SHIFT_SCHEDULE[r-1]
        C = left_shift(C, shifts)
        D = left_shift(D, shifts)

        if verbose:
            print(f"  Round {r}: Shift by {shifts}")
            print(f"         C{r} = {C} (hex: {bits_to_hex(C)})")
            print(f"         D{r} = {D} (hex: {bits_to_hex(D)})")

    # Step 3: Combine Ci and Di
    if verbose:
        print(f"\nStep 3: Combine C{round_num} and D{round_num}")

    CD = C + D

    if verbose:
        print(f"C{round_num}D{round_num} (56 bits) = {CD}")
        print(f"Hex: {bits_to_hex(CD)}")

    # Step 4: Apply PC-2
    if verbose:
        print(f"\nStep 4: Apply PC-2 permutation (56 bits -> 48 bits)")

    Ki = permute(CD, PC2)

    if verbose:
        print(f"K{round_num} (48 bits) = {Ki}")
        print(f"Hex: {bits_to_hex(Ki)}")

    return Ki


def generate_all_round_keys(K_plus):
    """Generate all 16 round keys from K+"""
    round_keys = []
    for i in range(1, 17):
        Ki = generate_round_key(K_plus, i, verbose=False)
        round_keys.append(Ki)
    return round_keys
