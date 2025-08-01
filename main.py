import requests
from urllib.parse import urlparse

def get_http_headers(url):
    """
    Fetches HTTP headers from a given URL and returns them in a dictionary.
    
    Parameters:
    url (str): The URL from which to fetch headers.

    Returns:
    dict: A dictionary containing the HTTP headers.
    """
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()  # Raise an error for bad responses
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers from {url}: {e}")
        return {}

def parse_url(url):
    """
    Parses the URL to extract the scheme, netloc, and path.

    Parameters:
    url (str): The URL to parse.

    Returns:
    tuple: A tuple containing the scheme, netloc, and path.
    """
    parsed = urlparse(url)
    return parsed.scheme, parsed.netloc, parsed.path

def display_headers(headers):
    """
    Displays the HTTP headers in a user-friendly format.

    Parameters:
    headers (dict): A dictionary of HTTP headers.
    """
    print("\nHTTP Headers:")
    for key, value in headers.items():
        print(f"{key}: {value}")

def main():
    """
    Main function to run the OSINT tool.
    Prompts the user for a URL, fetches its HTTP headers, and displays them.
    """
    url = input("Enter a URL (including http:// or https://): ")
    scheme, netloc, path = parse_url(url)
    
    if not scheme or not netloc:
        print("Invalid URL. Please include the scheme (http or https).")
        return
    
    print(f"Fetching HTTP headers for {url}...")
    headers = get_http_headers(url)
    display_headers(headers)

if __name__ == "__main__":
    main()
```