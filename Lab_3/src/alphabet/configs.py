"""
Predefined alphabet configurations factory
"""

from .config import AlphabetConfig

class AlphabetConfigs:
    """Factory for predefined alphabet configurations"""
    
    @staticmethod
    def romanian() -> AlphabetConfig:
        """Romanian alphabet configuration"""
        return AlphabetConfig("AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ", "K", "Romanian")
    
    @staticmethod
    def english() -> AlphabetConfig:
        """English alphabet configuration (J removed, used as separator)"""
        return AlphabetConfig("ABCDEFGHIKLMNOPQRSTUVWXYZ", "J", "English")
    
    @staticmethod
    def russian() -> AlphabetConfig:
        """Russian alphabet configuration (Ё removed, used as separator)"""
        return AlphabetConfig("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "Ё", "Russian")
    
    @staticmethod
    def custom(alphabet: str, separator: str = None, name: str = "Custom") -> AlphabetConfig:
        """Custom alphabet configuration"""
        if separator is None:
            # Use last letter as separator if not specified
            separator = alphabet[-1]
            alphabet = alphabet[:-1]
        return AlphabetConfig(alphabet, separator, name)