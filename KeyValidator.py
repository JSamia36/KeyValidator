import argparse
import subprocess
import json
import re
import concurrent.futures

def read_list(file_path):
    with open(file_path, 'r') as file:
        # Extract the API key from each line using regex
        return [re.search(r'\b[A-Fa-f0-9-]{36}\b', line).group() for line in file if re.search(r'\b[A-Fa-f0-9-]{36}\b', line)]

def run_command(item):
    command = f'curl -s -X POST https://api.heroku.com/apps -H "Accept: application/vnd.heroku+json; version=3" -H "Authorization: Bearer {item}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return item, result.stdout

def check_validity(response):
    try:
        response_json = json.loads(response)
        if response_json.get("id") == "unauthorized" and response_json.get("message") == "Invalid credentials provided.":
            return "Invalid"
    except json.JSONDecodeError:
        pass
    return "Valid"

def print_result(item, validity):
    if validity == "Invalid":
        print(f'{item} : \033[31m{validity}\033[0m')  # Red for "Invalid"
    else:
        print(f'{item} : \033[32m{validity}\033[0m')  # Green for "Valid"

def process_item(item):
    response = run_command(item)
    validity = check_validity(response[1])
    print_result(response[0], validity)

def main():
    parser = argparse.ArgumentParser(description='Run a command for each item in a list')
    parser.add_argument('-l', '--list', required=True, help='Path to the list file')
    
    args = parser.parse_args()
    
    items = read_list(args.list)
    
    # Use ThreadPoolExecutor to run commands concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_item, items)

if __name__ == "__main__":
    main()
