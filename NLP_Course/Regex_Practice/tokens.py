# Import necessary modules
from nltk import word_tokenize
from nltk import sent_tokenize

#scene_one is a group of sentences!
# Split scene_one into sentences: sentences
sentences = sent_tokenize(scene_one)
print(sentences)

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])
print(tokenized_sent)

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)
