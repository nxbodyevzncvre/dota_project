import sys
import pyautogui as pg
import config

sys.path.append(r"E:\python\titan")
from titan_algo import login_titan

sys.path.append(r"E:\python\dota")
from dota_algo import dota_algo

sys.path.append(r"E:\python\users")
#from user_algo import take_data, delete

## 9)TAKE DATA //COMPLETED
## 10)ALGORITHM FOR PASTING DATA(USER)
## 11)OPEN DOTA
## 12)START MATCH
## 13)TIME.SLEEP()
## 14)EXIT FROM DOTA
## 15)LOG OUT FROM STEAM






def main():
    # LOGGING TO STEAM
    login_titan(config.main_login, config.main_pass)
    dota_algo()
    




main()

# print(pg.position())