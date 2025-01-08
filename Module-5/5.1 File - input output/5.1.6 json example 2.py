import json

# Create an empty list to store multiple users' data
users_data = []

# Accept the number of users
num_users = int(input("Enter the number of users: "))

# Loop to accept input for each user
for n in range(num_users):
    user_data = {}
    user_data["name"] = input("Enter user's name: ")
    user_data["age"] = int(input("Enter user's age: "))
    user_data["city"] = input("Enter user's city: ")
    
    # Append user data to the list
    users_data.append(user_data)

# Write the list of users to a JSON file
with open("users_data.json", "w") as file:
    json.dump(users_data, file, indent=4)

print("All users' data has been written to users_data.json")
