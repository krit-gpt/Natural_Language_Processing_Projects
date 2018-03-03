# Import the regex module
import re

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = re.split('\.|\?|\!', my_string)
print(sentence_endings)

capitalized_words = re.findall('[A-Z]\w+', my_string)
print(capitalized_words)



# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, my_string))

# Find all digits in my_string and print the result
digits = r"\d+"
print(re.findall(digits, my_string))
