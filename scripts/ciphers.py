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


class xor_cipher:
    def encrypt_xor(text, key):
        """
        Encrypts the given text using the XOR cipher.

        Args:
            text (str): The text to be encrypted.
            key (int): The encryption key.

        Returns:
            str: The encrypted text.
        """
        encrypted_text = ""
        for char in text:
            encrypted_char = chr(ord(char) ^ key)
            encrypted_text += encrypted_char
        return encrypted_text

    def decrypt_xor(encrypted_text, key):
        """
        Decrypts the given encrypted text using the XOR cipher.

        Args:
            encrypted_text (str): The encrypted text to be decrypted.
            key (int): The encryption key.

        Returns:
            str: The decrypted text.
        """
        decrypted_text = ""
        for char in encrypted_text:
            decrypted_char = chr(ord(char) ^ key)
            decrypted_text += decrypted_char
        return decrypted_text


class atbash_cipher:
    def encrypt_atbash(text):
        """
        Encrypts the given text using the Atbash cipher.

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        encrypted_text = ""

        for char in text:
            if char.isalpha():
                if char.islower():
                    encrypted_char = chr(ord('z') - (ord(char) - ord('a')))
                else:
                    encrypted_char = chr(ord('Z') - (ord(char) - ord('A')))
            else:
                encrypted_char = char
            encrypted_text += encrypted_char

        return encrypted_text

    def decrypt_atbash(encrypted_text):
        """
        Decrypts the given encrypted text using the Atbash cipher.

        Args:
            encrypted_text (str): The encrypted text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        decrypted_text = atbash_cipher.encrypt_atbash(encrypted_text)

        return decrypted_text
