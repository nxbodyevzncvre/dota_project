import sys
import pyautogui as pg
import config

sys.path.append(r"E:\python\titan")
from titan_algo import login_steam

sys.path.append(r"E:\python\dota")
from dota_algo import dota_algo

sys.path.append(r"E:\python\users")
from user_algo import take_data, delete, user_data


def main():
    while dict:
        login, password = take_data(user_data)
        login_steam(config.main_login, config.main_pass)
        dota_algo()
        login_steam(login, password)
        dota_algo()
        delete()    

if __name__ == '__main__':
    main()