import enchant
import sys

#accept the movie name from command line arguments
input_word = sys.argv[1]

#load the personal word list dictionary

my_dict = enchant.PyPWL("ingredientslist.txt")
ingredients_dict = enchant.PyPWL("ingredientslist.txt")

#get suggestions for the input word
suggestions = my_dict.suggest(input_word)

#check if the word exists in the dictionary

word_exists = ingredients_dict.check(input_word)
print("word exists: ", word_exists)

print ("input:", input_word)
print("suggestions:", suggestions)

if not word_exists:

#get suggestions for the input word if the word doesn't exist in the dictionary
	suggestions = ingredients_dict.suggest(input_word)

	print ("input:", input_word)

	print("suggestions:", suggestions)