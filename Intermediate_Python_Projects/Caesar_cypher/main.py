from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        alphabet_index = alphabet.index(char)
        new_index = (alphabet_index + shift) % 26
        cipher_text += alphabet[new_index]
    return cipher_text

def decrypt(text, shift):
    decipher_text = ""
    for char in text:
        alphabet_index = alphabet.index(char)
        new_index = (alphabet_index - shift) % 26
        decipher_text += alphabet[new_index]
    return decipher_text

def main():
    direct = input("Press '1' to encrypt, press '2' to decrypt:\n")
    user_input = input("Type your message: ").lower()
    shift_amount = int(input("Type the shift number: "))
    if direct == "1":
        encrypted_message = encrypt(user_input, shift_amount)
        print(f"The encrypted message is: {encrypted_message}")
    elif direct == "2":
        decrypted_message = decrypt(user_input, shift_amount)
        print(f"The decrypted message is: {decrypted_message}")
    else:
        print("Invalid input. Please type '1' or '2'.")

if __name__ == "__main__":
    while True:
        main()
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if again == "no":
            print("Goodbye!")
            break