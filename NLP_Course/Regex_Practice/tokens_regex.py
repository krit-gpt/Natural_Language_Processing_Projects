# Search for the first occurrence of "coconuts" in scene_one: match
match = re.search("coconuts", scene_one)

# Print the start and end indexes of match
print(match.start(), match.end())

# Write a regular expression to search for anything in square brackets: pattern1
pattern = r"\[.*\]"
pattern1 = re.search(pattern, scene_one)
print(pattern1)

# Use re.search to find the first text in square brackets
print(re.search(pattern1[0], scene_one ))

# Find the script notation at the beginning of the fourth sentence and print it
print(sentences[3])
pattern2 = r"[\w\s]+"
print(re.match(pattern2, sentences[3]))
