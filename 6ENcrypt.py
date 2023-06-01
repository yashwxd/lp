def encrypt_transposition(message, key):
    # Remove spaces from the message
    message = message.replace(" ", "")
    # Calculate the number of rows required
    num_rows = (len(message) + key - 1) // key
    # Pad the message if needed
    padded_message = message.ljust(num_rows * key, ' ')
    # Create the encrypted message
    encrypted_message = ''
    for col in range(key):
        for row in range(num_rows):
            index = row * key + col
            encrypted_message += padded_message[index]
    return encrypted_message

# Test the encryption function
plaintext = input("Enter the plaintext message: ")
encryption_key = int(input("Enter the encryption key: "))
encrypted_message = encrypt_transposition(plaintext, encryption_key)
print("Encrypted message:", encrypted_message)