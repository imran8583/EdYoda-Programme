# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

indian_states = {
    "Telangana": "Hyderabad",
    "Karnataka": "Banglore",
    "Maharastra": "Mumbai",
    "West Bengal": "Kolkata",
    "Tamil Nadu": "Chennai",
    "Rajasthan": "Jaipur",
    "Uttarakhand": "Dehradun",
}

# Create a new json file in write mode to add above data into it.
with open(r"indian_states.json", "w") as file:

    # Write the dictionary to the file in JSON format
    json.dump(indian_states, file)


with open(r"indian_states.json", "r") as file:
    data = file.readlines()
    print(data)