import requests
import json
import os
from bs4 import BeautifulSoup

def fetch_html(url):
    return requests.get(url)

def parse_data(html):
    soup = BeautifulSoup(html.content, "html.parser")

    results = soup.find_all("div", "nrank-b")
    smartphones = []
    for result in results:
        # Extract smartphone name
        smartphone_li = result.find("li", "bfirst")
        for span in smartphone_li.find_all('span'):
            span.decompose()
        smartphone = smartphone_li.text.strip()

        # Extract score
        scores = [li.text for li in result.find_all('li')][1:]
        
        # Map scores to respective smartphone
        smartphones.append({
            'name': smartphone,
            'cpu': scores[0],
            'gpu': scores[1],
            'mem': scores[2],
            'ux': scores[3],
            'total': scores[4]
        })
    
    return smartphones

def write_to_json_file(data, filename):
    output_folder = "results"
    output_file = os.path.join(output_folder, filename)

    os.makedirs(output_folder, exist_ok=True)

    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

""" Main """
def main():
    urls = [
        "https://www.antutu.com/en/ranking/rank1.htm", # Android ranking url
        "https://www.antutu.com/en/ranking/ios1.htm" # iOS ranking url
    ]
    for url in urls:
        html = fetch_html(url)
        parsed_data = parse_data(html)

        filename = f"antutu_{url.split('/')[-1].replace('.htm', '')}.json"
        write_to_json_file(parsed_data, filename)

if __name__ == "__main__":
    main()
