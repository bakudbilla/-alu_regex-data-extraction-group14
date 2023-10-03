#!/bin/bash
import re
restaurant_names = [
    "Osteria Francescana - Italian",
    "Tasty queen - Ghanaian",
    "The place - Nigerian",
"McDonald's-American"]

# Regular expression pattern
pattern = r"^(.*?) - (.*)$"

# Iterate through API responses
for restaurant  in restaurant_names:
    match = re.match(pattern, restaurant)
    if match:
        restaurant_name = match.group(1)
        cuisine = match.group(2)
        print(f"Restaurant Name: {restaurant_name}, Cuisine: {cuisine}")
    else:
        print(f"No match found for: {restaurant}")
