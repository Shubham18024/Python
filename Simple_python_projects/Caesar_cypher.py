art = '''
                                                                                                                                             
  ,ad8888ba,                                                             ,ad8888ba,                        88                                 
 d8"'    `"8b                                                           d8"'    `"8b                       88                                 
d8'                                                                    d8'                                 88                                 
88            ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,    88          8b       d8 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8    88          `8b     d8' 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88            Y8,          `8b   d8'  88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88             Y8a.    .a8P `8b,d8'   88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88              `"Y8888Y"'    Y88'    88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                       d8'     88                                             
                                                                                      d8'      88                                             
'''
print(art)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
    def encrypt(original_text,shift_amount):
        encoded_msg = ""
        for letter in original_text :
            if letter not in alphabet :
                encoded_msg += letter
            else :
                position = (alphabet.index(letter) + shift_amount) % len(alphabet)
                encoded_msg += alphabet[position]
        print(f"Here is the encoded result: {encoded_msg}")
        
    def decrypt(original_text,shift_amount):
        decoded_msg = ""
        for letter in original_text :
            if letter not in alphabet :
                decoded_msg += letter
            else :
                position = (alphabet.index(letter) - shift_amount) % len(alphabet)
                decoded_msg += alphabet[position]
        print(f"Here is the decoded result: {decoded_msg}")
        
    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)
    else :
        print("Please enter exactly \"encode\" or \"decode\"")
        
    
ans = "yes"
while ans.lower() == "yes" :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(direction,text,shift)
    
    ans = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if ans != "yes":
         print("GoodBye 😎")

