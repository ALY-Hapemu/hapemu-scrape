import json
import os
import re
import requests
from bs4 import BeautifulSoup

DXOMARK_URL = 'https://www.dxomark.com/smartphones/'

def output_to_json(data, output_folder, filename):
    output_file = os.path.join(output_folder, filename)
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)
        print('Success.')

if __name__ == "__main__":
    html = requests.get(DXOMARK_URL)
    soup = BeautifulSoup(html.content, "html.parser")

    match = re.search(r'var smartphonesAsJson = (.*);', soup.prettify())

    if match:
        json_str = match.group(1)

        data = json.loads(json_str)
        # output_to_json(data, "results", "dxomark.json")
        
        names_list = [item['name'] for item in data]
        output_to_json(names_list, "results", "smartphone_namesss.json")
