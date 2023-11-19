import pybase64


class base64_coder:
    def encode_base64(text):
        """
        Encode the given text using base64 encoding.

        Args:
            text (str): The text to be encoded.

        Returns:
            str: The encoded text.
        """
        encoded_bytes = pybase64.b64encode(text.encode('utf-8'))
        encoded_text = encoded_bytes.decode('utf-8')
        return encoded_text

    def decode_base64(encoded_text):
        """
        Decode the given base64 encoded text.

        Args:
            encoded_text (str): The base64 encoded text.

        Returns:
            str: The decoded text, or "Invalid decoded text" if decoding fails.
        """
        try:
            decoded_bytes = pybase64.b64decode(encoded_text.encode('utf-8'))
            decoded_text = decoded_bytes.decode('utf-8')
            return decoded_text
        except Exception:
            return f"Invalid decoded text"


class morse_code_coder:
    global morse_code_dict
    global morse_code_dict_reverse

    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': '/'
    }
    morse_code_dict_reverse = {
        value: key for key, value in morse_code_dict.items()}

    def encoder_morse_code(text):
        """
        Encode the given text using Morse code.

        Args:
            text (str): The text to be encoded.

        Returns:
            str: The encoded text.
        """
        text = text.upper()
        encoded_message = ""
        for char in text:
            if char in morse_code_dict:
                encoded_message += morse_code_dict[char] + " "
            else:
                encoded_message += char
        return encoded_message

    def decoder_morse_code(encoded_text):
        """
        Decode the given Morse code.

        Args:
            encoded_text (str): The Morse code to be decoded.

        Returns:
            str: The decoded text.
        """
        morse_code_list = encoded_text.split()
        decoded_message = ""
        for code in morse_code_list:
            if code in morse_code_dict_reverse:
                decoded_message += morse_code_dict_reverse[code]
            else:
                decoded_message += " "
        return decoded_message


class bacon_coder:
    global bacon_dict_reverse
    global bacon_dict

    bacon_dict = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
        'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
        'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
        'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
        'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA',
        'Z': 'BBAAB', ' ': ' '
    }
    bacon_dict_reverse = {
        value: key for key, value in bacon_dict.items()}

    def encoder_bacon(text):
        """
        Encodes the given text using Bacon's cipher encoding.

        Args:
            text (str): The text to encode.

        Returns:
            str: The encoded text.
        """
        text = text.upper()

        encoded_text = ''
        for char in text:
            if char in bacon_dict:
                encoded_text += bacon_dict[char]

        return encoded_text

    def decoder_bacon(encoded_text):
        """
        Decodes the given Bacon's cipher encoded text.

        Args:
            encoded_text (str): The encoded text.

        Returns:
            str: The decoded text.
        """
        decoded_text = ''
        encoded_text = encoded_text.replace(" ", "")
        try:
            for i in range(0, len(encoded_text), 5):
                chunk = encoded_text[i:i + 5]
                if chunk in bacon_dict_reverse:
                    decoded_text += bacon_dict_reverse[chunk]
            if decoded_text != '':
                return decoded_text
            else:
                return "Invalid encoded text"
        except:
            return "Invalid encoded text"


class ascii_coder:
    def encoder_ascii(text):
        """
        Encodes the given text using ASCII encoding.

        Args:
            text (str): The text to encode.

        Returns:
            str: The encoded text.
        """
        encoded_text = ""
        for char in text:
            encoded_text += str(ord(char)) + " "
        return encoded_text.strip()

    def decoder_ascii(encoded_text):
        """
        Decodes the given ASCII encoded text.

        Args:
            encoded_text (str): The encoded text.

        Returns:
            str: The decoded text.
        """
        parts = encoded_text.split()
        decoded_text = ""
        for part in parts:
            try:
                char_code = int(part)
                decoded_text += chr(char_code)
            except ValueError:
                decoded_text += " "
        return decoded_text
