import random
from alphabet_list import alpha_list


def encrypting_string(string_to_encode: str) -> (str, int):
    """
    Converts the entered sentence to a `caesar cipher`.
    Consider the string "ABED", assuming the key to be '1',
    the caesar cipher created will be "BCFE".

    :param string_to_encode: The string to be converted to `caesar cipher`.
    :return: A tuple containing the encrypted string and the key used to encrypt the original string.
    """
    key = random.randint(1, 5)
    encrypted_string = ""
    len_string_to_encrypt, len_of_alpha_list = len(string_to_encode), len(alpha_list)
    index_of_string = 0

    while index_of_string < len_string_to_encrypt:
        _index = None
        for index, value in enumerate(alpha_list):
            if string_to_encode[index_of_string].casefold() not in alpha_list:
                encrypted_string += string_to_encode[index_of_string]
                break
            elif string_to_encode[index_of_string].casefold() == value:
                is_upper = True if string_to_encode[index_of_string].isupper() else False
                if index + key >= len_of_alpha_list:
                    _index = (index + key) - len_of_alpha_list
                else:
                    _index = index + key
                encrypted_string += alpha_list[_index].upper() if is_upper else alpha_list[_index]
                break
        index_of_string += 1

    return {key: encrypted_string}
