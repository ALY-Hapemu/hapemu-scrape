import re
import json

DXOMARK_URL = "aaa"
INPUT_FILE = "dxomark.html"
OUTPUT_FILE = "dxomark.json"

# TODO: get content from website

with open(INPUT_FILE, 'r') as file:
    content = file.read()

match = re.search(r'var smartphonesAsJson = (.*);', content)

if match:
    json_str = match.group(1)
    data = json.loads(json_str)

    with open(OUTPUT_FILE, 'w') as file:
        json.dump(data, file, indent=4)