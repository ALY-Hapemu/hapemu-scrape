import json
import os
import random
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
            # time.sleep(5)
            response = requests.get(url, headers=headers)
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
            'name': specs.get('modelname'),
            'releaseDate': specs.get('released-hl'),
            # 'body': specs.get('body-hl'),
            'os': specs.get('os-hl'),
            'storage': specs.get('storage-hl'),
            'displaySize': specs.get('displaysize-hl'),
            'displayResolution': specs.get('displayres-hl'),
            'cameraPixels': specs.get('camerapixels-hl'),
            'videoPixels': specs.get('videopixels-hl'),
            'ram': specs.get('ramsize-hl'),
            'chipset': specs.get('chipset-hl'),
            'battery': specs.get('batsize-hl'),
            'batteryType': specs.get('battype-hl'),
            # 'networkTechnology': specs.get('nettech'),
            # 'network2G': specs.get('net2g'),
            # 'network3G': specs.get('net3g'),
            # 'network4G': specs.get('net4g'),
            # 'network5G': specs.get('net5g'),
            # 'networkSpeed': specs.get('speed'),
            # 'dimensions': specs.get('dimensions'),
            # 'weight': specs.get('weight'),
            # 'build': specs.get('build'),
            # 'sim': specs.get('sim'),
            # 'bodyOther': specs.get('bodyother'),
            'displayType': specs.get('displaytype'),
            # 'displaySizeDetailed': specs.get('displaysize'),
            # 'displayResolutionDetailed': specs.get('displayresolution'),
            'displayProtection': specs.get('displayprotection'),
            # 'displayOtherFeatures': specs.get('displayother'),
            'cpu': specs.get('cpu'),
            'gpu': specs.get('gpu'),
            # 'memorySlot': specs.get('memoryslot'),
            'internalMemory': specs.get('internalmemory'),
            # 'memoryOther': specs.get('memoryother'),
            'mainCameraModules': specs.get('cam1modules'),
            'mainCameraFeatures': specs.get('cam1features'),
            'mainCameraVideo': specs.get('cam1video'),
            'selfieCameraModules': specs.get('cam2modules'),
            'selfieCameraFeatures': specs.get('cam2features'),
            'selfieCameraVideo': specs.get('cam2video'),
            'wlan': specs.get('wlan'),
            'bluetooth': specs.get('bluetooth'),
            'gps': specs.get('gps'),
            'nfc': specs.get('nfc'),
            'radio': specs.get('radio'),
            'usb': specs.get('usb'),
            'sensors': specs.get('sensors'),
            'otherFeatures': specs.get('featuresother'),
            'batteryDescription': specs.get('batdescription1'),
            'colors': specs.get('colors'),
            'models': specs.get('models'),
            'sarUS': specs.get('sar-us'),
            'sarEU': specs.get('sar-eu'),
            'price': specs.get('price'),
            'benchmarks': specs.get('tbench'),
            'batteryLife': specs.get('batlife2')
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

def write_to_json_file_in_urls_folder(data, filename):
    output_folder = "urls"
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

