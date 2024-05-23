# Function: Sort by Length
# Objective: Write a function `sort_by_length` that sorts a list of strings by the length of the strings in ascending order.
# Parameters:
# - strings: A list of strings.
# Returns:
# - A list of strings sorted by their length.

def sort_by_length(strings):
    return sorted(strings, key=len)

# Example usages:
print(sort_by_length(["a", "ccc", "dddd", "bb"]))  # Output: ["a", "bb", "ccc", "dddd"]
print(sort_by_length(["apple", "pie", "shortcake"]))  # Output: ["pie", "apple", "shortcake"]
print(sort_by_length(["may", "april", "september", "august"]))  # Output: ["may", "april", "august", "september"]
print(sort_by_length([]))  # Output: [], handling the empty list case
