# Function: Calculate Discounted Price
# Objective: Write a function `calculate_discounted_price` that computes the final price of an item
# after applying a discount percentage.
# Parameters:
# - original_price: An integer representing the original price of the item.
# - discount_percentage: An integer representing the discount rate applied to the original price.
# Returns:
# - The final price after the discount, as a float rounded to two decimal places.

def calculate_discounted_price(original_price, discount_percentage):
    discount_factor = 1 - (discount_percentage / 100)
    final_price = original_price * discount_factor

    return round(final_price, 2)

original_price = 100.0
discount_percentage = 20
final_price = calculate_discounted_price(original_price, discount_percentage)
print(f"The final price after {discount_percentage}% discount is {final_price:.2f}")
