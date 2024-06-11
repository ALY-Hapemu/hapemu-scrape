import json
import os
import re
import requests
from bs4 import BeautifulSoup

DXOMARK_URL = 'https://www.dxomark.com/smartphones/'
FILENAME = "dxomark.json"

if __name__ == "__main__":
    html = requests.get(DXOMARK_URL)
    soup = BeautifulSoup(html.content, "html.parser")

    match = re.search(r'var smartphonesAsJson = (.*);', soup.prettify())

    if match:
        json_str = match.group(1)
        data = json.loads(json_str)

        output_folder = "results"
        output_file = os.path.join(output_folder, FILENAME)

        os.makedirs(output_folder, exist_ok=True)

        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
            print('Success.')
