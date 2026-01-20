#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as invited_names:
    names=invited_names.readlines()
with open("./Input/Letters/starting_letter.txt") as starting_letters:
    letters=starting_letters.read()
for name in names:
    new_letters=letters.replace(PLACEHOLDER, name)
    stripped_name=name.strip()
    with open(f"send_to_{stripped_name}", mode="w") as file1:
        file1.write(new_letters)

# send_letter = letter.readlines()
# read_letter = str(send_letter)
# for name in names:
#     read_letter.replace(name,"[name]")
