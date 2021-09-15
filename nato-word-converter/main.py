import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter:row.code for index, row in data.iterrows()}
print(nato_alphabet.items())

to_convert = input("Type the name or word: ").upper()
converted_word = [nato_alphabet[letter] for letter in to_convert]
print(converted_word)
