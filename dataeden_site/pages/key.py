from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Generated Key:", key)
key_base64 = key.decode('utf-8')
print("URL-safe Base64 Encoded Key:", key_base64)
