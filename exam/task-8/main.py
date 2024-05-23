# Function: Pair Characters
# Objective: Write a function `pair_characters` that takes a string and returns a list of two-character pairs.
# If the string has an odd number of characters, append an asterisk '*' to the final pair to ensure all pairs consist of two characters.
# Parameters:
# - word: A string to be processed into pairs.
# Returns:
# - A list of two-character pairs.

def pair_characters(word):
    pairs = []
    
    for i in range(0, len(word), 2):
        if i+1 < len(word):
            pairs.append(word[i:i+2])
        else:
            pairs.append(word[i] + '*')
    
    return pairs

# Example usages:
print(pair_characters("hello"))  # Output: ['he', 'll', 'o*']
print(pair_characters("characters"))  # Output: ['ch', 'ar', 'ac', 'te', 'rs']
print(pair_characters("abcdef"))  # Output: ['ab', 'cd', 'ef']
print(pair_characters("a"))  # Output: ['a*']
