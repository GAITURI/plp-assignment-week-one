import os
import requests
from urllib.parse import urlparse

def download_image():
    """
    Prompts the user for an image URL, downloads the image, and saves it
    to a 'Fetched_Images' directory.
    """
    # Prompt the user for a URL
    url = input("Please enter the URL of the image you want to download: ").strip()

    if not url:
        print("URL cannot be empty. Please try again.")
        return

    # Create the directory if it doesn't exist
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    # Extract filename from URL or create a generic one
    try:
        # urlparse breaks the URL into components
        path = urlparse(url).path
        filename = os.path.basename(path)
        # If the filename is empty, create a generic one
        if not filename or '.' not in filename:
            filename = "downloaded_image.jpg"
    except Exception as e:
        print(f"Error parsing URL: {e}")
        filename = "downloaded_image.jpg"
        
    filepath = os.path.join("Fetched_Images", filename)

    print(f"Attempting to download from: {url}")

    # Use a try-except block to handle potential errors
    try:
        # Send a GET request to the URL with a timeout
        response = requests.get(url, timeout=10)
        # Raise an exception for bad HTTP status codes (4xx or 5xx)
        response.raise_for_status()

        # Save the image content to a file in binary mode
        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"Image successfully downloaded and saved as {filepath}")

    except requests.exceptions.RequestException as e:
        # Catch any request-related errors (e.g., connection errors, timeouts, HTTP errors)
        print(f"An error occurred while downloading the image: {e}")
    except IOError as e:
        # Catch file-related errors
        print(f"Error saving the image file: {e}")

if __name__ == "__main__":
    download_image()import os
import requests
from urllib.parse import urlparse

def download_image():
    """
    Prompts the user for an image URL, downloads the image, and saves it
    to a 'Fetched_Images' directory.
    """
    # Prompt the user for a URL
    url = input("Please enter the URL of the image you want to download: ").strip()

    if not url:
        print("URL cannot be empty. Please try again.")
        return

    # Create the directory if it doesn't exist
    try:
        os.makedirs("Fetched_Images", exist_ok=True)
    except OSError as e:
        print(f"Error creating directory: {e}")
        return

    # Extract filename from URL or create a generic one
    try:
        # urlparse breaks the URL into components
        path = urlparse(url).path
        filename = os.path.basename(path)
        # If the filename is empty, create a generic one
        if not filename or '.' not in filename:
            filename = "downloaded_image.jpg"
    except Exception as e:
        print(f"Error parsing URL: {e}")
        filename = "downloaded_image.jpg"
        
    filepath = os.path.join("Fetched_Images", filename)

    print(f"Attempting to download from: {url}")

    # Use a try-except block to handle potential errors
    try:
        # Send a GET request to the URL with a timeout
        response = requests.get(url, timeout=10)
        # Raise an exception for bad HTTP status codes (4xx or 5xx)
        response.raise_for_status()

        # Save the image content to a file in binary mode
        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"Image successfully downloaded and saved as {filepath}")

    except requests.exceptions.RequestException as e:
        # Catch any request-related errors (e.g., connection errors, timeouts, HTTP errors)
        print(f"An error occurred while downloading the image: {e}")
    except IOError as e:
        # Catch file-related errors
        print(f"Error saving the image file: {e}")

if __name__ == "__main__":
    download_image()