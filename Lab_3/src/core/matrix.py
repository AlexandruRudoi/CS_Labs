"""
Matrix management for Playfair cipher
"""

class PlayfairMatrix:
    """Manages the Playfair cipher matrix"""
    
    def __init__(self, alphabet: str, rows: int, cols: int):
        self.alphabet = alphabet
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.char_positions = {}
    
    def create_from_key(self, key: str) -> None:
        """Create matrix from key"""
        # Normalize key - remove duplicates and convert to uppercase
        normalized_key = ""
        seen = set()
        for char in key.upper():
            if char not in seen and char in self.alphabet:
                normalized_key += char
                seen.add(char)
        
        # Add remaining alphabet letters
        full_key = normalized_key
        for char in self.alphabet:
            if char not in seen:
                full_key += char
        
        # Create matrix
        self.matrix = []
        self.char_positions = {}
        
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                char_index = i * self.cols + j
                if char_index < len(full_key):
                    char = full_key[char_index]
                    row.append(char)
                    self.char_positions[char] = (i, j)
                else:
                    row.append("")  # Empty cell for incomplete matrix
            self.matrix.append(row)
    
    def get_position(self, char: str) -> tuple[int, int] | None:
        """Get position of character in matrix"""
        return self.char_positions.get(char)
    
    def get_char_at_position(self, row: int, col: int) -> str | None:
        """Get character at given position"""
        if 0 <= row < len(self.matrix) and 0 <= col < len(self.matrix[row]):
            return self.matrix[row][col] if self.matrix[row][col] != "" else None
        return None
    
    def display(self) -> None:
        """Display the matrix"""
        if not self.matrix:
            print("Matricea nu a fost creată încă!")
            return
        
        print(f"Matricea Playfair ({self.rows}×{self.cols}, {len(self.alphabet)} litere):")
        for i, row in enumerate(self.matrix):
            formatted_row = []
            for cell in row:
                formatted_row.append(cell if cell != "" else " ")
            print(f"Rândul {i + 1}: {' '.join(formatted_row)}")