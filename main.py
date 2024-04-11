def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shifting each digit up by 3 numbers
        encoded_password += encoded_digit
    return encoded_password


def decode(password):
    decode_password = encode(password)
    for digit in password:
        decoded_digit = str((int(digit) - 3) % 10)
        decode_password += decoded_digit
    return decode_password


if __name__ == "__main__":
    while True:
        menu()
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid password format.")
            else:
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
        elif option == "2":
            decode_password = decode(password)
            print(f"The encoded password is", encode(password), "and the original password is", decode(password), ".")
        elif option == "3":
            break
