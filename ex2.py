def change_word(text, letter, replacement):
    words = text.split()
    count_before = len(words)

    new_words = [word.replace(letter, replacement) for word in words]
    count_after = len(new_words)

    new_text = ' '.join(new_words)
    return new_text, count_before, count_after

# Input text
text = input("Input text: ")

# Count number text
words_before = len(text.split())
print("Numbers text before:", words_before)

# Input the numbers text replace
letter = input("Replace the numbers text: ")

# Input the text replace
replacement = input("Input text replace: ")

# Replaced and count numbers text current
new_text, words_before, words_after = change_word(text, letter, replacement)
print("Current text:", words_after)

# Show the information the word_before and after
print("Length of original text is::", words_before)
print("Length of modified text is:", words_after)
print("Modifired text:", replacement)
