import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
new_dict= {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input=input("Enter the word: ").upper()
    try:
        output=[new_dict[letter] for letter in user_input]
    except KeyError:
        print("Please enter a valid name")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()
