# Task 2: String Formatting
# Create a string named template with the following content: "Hello, {name}. Welcome to {place}."
# Use the format() function to replace {name} with "Alice" and {place} with "Wonderland". Store the result in a variable named formatted_string and print it.

template = "Hello, {name}. Welcome to {place}."
formatted_string = template.format(name="Alice", place="Wonderland")
print(formatted_string)

# =================================================================

# Task 3: Joining Strings
# Create a list named words that contains the following strings: "apple", "banana", "cherry".
# Use the join() function to combine these words into a single string, separated by a comma and a space ", ". Store the result in a variable named fruit_string and print it.

words = ["apple", "banana", "cherry"]
fruit_string = ", ".join(words)
print(fruit_string)

# =================================================================

# Task 4: Splitting a String
# Create a string named sentence with the following content: "The quick brown fox jumps over the lazy dog."
# Use the split() function to split the sentence into a list of words. Store the result in a variable named words_list and print it.

sentence = "The quick brown fox jumps over the lazy dog."
words_list = sentence.split()
print(words_list)

# =================================================================

# Task 5: Replacing Substrings
# Create a string named quote with the following content: "To be or not to be, that is the question."
# Use the replace() function to replace the word "be" with "code". Store the result in a variable named modified_quote and print it.

quote = "To be or not to be, that is the question."
modified_quote = quote.replace("be", "code")
print(modified_quote)

# =================================================================

# Task 6: Converting to Lowercase
# Create a string named mixed_case with the following content: "PyThOn Is AwEsOmE!"
# Use the lower() function to convert the entire string to lowercase. Store the result in a variable named lowercase_string and print it.

mixed_case = "PyThOn Is AwEsOmE!"
lowercase_string = mixed_case.lower()
print(lowercase_string)

# =================================================================

# Task 7: Converting to Uppercase
# Create a string named greeting with the following content: "good morning"
# Use the upper() function to convert the entire string to uppercase. Store the result in a variable named uppercase_greeting and print it.

greeting = "good morning"
uppercase_greeting = greeting.upper()
print(uppercase_greeting)
