import pandas
data=pandas.read_csv(r"nato_phonetic_alphabet.csv")
phonetic_dic={row.letter:row.code for (index,row)in data.iterrows()}
user_input=input("Enter a word: ").upper()
output=[phonetic_dic[letter] for letter in user_input]
print(output)