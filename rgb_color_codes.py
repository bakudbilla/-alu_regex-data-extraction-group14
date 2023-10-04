import re

# Regex pattern
pattern = r'rgb\([0-255],\s[0-255],\s[0-255])'

# Sample API response with rgb codes
api_response = 
"""
set of rgb color codes:
rgb(29, 56, 129), rgb(61, 220, 220), rgb(144, 34, 183), rgb(243, 145, 7), rgb(245, 42, 42), rgb(98, 255, 300)
"""

rgb_color_codes = re.findall(pattern, api_response)
print(rgb_color_code)