def get_targeted_brands():
    brand_urls = {
        # 'Samsung': 'https://www.gsmarena.com/samsung-phones-9.php',
        # 'Apple': 'https://www.gsmarena.com/apple-phones-48.php',
        # 'Google': 'https://www.gsmarena.com/google-phones-107.php',

        # 'Xiaomi': 'https://www.gsmarena.com/xiaomi-phones-80.php',
        # 'Oppo': 'https://www.gsmarena.com/oppo-phones-82.php',
        # 'Huawei': 'https://www.gsmarena.com/huawei-phones-58.php',
        # 'OnePlus': 'https://www.gsmarena.com/oneplus-phones-95.php',

        # 'Sony': 'https://www.gsmarena.com/sony-phones-7.php',
        # 'Realme': 'https://www.gsmarena.com/realme-phones-118.php',
        # 'Vivo': 'https://www.gsmarena.com/vivo-phones-98.php',
        # 'Motorola': 'https://www.gsmarena.com/motorola-phones-4.php',

        # 'Asus': 'https://www.gsmarena.com/asus-phones-46.php',
        # 'LG': 'https://www.gsmarena.com/lg-phones-20.php',
        # 'ZTE': 'https://www.gsmarena.com/zte-phones-62.php',
        # 'Honor': 'https://www.gsmarena.com/honor-phones-121.php',
        # 'Nokia': 'https://www.gsmarena.com/nokia-phones-1.php',
        # 'Lenovo': 'https://www.gsmarena.com/lenovo-phones-73.php',
        # 'Infinix': 'https://www.gsmarena.com/infinix-phones-119.php',
        # 'Tecno': 'https://www.gsmarena.com/tecno-phones-120.php',
        # 'Itel': 'https://www.gsmarena.com/itel-phones-131.php',
        # 'Alcatel': 'https://www.gsmarena.com/alcatel-phones-5.php',
        # 'Fairphone': 'https://www.gsmarena.com/fairphone-phones-127.php',
        # 'Nothing': 'https://www.gsmarena.com/nothing-phones-128.php',
        # 'TCL': 'https://www.gsmarena.com/tcl-phones-123.php',
        # 'Wiko': 'https://www.gsmarena.com/wiko-phones-96.php',

        # # CONFIRMED DOESN'T EXIST, fill data manually
        # 'Meitu': ''
        # 'POCO': '',
        # 'Nubia': '',
        # 'Crosscall': '',
    }

    for brand, brand_url in brand_urls.items():
        smartphone_urls = get_all_smartphone_urls(brand_url)
        write_to_json_file_in_urls_folder(smartphone_urls, brand.lower())

