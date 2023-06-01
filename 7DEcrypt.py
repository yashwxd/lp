def decrypt_transposition(encrypted_message, key):
    # Calculate the number of rows required
    num_rows = (len(encrypted_message) + key - 1) // key
    # Create the decrypted message
    decrypted_message = ''
    for row in range(num_rows):
        for col in range(key):
            index = col * num_rows + row
            if index < len(encrypted_message):
                decrypted_message += encrypted_message[index]
    return decrypted_message

# Test the decryption function
encrypted_message = input("Enter the encrypted message: ")
decryption_key = int(input("Enter the decryption key: "))
decrypted_message = decrypt_transposition(encrypted_message, decryption_key)
print("Decrypted message:", decrypted_message)
