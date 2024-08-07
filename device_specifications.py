import requests
from bs4 import BeautifulSoup

def fetch_device_specifications(url):
    try:
        response = requests.get(url)
        # print(response.text)

        soup = BeautifulSoup(response.content, 'html.parser')
        specifications = soup.find(id="model-brief-specifications")
        if specifications:
            print(specifications.text.strip())
        else:
            print("Specifications not found.")
    except requests.RequestException as e:
        return f"Error fetching specifications: {str(e)}"

# Example usage:
# url = "https://www.devicespecifications.com/en/model/d7fb5a7a"
# print(fetch_device_specifications(url))
fetch_device_specifications("https://www.devicespecifications.com/en/model/d7fb5a7a")