def read_json(filename):
    output_file = os.path.join("results", f'{filename}.json')
    try:
        with open(output_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def upsert_to_json(filename, new_data):
    output_file = os.path.join("results", f'{filename}.json')
    try:
        with open(output_file, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(new_data)
    with open(output_file, 'w') as file:
        json.dump(existing_data, file, indent=4)

def get_dxomark_score(dxomark_smartphone):
    if 'selfie' in dxomark_smartphone:
        return dxomark_smartphone['selfie']['score']
    elif 'mobile' in dxomark_smartphone:
        return dxomark_smartphone['mobile']['score']
    else:
        return None
    
def get_dxomark_subscores(dxomark_smartphone):
    subscores = {}
    if 'mobile' in dxomark_smartphone:
        subscores = dxomark_smartphone['mobile']['subscores']
        return subscores
    elif 'selfie' in dxomark_smartphone:
        subscores = dxomark_smartphone['selfie']['subscores']
        subscores['bokeh'] = 'NaN'
        subscores['preview'] = 'NaN'
        subscores['zoom'] = 'NaN'
    else:
        subscores['photo'] = 'NaN'
        subscores['video'] = 'NaN'
        subscores['bokeh'] = 'NaN'
        subscores['preview'] = 'NaN'
        subscores['zoom'] = 'NaN'
    
    return subscores

if __name__ == "__main__":
    if '--test' in sys.argv:
        test_get_all_smartphone_urls()
    elif '--clean' in sys.argv:
        # get_targeted_brands()

        smartphone_urls = {
            # Google
            # "Google Pixel 3": "google_pixel_3-9256.php",
            # 'Google Pixel 2': "google_pixel_2-8720.php",
            # 'Google Pixel 5': "google_pixel_5-10386.php",
            # 'Google Pixel 4': "google_pixel_4-9896.php",
            # 'Google Pixel 4a': "google_pixel_4a_5g-10385.php",
            # 'Google Pixel 6 Pro': "google_pixel_6_pro-10918.php",
            # 'Google Pixel 6': "google_pixel_6-11037.php",
            # 'Google Pixel 6a': "google_pixel_6a-11229.php",
            # 'Google Pixel 7 Pro': "google_pixel_7_pro-11908.php",
            # 'Google Pixel 7': "google_pixel_7-11903.php",
            # 'Google Pixel 7a': "google_pixel_7a-12170.php",
            # 'Google Pixel Fold': "google_pixel_fold-12265.php",
            # 'Google Pixel 8': "google_pixel_8-12546.php",
            # 'Google Pixel 8 Pro': "google_pixel_8_pro-12545.php",
            # 'Google Pixel 8a': "google_pixel_8a-12937.php"

            # Apple
            # "Apple iPhone XS Max": "apple_iphone_xs_max-9319.php",
            # "Apple iPhone X": "apple_iphone_x-8858.php",
            # "Apple iPhone 11 Pro Max": "apple_iphone_11_pro_max-9846.php",
            # "Apple iPhone 11": "apple_iphone_11-9848.php",
            # "Apple iPhone SE (2020)": "apple_iphone_se-7969.php",
            # "Apple iPhone 12": "apple_iphone_12-10509.php",
            # "Apple iPhone 12 Pro": "apple_iphone_12_pro-10508.php",
            # "Apple iPhone 12 Pro Max": "apple_iphone_12_pro_max-10237.php",
            # "Apple iPhone 12 mini": "apple_iphone_12_mini-10510.php",
            # "Apple iPhone 13 Pro": "apple_iphone_13_pro-11102.php",
            # "Apple iPhone 13 mini": "apple_iphone_13_mini-11104.php",
            # "Apple iPhone 13 Pro Max": "apple_iphone_13_pro_max-11089.php",
            # "Apple iPhone 13": "apple_iphone_13-11103.php",
            # "Apple iPhone SE (2022)": "apple_iphone_se_(2022)-11410.php",
            # "Apple iPhone 14": "apple_iphone_14-11861.php",
            # "Apple iPhone 14 Pro Max": "apple_iphone_14_pro_max-11773.php",
            # "Apple iPhone 14 Pro": "apple_iphone_14_pro-11860.php",
            # "Apple iPhone 14 Plus": "apple_iphone_14_plus-11862.php",
            # "Apple iPhone 15 Pro Max": "apple_iphone_15_pro_max-12548.php",
            # "Apple iPhone 15 Pro": "apple_iphone_15_pro-12557.php",
            # "Apple iPhone 15": "apple_iphone_15-12559.php",
            # "Apple iPhone 15 Plus": "apple_iphone_15_plus-12558.php"

            # Samsung
            # "Samsung Galaxy S8": "samsung_galaxy_s8-8161.php",
            # "Samsung Galaxy S10+": "samsung_galaxy_s10+-9535.php",
            # "Samsung Galaxy A71": "samsung_galaxy_a71_5g-10146.php",
            # "Samsung Galaxy Z Flip": "samsung_galaxy_z_flip-10054.php",
            # "Samsung Galaxy S20+": "samsung_galaxy_s20+-10080.php",
            # "Samsung Galaxy Note20 Ultra 5G (Exynos)": "samsung_galaxy_note20_ultra_5g-10261.php",
            # "Samsung Galaxy S10+ (Exynos)": "samsung_galaxy_s10+-9535.php",
            # "Samsung Galaxy S10 5G (Exynos)": "samsung_galaxy_s10_5g-9588.php",
            # "Samsung Galaxy Note 10+ (Exynos)": "samsung_galaxy_note10+-9732.php",
            # "Samsung Galaxy Note 10+ 5G (Exynos)": "samsung_galaxy_note10+_5g-9787.php",
            # "Samsung Galaxy S20 Ultra 5G (Exynos)": "samsung_galaxy_s20_ultra_5g-10040.php",
            # "Samsung Galaxy Note20 Ultra 5G (Snapdragon)": "samsung_galaxy_note20_ultra_5g-10261.php",
            # "Samsung Galaxy Note20 (Exynos)": "samsung_galaxy_note20-10338.php",
            # "Samsung Galaxy S21 Ultra 5G (Exynos)": "samsung_galaxy_s21_ultra_5g-10596.php",
            # "Samsung Galaxy Z Fold2 5G": "samsung_galaxy_z_fold2_5g-10342.php",
            # "Samsung Galaxy S21 Ultra 5G (Snapdragon)": "samsung_galaxy_s21_ultra_5g-10596.php",
            # "Samsung Galaxy S21 5G (Exynos)": "samsung_galaxy_s21_5g-10626.php",
            # "Samsung Galaxy S21+ 5G (Exynos)": "samsung_galaxy_s21+_5g-10625.php",
            # "Samsung Galaxy S21 5G (Snapdragon)": "samsung_galaxy_s21_5g-10626.php",
            # "Samsung Galaxy M51": "samsung_galaxy_m51-10148.php",
            # "Samsung Galaxy A52 5G": "samsung_galaxy_a52_5g-10631.php",
            # "Samsung Galaxy S21+ 5G (Snapdragon)": "samsung_galaxy_s21+_5g-10625.php",
            # "Samsung Galaxy A72": "samsung_galaxy_a72-10469.php",
            # "Samsung Galaxy A22 5G": "samsung_galaxy_a22_5g-10873.php",
            # "Samsung Galaxy Z Fold3 5G": "samsung_galaxy_z_fold3_5g-10906.php",
            # "Samsung Galaxy A52s 5G": "samsung_galaxy_a52s_5g-11039.php",
            # "Samsung Galaxy S21 FE 5G (Snapdragon)": "samsung_galaxy_s21_fe_5g-10954.php",
            # "Samsung Galaxy S22 (Exynos)": "samsung_galaxy_s22_5g-11253.php",
            # "Samsung Galaxy S22+ (Exynos)": "samsung_galaxy_s22+_5g-11252.php",
            # "Samsung Galaxy S22 Ultra (Exynos)": "samsung_galaxy_s22_ultra_5g-11251.php",
            # "Samsung Galaxy S22 (Snapdragon)": "samsung_galaxy_s22_5g-11253.php",
            # "Samsung Galaxy S22 Ultra (Snapdragon)": "samsung_galaxy_s22+_5g-11252.php",
            # "Samsung Galaxy A53 5G": "samsung_galaxy_a53_5g-11268.php",
            # "Samsung Galaxy A33 5G": "samsung_galaxy_a33_5g-11429.php",
            # "Samsung Galaxy Z Flip3 5G": "samsung_galaxy_z_flip3_5g-11044.php",
            # "Samsung Galaxy A13 5G": "samsung_galaxy_a13_5g-11149.php",
            # "Samsung Galaxy Z Fold4": "samsung_galaxy_z_fold4-11737.php",
            # "Samsung Galaxy Z Flip4": "samsung_galaxy_z_flip4-11538.php",
            # "Samsung Galaxy A23 5G": "samsung_galaxy_a23_5g-11736.php",
            # "Samsung Galaxy S23+": "samsung_galaxy_s23+-12083.php",
            # "Samsung Galaxy S23 Ultra": "samsung_galaxy_s23_ultra-12024.php",
            # "Samsung Galaxy A54 5G": "samsung_galaxy_a54-12070.php",
            # "Samsung Galaxy S23": "samsung_galaxy_s23-12082.php",
            # "Samsung Galaxy A34 5G": "samsung_galaxy_a34-12074.php",
            # "Samsung Galaxy A14 5G": "samsung_galaxy_a14-12151.php",
            # "Samsung Galaxy Z Flip5": "samsung_galaxy_z_flip5-12252.php",
            # "Samsung Galaxy Z Fold5": "samsung_galaxy_z_fold5-12418.php",
            # "Samsung Galaxy S23 FE": "samsung_galaxy_s23_fe-12520.php",
            # "Samsung Galaxy A05s": "samsung_galaxy_a05s-12584.php",
            # "Samsung Galaxy A25 5G": "samsung_galaxy_a25-12555.php",
            # "Samsung Galaxy S24 Ultra": "samsung_galaxy_s24_ultra-12771.php",
            # "Samsung Galaxy S24 (Exynos)": "samsung_galaxy_s24-12773.php",
            # "Samsung Galaxy S24+ (Exynos)": "samsung_galaxy_s24+-12772.php",
            # "Samsung Galaxy A15 5G": "samsung_galaxy_a15_5g-12638.php",
            # "Samsung Galaxy A15 LTE": "samsung_galaxy_a15-12637.php",
            # "Samsung Galaxy A55 5G": "samsung_galaxy_a55-12824.php",
            # "Samsung Galaxy A35 5G": "samsung_galaxy_a35-12705.php"

            # Xiaomi
            # "Xiaomi Mi MIX 3": "xiaomi_mi_mix_3-9378.php",
            # "Xiaomi Mi CC9 Pro Premium Edition": "xiaomi_mi_cc9_pro-9935.php",
            # "Xiaomi Mi 10 Pro": "xiaomi_mi_10_pro_5g-10055.php",
            # "Xiaomi Mi 10 Ultra": "xiaomi_mi_10_ultra-10361.php",
            # "Xiaomi Mi 10T Pro 5G": "xiaomi_mi_10t_pro_5g-10437.php",
            # "Xiaomi Mi 10 S": "xiaomi_mi_10s-10780.php",
            # "Xiaomi Mi 11": "xiaomi_mi_11-10656.php",
            # "Xiaomi Mi 11 Ultra": "xiaomi_mi_11_ultra-10737.php",
            # "Xiaomi Redmi 9": "xiaomi_redmi_9-10233.php",
            # "Xiaomi Redmi Note 10 Pro": "xiaomi_redmi_note_10_pro-10662.php",
            # "Xiaomi Redmi K40 Pro+": "xiaomi_redmi_k40_pro+-10752.php",
            # "Xiaomi Mi 11 Lite 5G": "xiaomi_mi_11_lite_5g-10815.php",
            # "Xiaomi Redmi Note 10": "xiaomi_redmi_note_10-10247.php",
            # "Xiaomi Redmi Note 10 5G": "xiaomi_redmi_note_10_5g-10768.php",
            # "Xiaomi Redmi Note 10S": "xiaomi_redmi_note_10s-10769.php",
            # "Xiaomi Mi 11i": "xiaomi_mi_11i-10777.php",
            # "Xiaomi Redmi K40 Gaming": "xiaomi_redmi_k40_gaming-10880.php",
            # "Xiaomi Mi 11 Pro": "xiaomi_mi_11_pro-10816.php",
            # "Xiaomi 11T Pro": "xiaomi_11t_pro-11100.php",
            # "Xiaomi 11T": "xiaomi_11t-11099.php",
            # "Xiaomi Redmi Note 11": "xiaomi_redmi_note_11-11336.php",
            # "Xiaomi 12 Pro": "xiaomi_12_pro-11287.php",
            # "Xiaomi 12": "xiaomi_12-11285.php",
            # "Xiaomi Redmi 10 2022": "xiaomi_redmi_10_2022-11357.php",
            # "Xiaomi Redmi Note 11 Pro 5G": "xiaomi_redmi_note_11_pro_5g-11333.php",
            # "Xiaomi Redmi Note 11S 5G": "xiaomi_redmi_note_11s_5g-11419.php",
            # "Xiaomi Redmi K50 Gaming": "xiaomi_redmi_k50_gaming-11362.php",
            # "Xiaomi 12S Ultra": "xiaomi_12s_ultra-11614.php",
            # "Xiaomi 12T": "xiaomi_12t-11888.php",
            # "Xiaomi 12T Pro": "xiaomi_12t_pro-11887.php",
            # "Xiaomi 12 Lite 5G": "xiaomi_12_lite-11472.php",
            # "Xiaomi 13 Pro": "xiaomi_13_pro-11962.php",
            # "Xiaomi 13": "xiaomi_13-12013.php",
            # "Xiaomi Mix Fold 2": "xiaomi_mix_fold_2-11758.php",
            # "Xiaomi Redmi Note 12 5G": "xiaomi_redmi_note_12-12063.php",
            # "Xiaomi Redmi Note 12 Pro+ 5G": "xiaomi_redmi_note_12_pro+-11954.php",
            # "Xiaomi Redmi Note 12 Pro 5G": "xiaomi_redmi_note_12_pro-11955.php",
            # "Xiaomi Redmi 12C": "xiaomi_redmi_12c-12051.php",
            # "Xiaomi Redmi Note 12": "xiaomi_redmi_note_12-12063.php",
            # "Xiaomi 13 Ultra": "xiaomi_13_ultra-12236.php",
            # "Xiaomi Redmi 12 5G": "xiaomi_redmi_12_5g-12446.php",
            # "Xiaomi 13T": "xiaomi_13t-12389.php",
            # "Xiaomi 13T Pro": "xiaomi_13t_pro-12388.php",
            # "Xiaomi Mix Fold 3": "xiaomi_mix_fold_3-12468.php",
            # "Xiaomi Redmi Note 13 Pro Plus 5G": "xiaomi_redmi_note_13_pro+-12572.php",
            # "Xiaomi Redmi 13C": "xiaomi_redmi_13c-12689.php",
            # "Xiaomi 14": "xiaomi_14-12626.php",
            # "Xiaomi Redmi Note 13 Pro 5G": "xiaomi_redmi_note_13_pro-12581.php",
            # "Xiaomi Redmi Note 13": "xiaomi_redmi_note_13_4g-12750.php",
            # "Xiaomi Redmi Note 13 5G": "xiaomi_redmi_note_13-12776.php",
            # "Xiaomi 14 Ultra": "xiaomi_14_ultra-12827.php",
            # "Xiaomi Redmi 13C 5G": "xiaomi_redmi_13c_5g-12726.php",
        }
        dxomark_smartphones = read_json('dxomark')
        for smartphone, smartphone_url in smartphone_urls.items():
            print(f'Fetching {smartphone}...')
            html = fetch_html(f"{GSMARENA_URL}/{smartphone_url}")
            print(f'Received {smartphone}.')

            gsmarena_smartphone = parse_smartphone_page(html)
            print('Smartphone: ', gsmarena_smartphone)

            dxomark_smartphone = next((item for item in dxomark_smartphones if item.get('name') == smartphone), None)
            print(f'Dxomark counterpart for {smartphone}: {dxomark_smartphone}')
            if dxomark_smartphone:
                final_smartphone = {
                    'name': dxomark_smartphone.get('name'),
                    'brand': dxomark_smartphone.get('brand'),
                    'dxomarkScore': get_dxomark_score(dxomark_smartphone),
                    'segmentPrice': dxomark_smartphone.get('segment_price'),
                    'ram': gsmarena_smartphone.get('ram'),
                    'launchDate': dxomark_smartphone.get('launch_date'),
                    'image': dxomark_smartphone.get('image'),
                    'battery': gsmarena_smartphone.get('battery'),
                    'cameraPixel': gsmarena_smartphone.get('cameraPixels'),
                    'videoPixel': gsmarena_smartphone.get('videoPixels'),
                    'displaySize': gsmarena_smartphone.get('displaySize'),
                    'displayRes': gsmarena_smartphone.get('displayResolution'),
                    'storage': gsmarena_smartphone.get('storage'),
                    'price': dxomark_smartphone.get('launch_price'),
                    'photo': get_dxomark_subscores(dxomark_smartphone)['photo'],
                    'bokeh': get_dxomark_subscores(dxomark_smartphone)['bokeh'],
                    'preview': get_dxomark_subscores(dxomark_smartphone)['preview'],
                    'zoom': get_dxomark_subscores(dxomark_smartphone)['zoom'],
                    'video': get_dxomark_subscores(dxomark_smartphone)['video'],
                }
                upsert_to_json('gsmarena', gsmarena_smartphone)
                upsert_to_json(f'final_{final_smartphone.get('brand')}', final_smartphone)
            else:
                break

    else:
        main()
























""" REGION: FETCHING WITH ROTATING PROXIES """
# proxies_list = open('proxies.txt', 'r').read().strip().split('\n')
# VALID_STATUS_CODES = [200]
# unchecked_proxies = set(proxies_list[0:10])
# working_proxies = set()
# not_working_proxies = set()

# def reset_proxy(proxy): 
#     unchecked_proxies.add(proxy) 
#     working_proxies.discard(proxy) 
#     not_working_proxies.discard(proxy) 
 
# def set_working(proxy): 
#     unchecked_proxies.discard(proxy) 
#     working_proxies.add(proxy) 
#     not_working_proxies.discard(proxy) 
 
# def set_not_working(proxy): 
#     unchecked_proxies.discard(proxy) 
#     working_proxies.discard(proxy) 
#     not_working_proxies.add(proxy)

# session = requests.Session()

# def check_proxies():
#     proxy = proxies_list.pop()
#     for proxy in list(unchecked_proxies):
#         try:
#             response = requests.get('http://ident.me/', proxies={'http': f'http://{proxy}'}, timeout=30)
#             if response.status_code in VALID_STATUS_CODES:
#                 set_working(proxy)
#             else:
#                 set_not_working(proxy)
#         except Exception as e:
#             print(e)

#     print('Unchecked proxies list:', unchecked_proxies)
#     print('Working proxies list: ', working_proxies)
#     print('Not working proxies list: ', not_working_proxies)

# def get_random_proxy():
#     available_proxies = tuple(unchecked_proxies.union(working_proxies))
#     if not available_proxies:
#         raise Exception('No available proxies.')
#     return random.choice(available_proxies)

# def fetch_html_rotating(url, proxy = None):
#     if not proxy:
#         proxy = get_random_proxy()

#     try:
#         response = 

#     return
""" ENDREGION """
