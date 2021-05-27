from alphabet_list import alpha_list


def decrypting_string(key: int, string_to_decrypt: str) -> str:
    """
    Decrypts the sentence from `caesar cipher` to `plain readable text`.

    :param key: The numerical `key` value used to encrypt the string
    :param string_to_decrypt: The string that is to be decrypted
    :return: The decrypted string
    """
    decrypted_string = ""
    len_string_to_decrypt, len_alpha_list = len(string_to_decrypt), len(alpha_list)
    index_of_string = 0

    while index_of_string < len_string_to_decrypt:
        for index, value in enumerate(alpha_list):
            _index = None
            if string_to_decrypt[index_of_string].casefold() not in alpha_list:
                decrypted_string += string_to_decrypt[index_of_string]
                break
            elif string_to_decrypt[index_of_string].casefold() == value:
                is_upper = True if string_to_decrypt[index_of_string].isupper() else False
                if index - key < 0:
                    _index = (index - key) + len_alpha_list
                else:
                    _index = index - key
                decrypted_string += alpha_list[_index].upper() if is_upper else alpha_list[_index]
                break
        index_of_string += 1

    return decrypted_string
