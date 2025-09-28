import os
import requests

# Ask user for an image URL
url = input("Enter the image URL: ")

# Make sure the folder exists
folder = "Fetched_Images"
os.makedirs(folder, exist_ok=True)

try:
    # Download the image
    response = requests.get(url)
    response.raise_for_status()

    # Get the filename from the URL (default to 'downloaded_image.jpg' if missing)
    filename = url.split("/")[-1]
    if not filename:
        filename = "downloaded_image.jpg"

    # Save the image
    filepath = os.path.join(folder, filename)
    with open(filepath, "wb") as f:
        f.write(response.content)

    print("Image saved as:", filepath)

except requests.exceptions.RequestException as e:
    print("Error downloading image:", e)
