# --- main.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
import json
from typing import Any

import discord

import milosbot.milos as milos

# --------------------------------------------------------------------- #

# --- Constants ------------------------------------------------------- #
# --------------------------------------------------------------------- #
RES_PICTURES_PATH = "data/resources/pictures/"
RES_GIFS_PATH = "data/resources/gifs/"


# --- Data structures ------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #
imgs_dict = {}
gifs_dict = {}

# --- Methods & Functions --------------------------------------------- #
# --------------------------------------------------------------------- #
wtfdoggo_img = discord.File('data/resources/pictures/WTF_Doggo.PNG')

fl_agostini = open('data/resources/gifs/Elfa/Agostini.json')
agostini_gifs = json.load(fl_agostini)
fl_agostini.close()

fl_billy_herrington = open('data/resources/gifs/Gachi/BillyHerrington.json')
billy_gifs = json.load(fl_billy_herrington)
fl_billy_herrington.close()

fl_brad_mcguire = open('data/resources/gifs/Gachi/BradMcGuire.json')
brad_gifs = json.load(fl_brad_mcguire)
fl_brad_mcguire.close()

fl_danny_lee = open('data/resources/gifs/Gachi/DannyLee.json')
danny_gifs = json.load(fl_danny_lee)
fl_danny_lee.close()

fl_gachies = open('data/resources/gifs/Gachi/Gachies.json')
gachies_gifs = json.load(fl_gachies)
fl_gachies.close()

fl_mark_wolff = open('data/resources/gifs/Gachi/MarkWolff.json')
mark_gifs = json.load(fl_mark_wolff)
fl_mark_wolff.close()

fl_ricardo_milos = open('data/resources/gifs/Gachi/RicardoMilos.json')
milos_gifs = json.load(fl_ricardo_milos)
fl_ricardo_milos.close()

fl_seasonals = open('data/resources/gifs/Gachi/Seasonals.json')
seasonals_gifs = json.load(fl_seasonals)
fl_seasonals.close()

fl_steve_rambo = open('data/resources/gifs/Gachi/SteveRambo.json')
steve_gifs = json.load(fl_steve_rambo)
fl_steve_rambo.close()

fl_van_darkholme = open('data/resources/gifs/Gachi/VanDarkholme.json')
van_gifs = json.load(fl_van_darkholme)
fl_van_darkholme.close()

fl_token = open('data/restricted/token.json')
token = json.load(fl_token)
fl_token.close()

fl_cmds = open('data/resources/commands.json')
cmds = json.load(fl_cmds)
fl_cmds.close()

fl_triggers = open('data/resources/triggers.json')
triggers = json.load(fl_triggers)
fl_triggers.close()

gifs_dict["Agostini"] = agostini_gifs
gifs_dict["BillyHerrington"] = billy_gifs
gifs_dict["BradMcGuire"] = brad_gifs
gifs_dict["DannyLee"] = danny_gifs
gifs_dict["Gachies"] = gachies_gifs
gifs_dict["MarkWolff"] = mark_gifs
gifs_dict["RicardoMilos"] = milos_gifs
gifs_dict["Seasonals"] = seasonals_gifs
gifs_dict["SteveRambo"] = steve_gifs
gifs_dict["VanDarkholme"] = van_gifs

imgs_dict["WTF_Doggo"] = wtfdoggo_img


def reload_files():
    global wtfdoggo_img
    wtfdoggo_img = discord.File('data/resources/pictures/WTF_Doggo.PNG')
    imgs_dict["WTF_Doggo"] = wtfdoggo_img

# --- Main ------------------------------------------------------------ #
# --------------------------------------------------------------------- #
if __name__ == '__main__':
    milos.milos_run()
