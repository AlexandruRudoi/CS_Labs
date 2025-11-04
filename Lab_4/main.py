from des_tables import PC1, PC2, SHIFT_SCHEDULE
from des_utils import (print_separator, print_table, bits_to_hex,
                       generate_random_key, apply_pc1)
from key_schedule import generate_round_key


def display_tables():
    """Display all DES tables used"""
    print_table(PC1, "PC-1 Table (64 -> 56 bits)", 7)
    print_table(PC2, "PC-2 Table (56 -> 48 bits)", 6)
    print(f"\nShift Schedule: {SHIFT_SCHEDULE}")


def validate_binary_string(bits, expected_length):
    """Validate if string is binary and has correct length"""
    if len(bits) != expected_length:
        return False, f"Length must be {expected_length} bits, got {len(bits)}"
    if not all(c in '01' for c in bits):
        return False, "Input must contain only 0s and 1s"
    return True, ""


def get_key_input():
    """Get key input from user with validation"""
    print("\nChoose input method:")
    print("1. Enter 64-bit key manually")
    print("2. Enter K+ (56-bit) directly")
    print("3. Generate random key")

    # Validate menu choice
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("Invalid choice! Please enter 1, 2, or 3.")

    if choice == "1":
        # Validate 64-bit key input
        while True:
            key_input = input(
                "\nEnter 64-bit key (binary string of 0s and 1s): ").strip()
            is_valid, error_msg = validate_binary_string(key_input, 64)
            if is_valid:
                key_64 = key_input
                break
            print(f"Invalid input! {error_msg}")
            print(
                "Example: 0001001100110100010101110111100110011011101111001101111111110001")

        print(f"\n✓ Valid 64-bit Key: {key_64}")
        print(f"  Hex: {bits_to_hex(key_64)}")
        print(f"\nApplying PC-1 to get K+...")
        K_plus = apply_pc1(key_64)

    elif choice == "2":
        # Validate 56-bit K+ input
        while True:
            K_plus = input(
                "\nEnter K+ (56-bit binary string of 0s and 1s): ").strip()
            is_valid, error_msg = validate_binary_string(K_plus, 56)
            if is_valid:
                break
            print(f"Invalid input! {error_msg}")
            print("Example: 00010011001101000101011101111001100110111011110011011111")

        print(f"\n✓ Valid K+ (56 bits): {K_plus}")

    else:
        key_64 = generate_random_key()
        print(f"\nRandom 64-bit Key: {key_64}")
        print(f"Hex: {bits_to_hex(key_64)}")
        print(f"\nApplying PC-1 to get K+...")
        K_plus = apply_pc1(key_64)

    print(f"\nK+ (56 bits): {K_plus}")
    print(f"Hex: {bits_to_hex(K_plus)}")

    return K_plus


def get_round_number():
    """Get round number from user with validation"""
    while True:
        round_input = input("\nEnter round number i (1-16): ").strip()

        # Check if input is a valid integer
        try:
            round_num = int(round_input)

            # Check if in valid range
            if 1 <= round_num <= 16:
                return round_num
            else:
                print(
                    f"Invalid range! Round number must be between 1 and 16, got {round_num}.")

        except ValueError:
            print(f"Invalid input! '{round_input}' is not a valid integer.")
            print("Please enter a number between 1 and 16.")


def main():
    print("="*80)
    print("DES ROUND KEY GENERATION - Task 2.3")
    print("Given K+ (56-bit permuted key), generate round key Ki")
    print("="*80)

    display_tables()
    print_separator()
    K_plus = get_key_input()

    print_separator()
    round_num = get_round_number()

    Ki = generate_round_key(K_plus, round_num)

    # Final result
    print(f"\n{'='*80}")
    print(f"FINAL RESULT")
    print(f"{'='*80}")
    print(f"Input K+ (56 bits): {K_plus}")
    print(f"Round number: {round_num}")
    print(f"Output K{round_num} (48 bits): {Ki}")
    print(f"K{round_num} in hex: {bits_to_hex(Ki)}")
    print(f"{'='*80}")


if __name__ == "__main__":
    main()
