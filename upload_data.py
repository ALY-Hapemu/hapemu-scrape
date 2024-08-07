import json
import os
from supabase import create_client, Client

def read_json_file(filename):
    file_path = os.path.join("results", f'{filename}.json')
    with open(file_path, 'r') as file:
        return json.load(file)

def upload_data_to_supabase(client: Client, table_name, data):
    response = client.table(table_name).upsert(data).execute()
    assert len(response.data) > 0
    print("Data uploaded successfully")

def insert_to_db(supabase, data, table_name):
    for i in data:
        print(i)
        upload_data_to_supabase(supabase, table_name, i)

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

def testink():
    # 1. Read final_*.json
    # 2. Read gsmarena.json
    # 3. Iterate over smartphones list from final_*.json and get the smartphone from gsmarena
    # 4. Insert chipset from gsmarena counterpart
    # 5. Delete rows from smartphone table
    # 6. Refill db with updated final_*.json
    filenames = [
        'final',
        'final_Apple',
        'final_Samsung',
        'final_Xiaomi',
    ]
    current_smartphones_in_db = []
    for filename in filenames:
        current_smartphones_in_db.extend(read_json_file(filename))

    gsmarena_smartphones = read_json_file("gsmarena")
    phones_with_no_match_in_gsmarena = []
    for current_smartphone_in_db in current_smartphones_in_db:
        gsmarena_smartphone = next((item for item in gsmarena_smartphones if item.get('name') == current_smartphone_in_db['name']), None)
        print(f'Gsmarena counterpart for {current_smartphone_in_db['name']}: {gsmarena_smartphone}')
        if gsmarena_smartphone:
            current_smartphone_in_db['processor'] = gsmarena_smartphone.get('chipset')
            # upsert_to_json('updated_all', current_smartphone_in_db)
        else:
            closest_counterpart = next((item for item in gsmarena_smartphones if current_smartphone_in_db['name'] in item.get('name', '')), None)
            if closest_counterpart:
                current_smartphone_in_db['processor'] = closest_counterpart.get('chipset')
                # upsert_to_json('remaining', current_smartphone_in_db)
            else:
                closest_counterpart_2 = next((item for item in gsmarena_smartphones if item.get('name') in current_smartphone_in_db['name']), None)
                if closest_counterpart_2:
                    current_smartphone_in_db['processor'] = closest_counterpart_2.get('chipset')
                    upsert_to_json('remaining2', current_smartphone_in_db)
                else:
                    upsert_to_json('not_found', current_smartphone_in_db)
                    phones_with_no_match_in_gsmarena.append(current_smartphone_in_db['name'])
    
    print(f'Phones with no match in gsmarena: {phones_with_no_match_in_gsmarena}')

def process_updated_data():
    final_data = []
    immediately_updated_smartphones = read_json_file('updated_all')
    remaining_smartphones = read_json_file('remaining')
    remaining_smartphones_2 = read_json_file('remaining2')

    final_data.extend(immediately_updated_smartphones)
    final_data.extend(remaining_smartphones)
    final_data.extend(remaining_smartphones_2)

    print(f'Final data: {final_data}')
    upsert_to_json('to_be_inserted', final_data)

def main():
    # Supabase project details
    DATABASE_URL = "https://teprmsxuirxhmriekpgh.supabase.co"
    DATABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRlcHJtc3h1aXJ4aG1yaWVrcGdoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTkwMjc3ODcsImV4cCI6MjAzNDYwMzc4N30.QYQtPCuyKuwUM_QD8UlPVPQXIl-JL1rCT_vC9gFucFA"

    # Connect to Supabase
    supabase = create_client(DATABASE_URL, DATABASE_KEY)
    
    # Read data from JSON file
    # insert_to_db(supabase, read_json_file("final_Apple"), 'smartphones')
    # insert_to_db(supabase, read_json_file("final_Samsung"), 'smartphones')
    # insert_to_db(supabase, read_json_file("final_Xiaomi"), 'smartphones')

    # insert_to_db(supabase, read_json_file("antutu_rank1"), 'antutu')
    # insert_to_db(supabase, read_json_file("antutu_ios1"), 'antutu')

    # testink()
    # process_updated_data()
    insert_to_db(supabase, read_json_file("to_be_inserted"), 'smartphones')


if __name__ == "__main__":
    main()
