"""
Cryptographic operations for Playfair cipher
"""

from .matrix import PlayfairMatrix

class PlayfairCryptographer:
    """Handles the core encryption/decryption logic"""
    
    def __init__(self, matrix: PlayfairMatrix, separator: str):
        self.matrix = matrix
        self.separator = separator
    
    def encrypt_pair(self, pair: str) -> str:
        """Encrypt a pair of characters"""
        char1, char2 = pair[0], pair[1]
        
        # Handle separator - it doesn't appear in matrix
        if char1 == self.separator or char2 == self.separator:
            return pair  # Return unchanged
        
        pos1 = self.matrix.get_position(char1)
        pos2 = self.matrix.get_position(char2)
        
        if not pos1 or not pos2:
            return pair  # Return unchanged if positions not found
        
        row1, col1 = pos1
        row2, col2 = pos2
        
        # Same row
        if row1 == row2:
            new_col1 = (col1 + 1) % self.matrix.cols
            new_col2 = (col2 + 1) % self.matrix.cols
            return self.matrix.get_char_at_position(row1, new_col1) + self.matrix.get_char_at_position(row2, new_col2)
        
        # Same column
        elif col1 == col2:
            new_row1 = (row1 + 1) % self.matrix.rows
            new_row2 = (row2 + 1) % self.matrix.rows
            return self.matrix.get_char_at_position(new_row1, col1) + self.matrix.get_char_at_position(new_row2, col2)
        
        # Rectangle
        else:
            return self.matrix.get_char_at_position(row1, col2) + self.matrix.get_char_at_position(row2, col1)
    
    def decrypt_pair(self, pair: str) -> str:
        """Decrypt a pair of characters"""
        char1, char2 = pair[0], pair[1]
        
        # Handle separator - it doesn't appear in matrix
        if char1 == self.separator or char2 == self.separator:
            return pair  # Return unchanged
        
        pos1 = self.matrix.get_position(char1)
        pos2 = self.matrix.get_position(char2)
        
        if not pos1 or not pos2:
            return pair  # Return unchanged if positions not found
        
        row1, col1 = pos1
        row2, col2 = pos2
        
        # Same row
        if row1 == row2:
            new_col1 = (col1 - 1) % self.matrix.cols
            new_col2 = (col2 - 1) % self.matrix.cols
            return self.matrix.get_char_at_position(row1, new_col1) + self.matrix.get_char_at_position(row2, new_col2)
        
        # Same column
        elif col1 == col2:
            new_row1 = (row1 - 1) % self.matrix.rows
            new_row2 = (row2 - 1) % self.matrix.rows
            return self.matrix.get_char_at_position(new_row1, col1) + self.matrix.get_char_at_position(new_row2, col2)
        
        # Rectangle
        else:
            return self.matrix.get_char_at_position(row1, col2) + self.matrix.get_char_at_position(row2, col1)