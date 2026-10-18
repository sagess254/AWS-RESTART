import json
# reading files in txt,json 

file_path = "C:/Users/user/OneDrive/Desktop/output.json"

try:
    with  open(file_path, 'r') as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("This file was not found")



