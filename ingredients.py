import re

data = "Here are the ingredients: beef, pork, chips, rice, and beans."

# Use a regular expression to match the ingredients format.
ingredient_pattern = r'ingredients:\s*([\w\s,]+)'

# Find all matches in the data using re.search().
match = re.search(ingredient_pattern, data, re.IGNORECASE)

if match:
    ingredients = match.group(1).split(', ')
    print(ingredients)
else:
    print("No ingredients found.")

