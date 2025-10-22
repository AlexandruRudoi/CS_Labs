"""
Utility functions for Playfair cipher
"""

import math

class MatrixDimensionCalculator:
    """Calculates optimal matrix dimensions for different alphabet sizes"""
    
    @staticmethod
    def calculate(alphabet_size: int) -> tuple[int, int]:
        """Calculate optimal matrix dimensions"""
        if alphabet_size <= 25:
            return 5, 5
        elif alphabet_size <= 30:
            return 5, 6
        elif alphabet_size <= 36:
            return 6, 6
        else:
            # For larger alphabets, calculate dynamically
            sqrt_size = math.sqrt(alphabet_size)
            rows = int(sqrt_size)
            cols = math.ceil(alphabet_size / rows)
            return rows, cols


class TextPreprocessor:
    """Handles text preprocessing for Playfair cipher"""
    
    def __init__(self, separator: str):
        self.separator = separator
    
    def prepare_text(self, text: str) -> list[str]:
        """Prepare text for encryption/decryption"""
        # Remove spaces and convert to uppercase
        clean_text = ''.join(text.upper().split())
        
        # Replace any separator in text with a substitute letter
        if self.separator in clean_text:
            substitute = chr(ord(self.separator) - 1) if ord(self.separator) > ord('A') else 'V'
            clean_text = clean_text.replace(self.separator, substitute)
        
        # Split into pairs
        pairs = []
        i = 0
        while i < len(clean_text):
            if i + 1 < len(clean_text):
                if clean_text[i] == clean_text[i + 1]:
                    # Insert separator between identical letters
                    pairs.append(clean_text[i] + self.separator)
                    i += 1
                else:
                    pairs.append(clean_text[i] + clean_text[i + 1])
                    i += 2
            else:
                # Add separator for odd length
                pairs.append(clean_text[i] + self.separator)
                i += 1
        
        return pairs