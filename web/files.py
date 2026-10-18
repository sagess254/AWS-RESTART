import json


employees = {
    "name": "Spongebob",
    "Age": 24,
    "job": "Cloud Engineer"
}

file_path = "C:/Users/user/OneDrive/Desktop/output.json"
try:
    with open(file_path, "w") as file:
        json.dump(employees, file, indent=4)
        print(f"json file  '{file_path}' was created")
except FileExistsError:
    print("That file exists")


