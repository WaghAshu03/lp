# AES Algorithm

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def encrypt_aes(key, plaintext):
    backend = default_backend()
    # Initialization Vector (IV) - should be random and unique for each encryption
    iv = b'\x00' * 16

    # Generate a random IV and create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # Create an encryptor object from the cipher
    encryptor = cipher.encryptor()

    # Apply padding to the plaintext
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Perform the encryption and obtain the ciphertext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return ciphertext


def decrypt_aes(key, ciphertext):
    backend = default_backend()
    # Initialization Vector (IV) - should be the same as used during encryption
    iv = b'\x00' * 16

    # Create a cipher object with the same key and mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # Create a decryptor object from the cipher
    decryptor = cipher.decryptor()

    # Perform the decryption and obtain the padded plaintext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding from the plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext


# Example usage
# 256-bit key (for demonstration purposes only, use a strong and secure key)
key = b'\x00' * 32
plaintext = b'This is a secret message'

ciphertext = encrypt_aes(key, plaintext)
decrypted_text = decrypt_aes(key, ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text.decode())
