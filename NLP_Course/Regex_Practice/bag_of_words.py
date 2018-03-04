# Import Counter
from collections import Counter

# Tokenize the article: tokens
tokens = Counter(word_tokenize(article))

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]
print(lower_tokens)

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)
print(bow_simple)

# Print the 10 most common tokens
print(bow_simple.most_common(10))
