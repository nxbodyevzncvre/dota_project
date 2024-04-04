import sys
sys.path.append(r"E:\python")
from readfile import read_details

def take_data():
    global dict
    dict = read_details("accs.txt")
    login = (tuple(dict.items())[0][1][0])
    password = (tuple(dict.items())[1][1][0])
    # return login, password
    print(dict)

def delete():
    dict["login"].pop(0)
    dict["password"].pop(0)
    print(f"{dict} ---- changed")

take_data()
delete()
delete()
