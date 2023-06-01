def encrypt_transposition(plaintext, key):
    ciphertext = ''
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext += plaintext[pointer]
            pointer += key
    return ciphertext


# Test the encryption function
plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key: "))

ciphertext = encrypt_transposition(plaintext, key)
print("Encrypted ciphertext:", ciphertext)