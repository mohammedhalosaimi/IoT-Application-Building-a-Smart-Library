"""
Create a file called dbInfo.json.
Copy the following code into it and adjust it to suit your DB.
{
    "address": "0.0.0.0",
    "username": "root",
    "password":"your_password"
}
"""
import json
import os

class cloud_db:

    @staticmethod
    def load_json():
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'dbInfo.json')
        with open(filename, 'r') as j:
            return json.load(j)

if __name__ == "__main__":
    values = cloud_db.load_json()
    print(values["address"])