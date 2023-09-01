from cryptography.fernet import Fernet

key = b'R_vUYsaQQkyR7GK8updBtHSq3MNM9rilsVCZPblc6YI='

# encrypted_content = b'gAAAAABk7K-Q_Z-LkgXMVOu2BMC2nygo4gkySKAlLTICOZAqOcVPiOi2uzk26YNN07XlWtBv8HeQ8Qvf0kCkP7ItlB8DcQf16g=='
encrypted_content = 'gAAAAABk7PciK2ZU0XJnGUUpRAn7gAGEK82MIDMLDboFG4wo9wBfhvP_vKG2Ooi2y0lUbxPluOY4nNAEsgSfpsuMSz-1n5Bk6w=='


f = Fernet(key)
decrypted_content = f.decrypt(encrypted_content).decode('utf-8')
print(decrypted_content)