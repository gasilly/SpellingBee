import enchant
import string
import numpy
import random

def main():
    word_count = 0
    used_words = []
    valid_letters = numpy.random.choice(list(string.ascii_lowercase), 7, False)
    key_letter = random.choice(valid_letters)
    ench = enchant.Dict("en_US")
    while True:
        print("Letters: ", valid_letters)
        print("Key Letter:", key_letter)
        word = str(input("Please enter a valid word or q to quit "))
        if(ench.check(word) and (len(word) > 3) and ((word in used_words) == False) and (word.find(key_letter) > 0) and all((letters in valid_letters for letters in word))):
            word_count += 1
            used_words.append(word)
        elif(word == "q"):
            break
        print("Total Words: ", word_count)

if __name__=="__main__":
    main()