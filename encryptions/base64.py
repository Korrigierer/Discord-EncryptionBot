import base64
import binascii


def base64_encode(message: str) -> str:
    # Convert the string to a bytes object
    bytes_object = bytes(message, "utf-8")

    # Encode the bytes object in base64
    encoded_string = base64.b64encode(bytes_object)

    # Return the encoded string as a string
    return encoded_string.decode("utf-8")


def base64_decode(message: str) -> str:
    # Convert the encoded string to a bytes object
    bytes_object = message.encode("utf-8")

    # Use a try-except block to handle any decoding errors
    try:
        # Decode the bytes object in base64
        decoded_string = base64.b64decode(bytes_object)

        # Return the decoded string as a string
        return decoded_string.decode("utf-8")
    except binascii.Error:
        # If an error occurred, return an empty string
        return ""
