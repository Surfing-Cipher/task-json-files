import json


def shorten_url1(long_url):
    return long_url.split("/")[-1].split("?")[0]


def shorten_url2(long_url):
    return long_url.split("/")[-1].split("?")[0]


def custom_shorten_url2(long_url):
    filename = long_url.split("/")[-1]
    filename_without_extension = filename.split(".")[0]
    shortened_url = shorten_url2(filename_without_extension)
    return shortened_url


# Load JSON data from the 'lp' file
with open('lp-data.json') as file:
    jsonData1 = json.load(file)

# Combine "data" and "data_a" arrays
combined_data1 = jsonData1.get("data", []) + jsonData1.get("data_a", [])

# List to store shortened image URLs
shortened_urls1 = []

# Dictionary to store items corresponding to shortened URLs
items_by_url1 = {}

# Loop through the combined array
for item in combined_data1:
    if "imageUrl" in item:
        image_url = item["imageUrl"]
        shortened_url = shorten_url1(image_url)
        shortened_urls1.append(shortened_url)
        items_by_url1[shortened_url] = item

# Load data from the 'db' file
with open('db-loropiana.json', 'r') as file:
    data2 = json.load(file)

# List to store shortened image URLs
shortened_urls2 = []

# Dictionary to store items corresponding to shortened URLs
items_by_url2 = {}

# Extract unique image URLs
unique_image_urls2 = set()

for item in data2:
    if isinstance(item, dict):
        image_url = item.get("imageUrl")
        if image_url:
            shortened_url = custom_shorten_url2(image_url)
            shortened_urls2.append(shortened_url)
            items_by_url2[shortened_url] = item
            unique_image_urls2.add(shortened_url)

# Convert both arrays to sets for efficient comparison
set_array1 = set(shortened_urls1)
set_array2 = set(shortened_urls2)

# Find the missing URLs by subtracting set_array2 from set_array1
missing_urls = set_array1 - set_array2

# Convert the missing_urls set back to a list
missing_urls_list = list(missing_urls)

# Load existing 'missing.json' file if it exists
try:
    with open('missing.json', 'r') as existing_file:
        existing_data = json.load(existing_file)
except (FileNotFoundError, json.JSONDecodeError):
    existing_data = []

# Append missing items corresponding to the missing URLs
missing_items_list = [items_by_url1[url]
                      for url in missing_urls_list if url in items_by_url1]

# Save the updated missing items to 'missing.json'
with open('missing.json', 'w') as file:
    json.dump(missing_items_list, file, indent=2)

# Function to print the length of 'missing.json'


def print_missing_json_length():
    try:
        with open('missing.json', 'r') as file:
            missing_data = json.load(file)
        print("Length of Missing JSON:", len(missing_data))
    except (FileNotFoundError, json.JSONDecodeError):
        print("Missing JSON file not found or contains invalid JSON data.")


# Call the function to print the length of 'missing.json'
print_missing_json_length()
