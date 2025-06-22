art = '''
  .oooooo.                                              .oooooo.                          oooo                         
 d8P'  `Y8b                                            d8P'  `Y8b                          888                           
888           .ooooo.   .oooo.o  .oooo.   oooo d8b    888          oooo    ooo oo.ooooo.   888 .oo.    .ooooo.  oooo d8b 
888          d88' `88b d88(  "8 `P  )88b  `888""8P    888           `88.  .8'   888' `88b  888P"Y88b  d88' `88b `888""8P 
888          888ooo888 `"Y88b.   .oP"888   888        888            `88..8'    888   888  888   888  888ooo888  888     
`88b    ooo  888    .o o.  )88b d8(  888   888        `88b    ooo     `888'     888   888  888   888  888    .o  888     
 `Y8bood8P'  `Y8bod8P' 8""888P' `Y888""8o d888b        `Y8bood8P'      .8'      888bod8P' o888o o888o `Y8bod8P' d888b    
                                                                   .o..P'       888                                      
                                                                   `Y8P'       o888o                                                                                                                                                          

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

