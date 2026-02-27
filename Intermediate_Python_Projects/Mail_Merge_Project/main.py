with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.read()
            


for name in names :
     clean_name = name.strip("\n")
     content = letter_template.replace("[name]", clean_name)
     with open(f"Output/ReadyToSend/letter_for_{clean_name}.docx", mode="w") as new_file:
         new_file.write(content)
