import json

# First we have to create the employee.json file with the following contents:

employees = [
    {
        "name": "Imran Abdul",
        "DOB": "04-07-1994",
        "height": "5'7\"",
        "city": "Hyderabad",
        "state": "Telangana State",
    },
    {
        "name": "Nikola Tesla",
        "DOB": "10-07-1972",
        "height": "5'10\"",
        "city": "Banglore",
        "state": "Karnataka",
    },
    {
        "name": "Albert Einstein",
        "DOB": "14-03-1978",
        "height": "5'9\"",
        "city": "Chennai",
        "state": "Tamil Nadu",
    },
    {
        "name": "Carl Sagan",
        "DOB": "23-12-1983",
        "height": "5'8\"",
        "city": "Mumbai",
        "state": "Maharashtra",
    },
    {
        "name": "Mary Curie",
        "DOB": "19-04-1979",
        "height": "5'5\"",
        "city": "Gandhinagar",
        "state": "Gujarat",
    },
    {
        "name": "Neil deGrasse Tyson",
        "DOB": "12-08-1989",
        "height": "5'10\"",
        "city": "Itanagar",
        "state": "Arunachal Pradesh",
    },
]

# Now write the above data to the employee.json file.

with open("employee.json", "w") as file:
    json.dump(employees, file)

# create an employee class with name,dob,height,city and state initializer parameters
class Employee:
    def __init__(self, name, DOB, height, city, state):
        self.name = name
        self.DOB = DOB
        self.height = height
        self.city = city
        self.state = state

# write a function that will read the json file and append the values of file as parameters of class Employee
def read_employee_info(filename):

    employee_list = []

    with open(filename, "r") as f:
        data = json.load(f)

    for employee in data:
        employee_list.append(
            Employee(
                employee["name"],
                employee["DOB"],
                employee["height"],
                employee["city"],
                employee["state"],
            )
        )

    return employee_list


def main():

    file_path = r"employee.json"
    emp_list = read_employee_info(file_path)

    for employee in emp_list:
        print(f"Name: {employee.name}")
        print(f"DOB: {employee.DOB}")
        print(f"Height: {employee.height}")
        print(f"City: {employee.city}")
        print(f"State: {employee.state}")
        print("----------------")


if __name__ == "__main__":
    main()
