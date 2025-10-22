"""
Core validation components for Playfair cipher
"""

class AlphabetValidator:
    """Handles alphabet and text validation"""
    
    def __init__(self, alphabet: str, separator: str):
        self.alphabet = alphabet
        self.separator = separator
    
    def validate_key(self, key: str) -> None:
        """Validate encryption key"""
        if len("".join(key.split())) < 7:
            raise ValueError("Cheia trebuie să aibă cel puțin 7 caractere!")
        
        for char in "".join(key.split()).upper():
            if char not in self.alphabet and char != self.separator:
                raise ValueError(f"Caracterul '{char}' nu este valid! Folosiți doar litere din alfabetul specificat.")
    
    def validate_text(self, text: str) -> None:
        """Validate input text"""
        for char in  "".join(text.split()).upper():
            if char != ' ' and char not in self.alphabet and char != self.separator:
                raise ValueError(f"Caracterul '{char}' nu este valid! Folosiți doar litere din alfabetul specificat.")