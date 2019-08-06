#!/usr/bin/python3.7
import json
from difflib import SequenceMatcher as match
import pprint
import textwrap 

pretty = pprint.PrettyPrinter( indent= 4, width= 80)

data_path = "./resources/data.json" 
# Read the data and parse it as a complex variable
data = json.load(open(data_path))
# pretty.pprint(data)

def sep(character, n):
	return character * n
	

# Get the definition(s) of the word
def get_definitions(word):
	
	if word not in data.keys():
		# Check for the lower case
		if word.lower() in data.keys():
			word = word.lower()

		# Check for the upper case
		elif word.upper() in data.keys():
			word = word.upper()

		# Check for the upper case
		elif word.title() in data.keys():
			word = word.title()

		# Check for closest match
		else:
			max_match_ratio = 0
			new_word = ""

			for key in data.keys():
				match_ratio = match(isjunk=None, a=word.lower(), b=key.lower()).ratio() * 100
				if match_ratio > 70 and match_ratio > max_match_ratio:
					max_match_ratio = match_ratio
					new_word = key
					# print(key, match_ratio)

			if max_match_ratio:
				if True if input("Word not found! Did you mean '" + new_word + "'? (y/n) : ").lower() == "y" else False:
					word = new_word
				else:
					return []
			else:
				# Word not found. Closest match doesn't pass the threshold match percentage
				print("The word doesn't exist in the dictionary! Kindly check the spellings!") 
				return []
	
	# Display number of definitions found
	print("Definitions found for", word, ":", len(data[word]))
	print(sep("-", 80))

	return data[word]

while True:
	print(sep("=", 80))
	# Get the input from the user
	word = input("Enter the word you want to check the definition of : ")
	# Get the definition(s) of the word
	definitions = get_definitions(word)
	
	if len(definitions):
		# Display all the definitions of the word
		for (index, definition) in enumerate(definitions):
			print(str(index + 1) + " :", end = " ")
			print("\n".join(textwrap.wrap(definition, width= 76)))

		print(sep("=", 80))
	
	if not input("Do you want to continue? (y/n) : ").lower() == "y":
		exit(0)
