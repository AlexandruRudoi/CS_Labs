"""
Main Playfair cipher facade that coordinates all components
"""

from .core.validator import AlphabetValidator
from .core.matrix import PlayfairMatrix
from .core.cryptographer import PlayfairCryptographer
from .utils.helpers import MatrixDimensionCalculator, TextPreprocessor
from .alphabet.config import AlphabetConfig

class PlayfairCipher:
    """Main Playfair cipher facade - coordinates all components"""
    
    def __init__(self, alphabet_config: AlphabetConfig = None):
        if alphabet_config is None:
            from .alphabet.configs import AlphabetConfigs
            alphabet_config = AlphabetConfigs.romanian()
        
        self.config = alphabet_config
        self.validator = AlphabetValidator(self.config.alphabet, self.config.separator)
        self.preprocessor = TextPreprocessor(self.config.separator)
        
        # Calculate matrix dimensions
        rows, cols = MatrixDimensionCalculator.calculate(len(self.config.alphabet))
        self.matrix = PlayfairMatrix(self.config.alphabet, rows, cols)
        self.cryptographer = PlayfairCryptographer(self.matrix, self.config.separator)
    
    def encrypt(self, plaintext: str, key: str) -> str:
        """Encrypt plaintext using Playfair cipher"""
        self.validator.validate_text(plaintext)
        self.validator.validate_key(key)
        
        self.matrix.create_from_key(key)
        pairs = self.preprocessor.prepare_text(plaintext)
        
        encrypted_pairs = []
        for pair in pairs:
            encrypted_pairs.append(self.cryptographer.encrypt_pair(pair))
        
        return ''.join(encrypted_pairs)
    
    def decrypt(self, ciphertext: str, key: str) -> str:
        """Decrypt ciphertext using Playfair cipher"""
        self.validator.validate_text(ciphertext)
        self.validator.validate_key(key)
        
        self.matrix.create_from_key(key)
        
        # Split ciphertext into pairs
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        decrypted_pairs = []
        
        for pair in pairs:
            if len(pair) == 2:
                decrypted_pairs.append(self.cryptographer.decrypt_pair(pair))
            else:
                decrypted_pairs.append(pair)  # Handle odd length
        
        return ''.join(decrypted_pairs)
    
    def create_matrix(self, key: str) -> None:
        """Create matrix for display purposes"""
        self.validator.validate_key(key)
        self.matrix.create_from_key(key)
    
    def display_matrix(self) -> None:
        """Display the current matrix"""
        self.matrix.display()
        print(f"\nLitera exclusă din alfabet (folosită ca separator): {self.config.separator}")
        print(f"Alfabetul folosit în matrice: {self.config.alphabet}")
    
    def get_alphabet_info(self) -> dict:
        """Get information about the alphabet and separator"""
        return self.config.get_info()
    
    def prepare_text(self, text: str) -> list[str]:
        """Expose text preparation for demonstration purposes"""
        return self.preprocessor.prepare_text(text)