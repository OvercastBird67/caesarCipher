from encrypt_string import encrypting_string
from decrypt_string import decrypting_string


def print_menu() -> None:
    """
    Prints the menu of the program.
    """
    print("\tEnter\n'e' to encrypt\n'd' to decrypt\n'q' to quit")


def continue_or_terminate() -> int:
    """
    Asks the user weather they wish to continue or terminate the program.

    :return: 1 if they wish to continue otherwise 0 is returned.
    """
    print("\nDo you wish to continue (Y/N)?")
    while True:
        continue_program = input("-> ").casefold()
        if continue_program not in ['y', 'n']:
            print("\nPlease enter 'y' for yes and 'n' for no: ")
        else:
            break
    if continue_program == 'y':
        print()
        print_menu()
        return 1
    else:
        return 0


print_menu()
control_id_outer = 1
while control_id_outer != 0:
    control_id_inner = 0
    selection = input("-> ").casefold()
    while control_id_inner != 1:
        if selection in ["e", "d", "q"]:
            if selection == 'e':
                string_in = input("\nEnter the string to encrypt: ")
                encrypted_string = encrypting_string(string_in)
                print(f"""The encrypted string is: {encrypted_string}.""")
                if continue_or_terminate() == 0:
                    control_id_inner, control_id_outer = 1, 0
                else:
                    control_id_inner = 1
            elif selection == 'd':
                string_in = input("\nEnter the string to decrypt: ")
                print("Enter the key: ", end="")
                while True:
                    try:
                        key = int(input())
                        break
                    except ValueError:
                        print("Please enter a numerical value: ", end="")
                decrypted_string = decrypting_string(key, string_in)
                print(f"""The decrypted string is "{decrypted_string}".""")
                if continue_or_terminate() == 0:
                    control_id_inner, control_id_outer = 1, 0
                else:
                    control_id_inner = 1
            else:
                control_id_inner, control_id_outer = 1, 0
        else:
            selection = input("\nPlease select a operation from the provided options\n-> ")

print("\nProgram Terminated")
