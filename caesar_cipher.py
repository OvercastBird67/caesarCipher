from string import ascii_lowercase
import random


class CaesarCipher:
    """
    Class to represent the encryption and decryption of a string using `Caesar Cipher`
    Consider the string `ABeD`, assuming the key to be `1`, the caesar cipher created will be `BCFE`.
    Inversely if the entered string is `BCfE` and key is specified to be `1` then the result will be `ABeD`

    The key is auto-generated during run-time and is `not to be provided` while calling the `encrypt_string` method.

    However while calling the `decrypt_string` method the key is to be `explicitly provided by the user`, otherwise the
    value will default to `1`.

    Attributes:
        string (str): The string passed, which is to be encrypted/decrypted
        len_string (int): Length of the string to be encrypted/decrypted
        alpha_list (list): A list containing all the alphabets in lowercase
        len_alpha_list (int): Length of the alpha_list

    Methods:
        encrypt_string: Treats the entered string as `plain text` and converts it `cipher text`
        decrypt_string: Treats the entered string as `cipher text` and converts it to `plain text`
    """

    def __init__(self, string: str) -> None:
        """
        Initializes the object and assigns the passed string value to a variable

        :param string: The passed string that is to be converted
        """
        self.string = string
        self.len_string = len(self.string)
        self.alpha_list = list(ascii_lowercase)
        self.len_alpha_list = len(self.alpha_list)

    def encrypt_string(self) -> tuple:
        """
        Encrypts the provided string from `plain text` to a `caesar cipher`

        :return: A tuple containing the key and the encrypted string
        """
        key = random.randint(1, 5)
        encrypted_string = ""
        index_of_string = 0

        while index_of_string < self.len_string:
            for index, value in enumerate(self.alpha_list):
                if self.string[index_of_string].casefold() not in self.alpha_list:
                    encrypted_string += self.string[index_of_string]
                    break
                elif self.string[index_of_string].casefold() == value:
                    is_upper = True if self.string[index_of_string].isupper() else False
                    new_index = \
                        (index + key) - self.len_alpha_list if index + key >= self.len_alpha_list else index + key
                    encrypted_string += self.alpha_list[new_index].upper() if is_upper else self.alpha_list[new_index]
                    break
            index_of_string += 1

        return key, encrypted_string

    def decrypt_string(self, key: int = 1) -> str:
        """
        Decrypts the provided string from a caesar `cipher back` to `plain text`

        :param key: An integer value used to decrypt the text
                    If not provided, will default to `1`
        :return: A string, which contains the plain text for the received caesar cipher
        """
        decrypted_string = ""
        index_of_string = 0

        while index_of_string < self.len_string:
            for index, value in enumerate(self.alpha_list):
                if self.string[index_of_string].casefold() not in self.alpha_list:
                    decrypted_string += self.string[index_of_string]
                    break
                elif self.string[index_of_string].casefold() == value:
                    is_upper = True if self.string[index_of_string].isupper() else False
                    new_index = (index - key) + self.len_alpha_list if index - key < 0 else index - key
                    decrypted_string += self.alpha_list[new_index].upper() if is_upper else self.alpha_list[new_index]
                    break
            index_of_string += 1

        return decrypted_string


if __name__ == "__main__":
    key_in, en_string = CaesarCipher("Hello!").encrypt_string()
    print(en_string)
    print(CaesarCipher(en_string).decrypt_string(key_in))
