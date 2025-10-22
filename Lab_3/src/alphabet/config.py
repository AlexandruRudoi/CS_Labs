"""
Alphabet configuration and management
"""

from ..utils.helpers import MatrixDimensionCalculator

class AlphabetConfig:
    """Represents an alphabet configuration"""
    
    def __init__(self, alphabet: str, separator: str, name: str = "Custom"):
        self.alphabet = alphabet.upper()
        self.separator = separator.upper()
        self.name = name
        
        # Remove separator from alphabet if it exists there
        if self.separator in self.alphabet:
            self.alphabet = self.alphabet.replace(self.separator, "")
    
    def get_info(self) -> dict:
        """Get alphabet information"""
        rows, cols = MatrixDimensionCalculator.calculate(len(self.alphabet))
        return {
            'name': self.name,
            'alphabet': self.alphabet,
            'separator': self.separator,
            'total_letters': len(self.alphabet),
            'excluded_letter': self.separator,
            'matrix_dimensions': f"{rows}×{cols}"
        }