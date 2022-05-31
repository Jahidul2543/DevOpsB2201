import json
from self import self


"""
Deserializing JSON
JSON	--->    Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""


def read_data():
    with open("data/data.json", "r") as read_file:
        file_data = json.load(read_file)
        print(file_data)
        print(type(file_data))
        print(file_data["president"]["hobby"][0])


if __name__ == "__main__":
    read_data()