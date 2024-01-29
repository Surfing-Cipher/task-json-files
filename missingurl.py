import json


def shorten_url1(long_url):
    return long_url.split("/")[-1].split("?")[0]


# Load JSON data from a file
with open('lp-data.json') as file:
    jsonData1 = json.load(file)

# Combine "data" and "data_a" arrays
combined_data1 = jsonData1.get("data", []) + jsonData1.get("data_a", [])

# List to store shortened image URLs
shortened_urls1 = []

# Loop through the combined array
for item in combined_data1:
    if "imageUrl" in item:
        image_url = item["imageUrl"]
        shortened_url = shorten_url1(image_url)
        shortened_urls1.append(shortened_url)

# Output the combined shortened image URLs list
print(json.dumps(shortened_urls1, indent=2))

# Print the length of the combined shortened image URLs list
print("\nNumber of Combined Shortened Image URLs:", len(shortened_urls1))

# Finding the size of the combined array
size_of_combined_data = len(combined_data1)

# Printing the result
print("\nSize of Combined Data:", size_of_combined_data)


# Given URL shortening function


def shorten_url2(long_url):
    return long_url.split("/")[-1].split("?")[0]

# Custom URL shortening function for the second code


def custom_shorten_url2(long_url):
    # Split the URL based on "/" and take the last part
    filename = long_url.split("/")[-1]

    # Remove the file extension (assuming it's always '.jpeg')
    filename_without_extension = filename.split(".")[0]

    # Use the same format as the first code for consistency
    shortened_url = shorten_url2(filename_without_extension)

    return shortened_url


# Load data from a JSON file
with open('db-loropiana.json', 'r') as file:
    data2 = json.load(file)

# Find the size of the original array
original_size2 = len(data2)

# List to store shortened image URLs
shortened_urls2 = []

# Extract unique image URLs
unique_image_urls2 = set()

for item in data2:
    if isinstance(item, dict):  # Check if the item is a dictionary
        image_url = item.get("imageUrl")
        if image_url:
            # Use the custom shortening function to get the shortened URL
            shortened_url = custom_shorten_url2(image_url)
            shortened_urls2.append(shortened_url)
            unique_image_urls2.add(shortened_url)

# Output the combined shortened image URLs list
print(json.dumps(shortened_urls2, indent=2))

# Print the length of the combined shortened image URLs list
print("\nNumber of Combined Shortened Image URLs:", len(shortened_urls2))

# Printing the result
print("Unique Shortened URLs Size:", len(unique_image_urls2))
print("Original Size:", original_size2)


# Convert both arrays to sets for efficient comparison
set_array1 = set(shortened_urls1)
set_array2 = set(shortened_urls2)

# Find the missing URLs by subtracting set_array2 from set_array1
missing_urls = set_array1 - set_array2

# Convert the missing_urls set back to a list
missing_urls_list = list(missing_urls)

# Output the missing URLs list
print("\nMissing URLs:")
print(json.dumps(missing_urls_list, indent=2))

# Print the length of the missing URLs list
print("\nNumber of Missing URLs:", len(missing_urls_list))
