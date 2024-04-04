import pyautogui as pg
import config
from time import sleep



## 3)ALGORITHM FOR PASTING DATA(TITAN) ## 2)TAKE DATA
## 4)OPEN DOTA
## 5)START MATCH
## 6)TIME.SLEEP()
## 7)EXIT FROM DOTA
## 8)LOG OUT FROM STEAM

def login_titan(login, password):
    sleep(5)
    pg.click((config.log["log-x"]), (config.log["log-y"]))
    pg.typewrite(login)
    sleep(0.5)
    pg.click((config.passw["passw-x"]), (config.passw["passw-y"]))
    pg.typewrite(password)
    sleep(0.5)
    pg.click((config.btn["enter-x"]), (config.btn["enter-y"]))
    sleep(5)
