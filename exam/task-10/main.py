# Function: Generate Hangman Phrase
# Objective: Create a function `generate_hangman_phrase` that takes a phrase and a list of guessed letters,
# and returns a string with hyphens for every letter not guessed, while showing the letters that were guessed.
# Parameters:
# - phrase: A string representing the phrase to be guessed.
# - guessed_letters: A list of characters representing the letters that have been guessed so far.
# Returns:
# - A string representing the current state of the phrase with unguessed letters replaced by hyphens.

def generate_hangman_phrase(phrase, guessed_letters):
    result = ""
    for char in phrase:
        if char.isalpha():
            if char.lower() in guessed_letters:
                result += char
            else:
                result += "-"
        else:
            result += char
            
    return result

# Example usage:
print(generate_hangman_phrase("hello world", ['e', 'o']))
print(generate_hangman_phrase("Happy Birthday", ['a', 'p', 'y']))
print(generate_hangman_phrase("OpenAI GPT-3", ['p', 't', 'g', '3']))
