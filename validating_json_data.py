import json

# Path to the JSON file
json_file_path = '/mnt/data/WH1HFGJHJ0.json'

# List of specific localizationKey values to check for
values_to_check = [
    "test.prod1553.2749.result0",
    "test.prod1553.3745.result0",
    "test.prod1553.3738.resultM101",
    "test.prod1553.3744.result0",
    "test.prod1553.4005.result0",
    "test.prod1553.4003.result0",
    "test.prod1553.4002.result0",
    "test.prod1553.4004.result0",
    "test.prod1553.4008.result0",
    "test.prod1553.4009.result0",
    "test.prod1553.4009.result0",
    "test.prod1553.4006.result0",
    "test.prod1553.4007.result0",
    "test.prod1553.2749.result0",
    "test.prod1553.4009.result0",
    "test.prod1553.2749.result0",
    "test.prod1553.8291.result0",
    "test.prod1553.8313.result0",
    "test.prod1553.8231.result0",
    "test.prod1553.2749.result0",
    "test.prod1553.8222.result0",
    "test.prod1553.8334.result0",
    "test.prod1553.2749.result0",
    "test.prod1553.8284.result0",
    "test.prod1553.8357.result0",
    "test.prod1553.8401.result0",
    "test.prod1553.8398.result0",
    "test.prod1553.8400.result0",
    "test.prod1553.8397.result0",
    "test.prod1553.4615.result0"
]

# Load the JSON data from the file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# ANSI escape codes for coloring
RED = '\033[91m'
ENDC = '\033[0m'

# Function to recursively search for the 'localizationKey' in the JSON data
def find_localization_keys(obj, keys, values_to_check, found_values, differing_values):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'localizationKey':
                keys.append(value)
                if value in values_to_check:
                    found_values.append(value)
                else:
                    differing_values.append(value)
            elif isinstance(value, (dict, list)):
                find_localization_keys(value, keys, values_to_check, found_values, differing_values)
    elif isinstance(obj, list):
        for item in obj:
            find_localization_keys(item, keys, values_to_check, found_values, differing_values)

# Lists to store the found 'localizationKey' values and differing values
localization_keys = []
found_values = []
differing_values = []

# Find all 'localizationKey' values in the JSON data and check for the specific values
find_localization_keys(data, localization_keys, values_to_check, found_values, differing_values)

# Print the found 'localizationKey' values
print("Found localizationKey values:")
for key in localization_keys:
    print(key)

# Validate if the specific values exist in the JSON data
print("\nValidation Results:")
for value in values_to_check:
    if value in found_values:
        print(f"The value '{value}' exists in the file.")
    else:
        print(f"{RED}The value '{value}' does NOT exist in the file.{ENDC}")

# Print any differing values found in the file
print("\nDiffering Values:")
for value in differing_values:
    print(f"{RED}Differing value found: '{value}'{ENDC}")
