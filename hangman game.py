import random
import hangman_words
import hangman_art
print(hangman_art.logo)
lives=6
chosen_word = random.choice(hangman_words.word_list)
display = []
for letter in range(0, len(chosen_word)):
    display.append('_')
print(display)
chosen_word = list(chosen_word)
while display!=chosen_word and lives!=0:
    guess = input('Guess a letter: ')
    guess = guess.lower()
    for word in range(0, len(chosen_word)):
        if chosen_word[word] == guess:
            ind = word
            display[ind] = guess
    print(display)
    if guess not in chosen_word:
        print(f'{guess} is not in the chosen word')
        lives-=1
        print(hangman_art.stages[lives])
    else:
       lives=lives
       print(hangman_art.stages[lives])
if display==chosen_word:
    print('You have won')
elif lives==0:
    chosen_word=''.join(chosen_word)
    print('You have lose')
    print(f'The chosen word is {chosen_word}')

    