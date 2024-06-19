import json
import os
import requests
import sys
import time
from bs4 import BeautifulSoup

"""
GSM Arena
---------
Website structure:
1. All brands list -> https://www.gsmarena.com/makers.php3
2. Brand-specific page (e.g. Samsung) -> https://www.gsmarena.com/samsung-phones-9.php
3. Smartphone-specific page (e.g. Samsung Galaxy S24 Ultra) -> https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php
"""

GSMARENA_URL = 'https://www.gsmarena.com/'
MAX_NUMBER_OF_PAGES_TO_FETCH = 5
GSMARENA_RETRYAFTER_IN_SECONDS = 36 # From GSMArena's response headers' "Retry-After" field.
FILENAME = 'gsmarena_smartphones.json'

# TODOs: 
# - Implement Proxy Rotator in case scraping entire site goes too long with current mechanism. Refer: https://www.zenrows.com/blog/web-scraping-rate-limit, https://www.zenrows.com/blog/stealth-web-scraping-in-python-avoid-blocking-like-a-ninja, https://www.zenrows.com/blog/how-to-rotate-proxies-in-python
#   - An alternative (tedious, but doable), split the scraping process to different computers scraping for different pre-defined brands list.
def fetch_html(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            response = requests.get(url, headers=headers)
            print(response)
            response.raise_for_status() # Raises HTTPError for bad responses
            return response
        except requests.RequestException:
            # Decided to apply a timeout as long as the value in Retry-After response header, in case of the HTML
            # is empty/not received, which is in most cases due to the HTTP 429 Error (Too Many Requests)
            # Refer: https://stackoverflow.com/a/23367215
            print(f'Retrying after {GSMARENA_RETRYAFTER_IN_SECONDS} seconds...')
            time.sleep(GSMARENA_RETRYAFTER_IN_SECONDS) # Wait before retrying
            print(f'Retrying...')
            attempts += 1

    if attempts >= max_attempts:
        print(f'Failed to fetch {url} after {max_attempts} attempts')

    return None

def parse_smartphone_page(html):
    soup = BeautifulSoup(html.content, 'html.parser')

    # Find all elements with a 'data-spec' attribute
    spec_elements = soup.find_all(attrs={'data-spec': True})

    # Extract and print the text of each element
    specs = {}
    for element in spec_elements:
        specs[element['data-spec']] = element.get_text(strip=True)

    smartphone = {}
    if specs:
        smartphone = {
            'name': specs['modelname'],
            'releaseDate': specs['released-hl'],
            'body': specs['body-hl'],
            'os': specs['os-hl'],
            'storage': specs['storage-hl'],
            'displaySize': specs['displaysize-hl'],
            'displayResolution': specs['displayres-hl'],
            'cameraPixels': specs['camerapixels-hl'],
            'videoPixels': specs['videopixels-hl'],
            'ram': specs['ramsize-hl'],
            'chipset': specs['chipset-hl'],
            'battery': specs['batsize-hl'],
            'batteryType': specs['battype-hl'],
            'networkTechnology': specs['nettech'],
            'network2G': specs['net2g'],
            'network3G': specs['net3g'],
            'network4G': specs['net4g'],
            'network5G': specs['net5g'],
            'networkSpeed': specs['speed'],
            'dimensions': specs['dimensions'],
            'weight': specs['weight'],
            'build': specs['build'],
            'sim': specs['sim'],
            'bodyOther': specs['bodyother'],
            'displayType': specs['displaytype'],
            'displaySizeDetailed': specs['displaysize'],
            'displayResolutionDetailed': specs['displayresolution'],
            'displayProtection': specs['displayprotection'],
            'displayOtherFeatures': specs['displayother'],
            'cpu': specs['cpu'],
            'gpu': specs['gpu'],
            'memorySlot': specs['memoryslot'],
            'internalMemory': specs['internalmemory'],
            'memoryOther': specs['memoryother'],
            'mainCameraModules': specs['cam1modules'],
            'mainCameraFeatures': specs['cam1features'],
            'mainCameraVideo': specs['cam1video'],
            'selfieCameraModules': specs['cam2modules'],
            'selfieCameraFeatures': specs['cam2features'],
            'selfieCameraVideo': specs['cam2video'],
            'wlan': specs['wlan'],
            'bluetooth': specs['bluetooth'],
            'gps': specs['gps'],
            'nfc': specs['nfc'],
            'radio': specs['radio'],
            'usb': specs['usb'],
            'sensors': specs['sensors'],
            'otherFeatures': specs['featuresother'],
            'batteryDescription': specs['batdescription1'],
            'colors': specs['colors'],
            'models': specs['models'],
            'sarUS': specs['sar-us'],
            'sarEU': specs['sar-eu'],
            'price': specs['price'],
            'benchmarks': specs['tbench'],
            'batteryLife': specs['batlife2']
        }
    print(json.dumps(smartphone, indent=4) + '\n\n\n')
    
    return smartphone

def get_all_brand_urls():
    print('Fetching all brand urls...')

    html = fetch_html(f'{GSMARENA_URL}/makers.php3')
    soup = BeautifulSoup(html.content, 'html.parser')

    # Get elements in brands list
    brands_list = soup.find('div', class_='st-text')

    # Extract brand urls
    brand_urls = [a['href'] for a in brands_list.find_all('a')]

    print('Done fetching all brand urls.\n')

    return brand_urls

def get_smartphone_urls_in_current_page(url):
    smartphone_urls = []
    next_page_url = ''

    if url:
        html = fetch_html(url)
        soup = BeautifulSoup(html.content, 'html.parser')
    
        # Get elements in smartphones list
        smartphones_list = soup.find('div', class_='makers')

        # Extract smartphone urls
        smartphone_urls = [a['href'] for a in smartphones_list.find_all('a')]

        # Extract next page url
        pages_list = soup.find('div', class_='nav-pages')
        if pages_list:
            strong_tag = pages_list.find('strong')
            next_page_url = f"{GSMARENA_URL}/{strong_tag.find_next('a')['href']}"

    return smartphone_urls, next_page_url

def get_number_of_pages(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    # Get the number of pages
    number_of_pages = 1
    pages_list = soup.find('div', class_='nav-pages')
    if pages_list:
        # Count number of elements in pages_list
        number_of_pages = pages_list.find_all()

        # Deduct 2 (number of arrow sign elements) from the total number of elements to get the actual number of pages
        number_of_pages = len(number_of_pages) - 2

        max_number_of_pages_shown_in_pagination_element = 4
        if number_of_pages == max_number_of_pages_shown_in_pagination_element:
            # Find the number on the last element. If the total number of pages is more than max_number_of_pages_to_fetch (5), then just set to 5.
            number_of_pages = min(int(pages_list.find_all()[-2].text.strip()), MAX_NUMBER_OF_PAGES_TO_FETCH)

    return number_of_pages

def get_all_smartphone_urls(brand_url):
    # Extract smartphone urls
    number_of_pages = get_number_of_pages(brand_url)
    smartphone_urls = []
    url_to_fetch = brand_url
    print(f'Number of pages: {number_of_pages}')
    for i in range(number_of_pages):
        smartphone_urls_in_current_page, next_page_url = get_smartphone_urls_in_current_page(url_to_fetch)

        smartphone_urls.extend(smartphone_urls_in_current_page)
        url_to_fetch = next_page_url

    print(smartphone_urls)
    print("\n\n\n")

    return smartphone_urls

def write_to_json_file(data, filename):
    output_folder = "results"
    output_file = os.path.join(output_folder, f'{filename}.json')

    os.makedirs(output_folder, exist_ok=True)

    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

""" Main """
def main():
    smartphones = []
    brand_urls = get_all_brand_urls()
    for brand_url in brand_urls:
        smartphone_urls = get_all_smartphone_urls(f'{GSMARENA_URL}/{brand_url}')

        for smartphone_url in smartphone_urls:
            html = fetch_html(f'{GSMARENA_URL}/{smartphone_url}')
            smartphone = parse_smartphone_page(html)
            smartphones.append(smartphone)

    write_to_json_file(smartphones, FILENAME)

""" Testing Methods """
def test_get_all_smartphone_urls():
    get_all_smartphone_urls('https://www.gsmarena.com/nvidia-phones-97.php') # 1 page
    get_all_smartphone_urls('https://www.gsmarena.com/acer-phones-59.php') # 2 pages
    get_all_smartphone_urls('https://www.gsmarena.com/realme-phones-118.php') # 4 pages
    get_all_smartphone_urls('https://www.gsmarena.com/samsung-phones-9.php') # many pages

def test_parse_smartphone_page():
    test_html = fetch_html(f'{GSMARENA_URL}/samsung_galaxy_s24_ultra-12771.php')
    if test_html:
        print('received')
        print(test_html.status_code)
    else:
        print('noo :(')
        print(test_html.status_code)

    parse_smartphone_page(test_html)

if __name__ == "__main__":
    if '--test' in sys.argv:
        test_get_all_smartphone_urls()
        test_parse_smartphone_page()
    else:
        main()