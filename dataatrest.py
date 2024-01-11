from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
def pad(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data
def unpad(data):
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data
def generate_key():
    return urlsafe_b64encode(os.urandom(32)).decode('utf-8')
def encrypt(data, key):
    key = urlsafe_b64decode(key)
    data = pad(data.encode('utf-8'))
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return urlsafe_b64encode(iv + ciphertext).decode('utf-8')
def decrypt(ciphertext, key):
    key = urlsafe_b64decode(key)
    ciphertext = urlsafe_b64decode(ciphertext)
    iv = ciphertext[:16]
    data = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return unpad(decrypted_data).decode('utf-8')
# healthdata of eldercare
data_to_encrypt = ("Eldercare data: Patient: Ayomikun, age: 73, "
                   "blood pressure: 120/80mmHg, heart rate: 70bpm.")
encryption_key = generate_key()
print(f"Encryption Key: {encryption_key}")
encrypted_data = encrypt(data_to_encrypt, encryption_key)
print(f"Encrypted Data: {encrypted_data}")
decrypted_data = decrypt(encrypted_data, encryption_key)
print(f"Decrypted Data: {decrypted_data}")
