# Function: Invert RGB Color
# Objective: Write a function `color_invert` that takes an RGB color tuple and returns the inverted color tuple.
# Parameters:
# - color: A tuple with three integers representing the RGB values of the color (each value ranges from 0 to 255).
# Returns:
# - A tuple representing the inverted RGB values.

def color_invert(color):
    inverted_color = tuple(255 - value for value in color)

    return inverted_color

color = (100, 150, 200)
inverted_color = color_invert(color)
print(f"The inverted color is {inverted_color}")
