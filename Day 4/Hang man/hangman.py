import random
from symbols import stages
from symbols import logo
from wordlist import word_list
print(logo)
lives=7
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display=[]

for i in range(len(chosen_word)):
  display.append("_")
print(display)

end=True
while end:
  guess = input("Guess a letter: ").lower()
  if guess in display:
      print(f"The letter {guess} is already obtained.")
  for i in range(len(chosen_word)):
      if guess == chosen_word[i]:
          display[i]=guess
  print(display)
  if guess not in chosen_word:
    print(f"The letter {guess} is not in the word.")
    print(stages[lives-1])
    lives=lives-1
  if lives == 0:
    end=False
    print("You lose")
  if "_" not in display:
    end=False
    print("You win")

