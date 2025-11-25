# Main script using modular cryptographic algorithms
from rsa import generate_rsa_keys, rsa_encrypt, rsa_decrypt
from elgamal import generate_elgamal_keys, elgamal_encrypt, elgamal_decrypt
from diffie_hellman import diffie_hellman_exchange, simple_aes_demo
from utils import P


def display_menu():
    print("\n" + "="*80)
    print("CRYPTOGRAPHIC ALGORITHMS MENU")
    print("="*80)
    print("1. RSA Algorithm")
    print("2. ElGamal Algorithm")
    print("3. Diffie-Hellman & AES")
    print("0. Exit")
    print("="*80)


def run_rsa(message):
    print("\n" + "="*80)
    print("Task 2.1: RSA Algorithm")
    print("="*80)

    # Generate RSA keys
    rsa_keys = generate_rsa_keys(2048)
    print(f"\nRSA keys generated.")
    print(f'Public key: {rsa_keys["public_key"]}')
    print(f'Private key: {rsa_keys["private_key"]}')

    # Encrypt message
    encrypted_rsa = rsa_encrypt(message, rsa_keys['public_key'])

    # Decrypt message
    decrypted_rsa = rsa_decrypt(encrypted_rsa, rsa_keys['private_key'])


def run_elgamal(message):
    print("\n" + "="*80)
    print("Task 2.2: ElGamal Algorithm")
    print("="*80)

    # Generate ElGamal keys
    elgamal_keys = generate_elgamal_keys()

    # Encrypt message
    encrypted_elgamal = elgamal_encrypt(message, elgamal_keys['public_key'])

    # Decrypt message
    decrypted_elgamal = elgamal_decrypt(
        encrypted_elgamal, elgamal_keys['private_key'], P)


def run_diffie_hellman(message):
    print("\n" + "="*80)
    print("Task 3: Diffie-Hellman & AES")
    print("="*80)

    # Diffie-Hellman key exchange
    dh_result = diffie_hellman_exchange()

    # Demonstrate AES with derived key
    simple_aes_demo(dh_result['aes_key'], message)


def main():
    message = None

    while True:
        display_menu()
        choice = input("\nEnter your choice (0-3): ").strip()

        if choice == '0':
            print("\nExiting program. Goodbye!")
            break

        if choice in ['1', '2', '3']:
            # Ask for message if not already provided
            if message is None:
                message = input("\nEnter your first and last name: ")

            # Execute selected algorithm
            if choice == '1':
                run_rsa(message)
            elif choice == '2':
                run_elgamal(message)
            elif choice == '3':
                run_diffie_hellman(message)

            # Ask if user wants to continue
            continue_choice = input(
                "\nDo you want to continue? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("\nExiting program. Goodbye!")
                break
        else:
            print("\nInvalid choice! Please enter a number between 0 and 3.")


if __name__ == "__main__":
    main()
