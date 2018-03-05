'''
NER via ensemble model
In the final exercise of this NER chapter, you'll use the spacy and polyglot models to extract the best entities possible from English text. Here, you'll be using a long Medium post with a mixture of more formal article writing and informal. You'll find entities using both spacy and polyglot and choose only entities identified by both to create a sort of ensemble model.

In this exercise, you have access to the polyglot Text class and the loaded english vectors for spacy in nlp. You also have the article text in article. The set of polyglot entities have been computed and are available in poly_ents. Your task is to compute the spacy entities and then find the intersection between the polyglot entities and the spacy entities.

Here, you'll be working with sets. A set comprehension looks exactly like a list comprehension, with the exception that it uses the set syntax markers {}.

'''

# Create a set of spaCy entities keeping only their text: spacy_ents
spacy_ents = {e.text for e in doc.ents} 

# Create a set of the intersection between the spacy and polyglot entities: ensemble_ents
ensemble_ents = spacy_ents.intersection(poly_ents)

# Print the common entities
print(ensemble_ents)

# Calculate the number of entities not included in the new ensemble set of entities: num_left_out
num_left_out = len(spacy_ents.union(poly_ents)) - len(ensemble_ents)
print(num_left_out)

'''

{'Tal Hassner', 'Francis Galton', 'Papuans', 'Manning', 'George Gliddon', 'Charina Choi', 'Guangdong', 'Georg Christoph Lichtenberg', 'Ernst Haeckel', 'England', 'Pavia', 'Darwin', 'Temple University', 'Byron', 'Roberts', 'China', 'Israeli', 'Swiss', 'Naples', 'Giuseppe Villella', 'Geoffrey Hinton', 'Australia', 'California', 'Lombroso', 'Tobias Weyand', 'Jason Friedenfelds', 'Nazi', 'Gliddon', 'James Weidmann', 'Kathryn Hume', 'Zhang’s', 'Josiah Nott', 'Ilya Sutskever', 'Brian Holtz', 'Howard', 'Stockholm', 'Alison Lentz', 'Atlanta', 'Liaoning', 'Nixon', 'Stephen Jay Gould', 'Fink', 'Mike Burton', 'Zhang', 'Caucasian', 'Thomas Clarkson', 'Marco Polo', 'Samuel Morton', 'William Shakespeare', 'Pieter Camper', 'Alex Krizhevsky', 'Plato', '”', 'Gil Levi', '“', 'Google', 'Clarkson', 'John Howard', 'Chuck Close', 'Wu', 'Italy', 'Jiangsu', 'Ilya Kostrikov', 'CNN', 'Cesare Lombroso', 'Isaac Newton'}
250
'''
