def create_substitution_key():
    # Create a simple substitution key (this can be random or based on a specific pattern)
    original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    return dict(zip(original, key))

def substitution_encrypt(plain_text, key):
    encrypted_text = ''
    for char in plain_text:
        if char.isupper():
            encrypted_text += key[char]
        elif char.islower():
            encrypted_text += key[char.upper()].lower()  # Preserve case
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def substitution_decrypt(encrypted_text, key):
    reverse_key = {v: k for k, v in key.items()}
    decrypted_text = ''
    for char in encrypted_text:
        if char.isupper():
            decrypted_text += reverse_key[char]
        elif char.islower():
            decrypted_text += reverse_key[char.upper()].lower()  # Preserve case
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

# Example usage:
message = "Hello, World!"
key = create_substitution_key()

encrypted = substitution_encrypt(message, key)
decrypted = substitution_decrypt(encrypted, key)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")
