"""
User Interface for Playfair Cipher
"""

from ..playfair import PlayfairCipher
from ..alphabet.configs import AlphabetConfigs

class PlayfairUI:
    """Main user interface for Playfair cipher"""
    
    def __init__(self):
        self.cipher = None
        self.current_alphabet = "Romanian"
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("     CIFRUL PLAYFAIR")
        print("="*50)
        print("1. Criptare")
        print("2. Decriptare")
        print("3. Afișare matrice")
        print("4. Schimbare alfabet")
        print("5. Informații despre alfabet")
        print("6. Ieșire")
        print("="*50)
        print(f"Alfabet curent: {self.current_alphabet}")
    
    def display_alphabet_menu(self):
        """Display alphabet selection menu"""
        print("\n--- Selectare Alfabet ---")
        print("1. Română (30 litere, separator: W)")
        print("2. Engleză (25 litere, separator: J)")
        print("3. Rusă (32 litere, separator: Ё)")
        print("4. Alfabet personalizat")
        print("5. Înapoi la meniul principal")
    
    def get_user_choice(self, max_choice=6):
        """Get and validate user choice"""
        try:
            choice = int(input(f"Alegeți opțiunea (1-{max_choice}): "))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"Opțiune invalidă! Alegeți între 1-{max_choice}.")
                return None
        except ValueError:
            print("Vă rugăm să introduceți un număr valid!")
            return None
    
    def setup_alphabet(self):
        """Setup alphabet configuration"""
        while True:
            self.display_alphabet_menu()
            choice = self.get_user_choice(5)
            
            if choice is None:
                continue
            
            if choice == 1:
                alphabet_config = AlphabetConfigs.romanian()
                self.cipher = PlayfairCipher(alphabet_config)
                self.current_alphabet = "Romanian"
                print("Alfabet român activat.")
                break
            elif choice == 2:
                alphabet_config = AlphabetConfigs.english()
                self.cipher = PlayfairCipher(alphabet_config)
                self.current_alphabet = "English"
                print("Alfabet englez activat.")
                break
            elif choice == 3:
                alphabet_config = AlphabetConfigs.russian()
                self.cipher = PlayfairCipher(alphabet_config)
                self.current_alphabet = "Russian"
                print("Alfabet rus activat.")
                break
            elif choice == 4:
                self.setup_custom_alphabet()
                break
            elif choice == 5:
                break
    
    def setup_custom_alphabet(self):
        """Setup custom alphabet"""
        print("\n--- Alfabet Personalizat ---")
        alphabet = input("Introduceți alfabetul (fără spații): ").strip()
        if not alphabet:
            print("Alfabetul nu poate fi gol!")
            return
        
        separator = input("Introduceți separatorul (opțional, apăsați Enter pentru automat): ").strip()
        if not separator:
            separator = None
        
        try:
            alphabet_config = AlphabetConfigs.custom(alphabet, separator)
            self.cipher = PlayfairCipher(alphabet_config)
            self.current_alphabet = "Custom"
            print(f"Alfabet personalizat activat: {len(self.cipher.config.alphabet)} litere, separator: {self.cipher.config.separator}")
        except Exception as e:
            print(f"Eroare la configurarea alfabetului: {e}")
    
    def ensure_cipher_initialized(self):
        """Ensure cipher is initialized with an alphabet"""
        if self.cipher is None:
            print("Alfabetul nu a fost configurat. Folosesc alfabetul român implicit.")
            alphabet_config = AlphabetConfigs.romanian()
            self.cipher = PlayfairCipher(alphabet_config)
            self.current_alphabet = "Romanian"
    
    def run(self):
        """Main application loop"""
        print("Bun venit la Cifrul Playfair pentru alfabete multiple!")
        
        # Initialize with default Romanian alphabet
        alphabet_config = AlphabetConfigs.romanian()
        self.cipher = PlayfairCipher(alphabet_config)
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice is None:
                continue
            
            if choice == 1:
                self._handle_encryption()
            elif choice == 2:
                self._handle_decryption()
            elif choice == 3:
                self._handle_matrix_display()
            elif choice == 4:
                self.setup_alphabet()
            elif choice == 5:
                self._show_alphabet_info()
            elif choice == 6:
                print("\nLa revedere!")
                break
            
            input("\nApăsați Enter pentru a continua...")
    
    def _handle_encryption(self):
        """Handle encryption process"""
        self.ensure_cipher_initialized()
        print("\n--- CRIPTARE ---")
        key = self._get_key()
        plaintext = self._get_text("textul de criptat")
        
        try:
            ciphertext = self.cipher.encrypt(plaintext, key)
            print(f"\nTextul original: {plaintext}")
            print(f"Criptograma: {ciphertext}")
            
            # Ask if user wants to see the matrix
            show_matrix = input("\nDoriți să vedeți matricea folosită? (d/n): ").lower()
            if show_matrix in ['d', 'da', 'y', 'yes']:
                print()
                self.cipher.display_matrix()
                
        except Exception as e:
            print(f"Eroare la criptare: {e}")
    
    def _handle_decryption(self):
        """Handle decryption process"""
        self.ensure_cipher_initialized()
        print("\n--- DECRIPTARE ---")
        key = self._get_key()
        ciphertext = self._get_text("criptograma")
        
        try:
            plaintext = self.cipher.decrypt(ciphertext, key)
            print(f"\nCriptograma: {ciphertext}")
            print(f"Textul decriptat: {plaintext}")
            
            # Ask if user wants to see the matrix
            show_matrix = input("\nDoriți să vedeți matricea folosită? (d/n): ").lower()
            if show_matrix in ['d', 'da', 'y', 'yes']:
                print()
                self.cipher.display_matrix()
                
        except Exception as e:
            print(f"Eroare la decriptare: {e}")
    
    def _handle_matrix_display(self):
        """Handle matrix display"""
        self.ensure_cipher_initialized()
        print("\n--- AFIȘARE MATRICE ---")
        key = self._get_key()
        
        try:
            self.cipher.create_matrix(key)
            print()
            self.cipher.display_matrix()
        except Exception as e:
            print(f"Eroare la crearea matricei: {e}")
    
    def _show_alphabet_info(self):
        """Show information about the current alphabet"""
        self.ensure_cipher_initialized()
        print("\n--- INFORMAȚII ALFABET ---")
        alphabet_info = self.cipher.get_alphabet_info()
        print(f"Alfabetul curent: {alphabet_info['name']}")
        print(f"Litere în matrice: {alphabet_info['alphabet']}")
        print(f"Numărul de litere: {alphabet_info['total_letters']}")
        print(f"Litera exclusă (separator): {alphabet_info['excluded_letter']}")
        print(f"Dimensiuni matrice: {alphabet_info['matrix_dimensions']}")
        
        if self.current_alphabet == "Romanian":
            print("\nCaracterele speciale românești: Ă, Â, Î, Ș, Ț")
        elif self.current_alphabet == "Russian":
            print("\nCaracterele speciale rusești: Ё (exclusă), Я, Ю, Щ, Ч, Ш, Ж")
        
        print("\nMatricea Playfair folosește dimensiuni calculate automat pe baza alfabetului.")
        print("Litera cea mai puțin folosită este exclusă din matrice și folosită ca separator.")
    
    def _get_key(self):
        """Get and validate encryption key"""
        while True:
            try:
                key = input("Introduceți cheia (minim 7 caractere): ").strip()
                if not key:
                    print("Cheia nu poate fi goală!")
                    continue
                
                self.cipher.validator.validate_key(key)
                return key
            except ValueError as e:
                print(f"Eroare: {e}")
    
    def _get_text(self, text_type):
        """Get and validate text input"""
        while True:
            try:
                text = input(f"Introduceți {text_type}: ").strip()
                if not text:
                    print(f"{text_type.capitalize()} nu poate fi gol!")
                    continue
                
                self.cipher.validator.validate_text(text)
                return text
            except ValueError as e:
                print(f"Eroare: {e}")