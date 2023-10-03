import re

# Regex pattern
pattern = r'\b[A-Z]{3}\d{3}\b'

# Sample API response containing product codes
api_response = """
Some product codes:
ABC123, XYZ456, DEF789, GHI234, JKL567
"""

product_codes = re.findall(pattern, api_response)
print(product_codes)
