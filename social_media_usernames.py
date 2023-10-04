import re

# Example API response
api_response = "Hello! Check out my social media profiles: @user123 on Twitter and @john_doe456 on Instagram."

# Define the regex pattern
pattern = r'@([a-zA-Z0-9]+)'

# Find all matches in the API response
matches = re.findall(pattern, api_response)

# Print the extracted usernames
print(matches)
