DEFAULT_NAME = "[name]"

names_list = open("./Input/Names/invited_names.txt", mode="r")


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace(DEFAULT_NAME, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)

