import pyautogui as pg
import config
from time import sleep
import sys
sys.path.append(r"E:\python\users")

def login_steam(login, password):
    sleep(5)
    pg.click((config.log["log-x"]), (config.log["log-y"]))
    pg.typewrite(login)
    sleep(0.5)
    pg.click((config.passw["passw-x"]), (config.passw["passw-y"]))
    pg.typewrite(password)
    sleep(0.5)
    pg.click((config.btn["enter-x"]), (config.btn["enter-y"]))
    sleep(5)