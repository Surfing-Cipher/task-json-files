import json

# Given URL shortening function


def shorten_url(long_url):
    return long_url.split("/")[-1].split("?")[0]


# Load JSON data from a file
with open('lp-data.json') as file:
    jsonData = json.load(file)

# Combine "data" and "data_a" arrays
combined_data = jsonData.get("data", []) + jsonData.get("data_a", [])

# List to store shortened image URLs
shortened_urls = []

# Loop through the combined array
for item in combined_data:
    if "imageUrl" in item:
        image_url = item["imageUrl"]
        shortened_url = shorten_url(image_url)
        shortened_urls.append(shortened_url)

# Output the combined shortened image URLs list
print(json.dumps(shortened_urls, indent=2))

# Print the length of the combined shortened image URLs list
print("\nNumber of Combined Shortened Image URLs:", len(shortened_urls))

# Finding the size of the combined array
size_of_combined_data = len(combined_data)

# Printing the result
print("\nSize of Combined Data:", size_of_combined_data)


def print_missing_json_length():
    try:
        with open('missing.json', 'r') as file:
            missing_data = json.load(file)
        print("Length of Missing JSON:", len(missing_data))
    except FileNotFoundError:
        print("Missing JSON file not found.")


# Call the function to print the length of 'missing.json'
print_missing_json_length()
