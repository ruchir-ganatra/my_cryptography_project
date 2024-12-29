from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate a new RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save the keys to files
with open("private_key.pem", "wb") as f:
    f.write(private_key)

with open("public_key.pem", "wb") as f:
    f.write(public_key)

# Encrypt a message
with open("public_key.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(public_key)
message = b"Hello, World!"
ciphertext = cipher_rsa.encrypt(message)

print(f"Ciphertext: {ciphertext}")

# Decrypt the message
with open("private_key.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

cipher_rsa = PKCS1_OAEP.new(private_key)
plaintext = cipher_rsa.decrypt(ciphertext)

print(f"Plaintext: {plaintext.decode()}")