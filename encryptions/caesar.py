def caesar_cipher(message: str, shift: int) -> str:
    # Initialize the encrypted message as an empty string
    encrypted_message = ""

    # Iterate through each character in the message
    for char in message:
        # Check if the character is an ASCII character
        if char.isascii():
            # Convert the character to its ASCII code
            ascii_code = ord(char)

            # Shift the ASCII code by the specified number of characters
            ascii_code += shift

            # Use a while loop to handle ASCII codes that are out of range
            while ascii_code < 32 or ascii_code > 126:
                if ascii_code < 32:
                    ascii_code += 95
                elif ascii_code > 126:
                    ascii_code -= 95

            # Convert the ASCII code back to a character
            encrypted_char = chr(ascii_code)
        else:
            # If the character is not an ASCII character, leave it unchanged
            encrypted_char = char

        # Add the encrypted character to the encrypted message
        encrypted_message += encrypted_char

    return encrypted_message
