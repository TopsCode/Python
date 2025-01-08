import json

# Create an empty dictionary to store user input
user_data = {}

# Accept user input
user_data["name"] = input("Enter your name: ")
user_data["age"] = int(input("Enter your age: "))
user_data["city"] = input("Enter your city: ")

# Open a JSON file in write mode
with open("user_data.json", "w") as file:
    # Write the dictionary to the file in JSON format
    json.dump(user_data, file, indent=4)

print("Data has been written to user_data.json")
