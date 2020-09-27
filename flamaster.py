word = "ABBCCCDDDDEEEEEFGGHIIJKKKL"

def flamaster(word: str):
    letters = []

    for letter in word:
        letters.append(letter)

    new_word = []

    for letter in letters:
        if letter in letters:
            if letters.count(letter) > 2:
                letter = letter + str(letters.count(letter)) 
                if new_word.count(letter) >= 1:
                    letter = ""
                    
            new_word.append(letter)

    optimal_word = ""

    for letter in new_word:
        optimal_word += letter

    return optimal_word
try:
    print(flamaster(word))
except TypeError:
    print("Input must be a string")