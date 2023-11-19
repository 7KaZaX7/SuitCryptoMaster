class caesar_cipher:
    def encrypt_caesar(text, key):
        """
        Encrypts the given text using the Caesar cipher.

        Args:
            text (str): The text to be encrypted.
            key (int): The encryption key.

        Returns:
            str: The encrypted text.
        """
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr(
                    ((ord(char) - shift + key) % 26) + shift)
            else:
                encrypted_char = char
            encrypted_text += encrypted_char
        return encrypted_text

    def decrypt_caesar(encrypted_text, key):
        """
        Decrypts the given encrypted text using the Caesar cipher.

        Args:
            encrypted_text (str): The encrypted text to be decrypted.
            key (int): The encryption key.

        Returns:
            str: The decrypted text.
        """
        decrypted_text = ""
        for char in encrypted_text:
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')
                decrypted_char = chr(
                    ((ord(char) - shift - key) % 26) + shift)
            else:
                decrypted_char = char
            decrypted_text += decrypted_char
        return decrypted_text
