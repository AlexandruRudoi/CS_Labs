import rsa
import elgamal


# Read the message used for signing from a text file
def read_message(path="message.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    message = read_message()
    print(f"Message: {message[:250]}...")
    print(f"Message length: {len(message)} characters\n")

    # RSA: generate keys, sign and verify using MD5 hash
    print("RSA Digital Signature (Hash: MD5)")
    n, e, d, p, q = rsa.generate_rsa_keys(3072)
    signature_rsa, hash_rsa = rsa.sign(message, d, n)
    valid_rsa, h_rsa, h_rsa_prime = rsa.verify(message, signature_rsa, e, n)
    print(f"RSA valid: {valid_rsa}")

    # ElGamal: use provided p and g, generate keys, sign and verify with MD4 hash
    print("\nElGamal Digital Signature (Hash: MD4)")
    raw_p = """323170060713110073001535134778251633624880571334890751745884
 34139269806834136210002792056362640164685458556357935330816928
 82902308057347262527355474246124574102620252791657297286270630
 03252634282131457669314142236542209411113486299916574782680342
 30553086349050635557712219187890332729569696129743856241741236
 23722519734640269185579776797682301462539793305801522685873076
 11975324364674758554607150438968449403661304976978128542959586
 59597567051283852132784468522925504568272879113720098931873959
 14337417583782600027803497319855206060753323412260325468408812
 0031105907484281003994966956119696956248629032338072839127039"""

    p_elgamal = raw_p.replace("\n", "").replace(" ", "")
    g_elgamal = "2"
    x, y, p_int, g_int = elgamal.generate_elgamal_keys(p_elgamal, g_elgamal)
    signature_elgamal = elgamal.sign(message, x, p_int, g_int)
    valid_elgamal, h_elg, left, right = elgamal.verify(
        message, signature_elgamal, y, p_int, g_int)
    print(f"ElGamal valid: {valid_elgamal}")


if __name__ == "__main__":
    main()
