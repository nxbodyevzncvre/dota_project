import pyautogui as pg
import config
from time import sleep

def dota_algo():
    sleep(4)
    pg.click(config.library["x"], config.library["y"])
    sleep(1)
    pg.click(config.search["search-x"], config.search["search-y"])
    sleep(1)
    pg.typewrite("dota")
    sleep(1)
    pg.click(config.dota["dota-x"], config.dota["dota-y"])
    sleep(2)
    pg.click(config.play_steam["play-x"], config.play_steam["play-y"])
    sleep(25)
    pg.click(config.game["game-x"], config.game["game-y"])
    sleep(1)
    pg.click(config.dota_plus["dota_plus-x"], config.dota_plus["dota_plus-y"])
    sleep(2)
    pg.click(config.game["game-x"], config.game["game-y"])
    sleep(2)
    pg.click(config.allpick["allpick-x"], config.allpick["allpick-y"])
    sleep(2)
    pg.click(config.game["game-x"], config.game["game-y"])
    sleep(2)
    pg.click(config.cancel_game["cancel-x"], config.cancel_game["cancel-y"])
    sleep(7)
    pg.click(config.game["game-x"], config.game["game-y"])
    sleep(2)
    pg.click(config.game["game-x"], config.game["game-y"])
    sleep(6)
    pg.click(config.cancel_game["cancel-x"], config.cancel_game["cancel-y"])
    sleep(7)
    pg.click(config.settings["settings-x"], config.settings["settings-y"])
    sleep(0.5)
    pg.click(config.account["account-x"], config.account["account-y"])
    sleep(0.5)
    pg.click(config.recal["recal-x"], config.recal["recal-y"])
    sleep(2)
    # add recal_accept
    pg.click(config.cancel_game["cancel-x"], config.cancel_game["cancel-y"])
    sleep(1.5)
    pg.click(config.exit_from_dota["exit_from_dota-x"], config.exit_from_dota["exit_from_dota-y"])
    sleep(10)
    pg.click(config.exit_from_dota_accept["exit_from_dota_accept-x"], config.exit_from_dota_accept["exit_from_dota_accept-y"])
    sleep(20) 
    pg.click(config.account_exit_settings["account_exit_settings-x"], config.account_exit_settings["account_exit_settings-y"])
    sleep(2)
    pg.click(config.account_exit_settings["account_exit_settings-x"], config.account_exit_settings["account_exit_settings-y"])
    sleep(10)
    pg.click(config.account_exit["account_exit-x"], config.account_exit["account_exit-y"])
    sleep(10)
    pg.click(config.account_exit_accept["account_exit_accept-x"], config.account_exit_accept["account_exit_accept-y"])
    sleep(10)
    pg.click(config.add_account["add_account-x"], config.add_account["add_account-y"])
    sleep(4)