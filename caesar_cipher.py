from string import ascii_lowercase
import random


class CaesarCipher:

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

    def decrypt_string(self, key: int) -> str:
        """
        Decrypts the provided string from a caesar `cipher back` to `plain text`

        :param key: An integer value used to encrypt the text
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
