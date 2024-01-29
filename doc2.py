import json

# Given URL shortening function


def shorten_url(long_url):
    return long_url.split("/")[-1].split("?")[0]

# Custom URL shortening function for the second code


def custom_shorten_url(long_url):
    # Split the URL based on "/" and take the last part
    filename = long_url.split("/")[-1]

    # Remove the file extension (assuming it's always '.jpeg')
    filename_without_extension = filename.split(".")[0]

    # Use the same format as the first code for consistency
    shortened_url = shorten_url(filename_without_extension)

    return shortened_url


# Load data from a JSON file
with open('db-loropiana.json', 'r') as file:
    data = json.load(file)

# Find the size of the original array
original_size = len(data)

# List to store shortened image URLs
shortened_urls = []

# Extract unique image URLs
unique_image_urls = set()

for item in data:
    if isinstance(item, dict):  # Check if the item is a dictionary
        image_url = item.get("imageUrl")
        if image_url:
            # Use the custom shortening function to get the shortened URL
            shortened_url = custom_shorten_url(image_url)
            shortened_urls.append(shortened_url)
            unique_image_urls.add(shortened_url)

# Output the combined shortened image URLs list
print(json.dumps(shortened_urls, indent=2))

# Print the length of the combined shortened image URLs list
print("\nNumber of Combined Shortened Image URLs:", len(shortened_urls))

# Printing the result
print("Unique Shortened URLs Size:", len(unique_image_urls))
print("Original Size:", original_size)
