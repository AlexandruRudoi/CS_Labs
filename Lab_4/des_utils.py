import random


def bits_to_hex(bits):
    """Convert bit string to hex for easier reading"""
    hex_str = hex(int(bits, 2))[2:].upper().zfill(len(bits)//4)
    return hex_str


def permute(bits, table):
    """Apply permutation table to bits"""
    return ''.join(bits[i-1] for i in table)


def left_shift(bits, n):
    """Circular left shift"""
    return bits[n:] + bits[:n]


def generate_random_key():
    """Generate random 64-bit key"""
    return ''.join(random.choice('01') for _ in range(64))


def apply_pc1(key_64):
    """Apply PC-1 to get K+ (56 bits)"""
    from des_tables import PC1
    return permute(key_64, PC1)


def split_key(key_56):
    """Split 56-bit key into C0 and D0 (28 bits each)"""
    C = key_56[:28]
    D = key_56[28:]
    return C, D


def print_separator():
    print("=" * 80)


def print_table(table, name, cols=8):
    """Display a table in formatted rows"""
    print(f"\n{name}:")
    for i in range(0, len(table), cols):
        print("  ", table[i:i+cols])
