import sys
sys.path.append(r"E:\python")
from readfile import read_details
import config

user_data = read_details("accs.txt")

def take_data(user_data):
    login = (tuple(user_data.items())[0][1][0])
    password = (tuple(user_data.items())[1][1][0])
    return login, password

def delete():
    user_data["login"].pop(0)
    user_data["password"].pop(0)
    if not user_data["login"]:
        del user_data["login"]
    if not user_data["password"]:
        del user_data["password"]

    print(f"{user_data} ---- changed")