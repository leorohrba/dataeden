import base64
from cryptography.fernet import Fernet

key = b'R_vUYsaQQkyR7GK8updBtHSq3MNM9rilsVCZPblc6YI='

# key64 = base64.urlsafe_b64encode(key)
# f = Fernet(key64)

# f = Fernet(key.decode('utf-8'))
f = Fernet(key)

# string = b'gAAAAABk7K-Q_Z-LkgXMVOu2BMC2nygo4gkySKAlLTICOZAqOcVPiOi2uzk26YNN07XlWtBv8HeQ8Qvf0kCkP7ItlB8DcQf16g=='
# string = b'gAAAAABk7PciK2ZU0XJnGUUpRAn7gAGEK82MIDMLDboFG4wo9wBfhvP_vKG2Ooi2y0lUbxPluOY4nNAEsgSfpsuMSz-1n5Bk6w=='
string = b'gAAAAABk7PciK2ZU0XJnGUUpRAn7gAGEK82MIDMLDboFG4wo9wBfhvP_vKG2Ooi2y0lUbxPluOY4nNAEsgSfpsuMSz-1n5Bk6w=='

message = "3@3.com"

# Encrypt the message
string = f.encrypt(message.encode())
# 
# Print the encrypted message
# print("Encrypted:", encrypted_message)

encrypted_string = string.decode('utf-8')

# Decrypt the string
# decrypted_string = f.decrypt(string).decode('utf-8')
# print("Decrypt:", decrypted_string)

print("Encrypt:", encrypted_string)