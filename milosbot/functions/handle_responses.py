# --- handle_responses.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #
import discord
import os
# --- Imports --------------------------------------------------------- #
from main import triggers
from main import RES_PATH
import classes.embed_message
import data.resources.pictures as res
import random
# --------------------------------------------------------------------- #

# --- Data structures ------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #


# --- Methods & Functions --------------------------------------------- #
def handle_response(message) -> classes.embed_message.EmbedMessage:
    p_message = message.lower()

    for t in triggers:
        dataz = triggers[t]
        for s in dataz['TRIGGER']:
            if s in p_message:
                if not dataz['EMBED']:
                    idx = random.randint(0, len(dataz['IMAGE']) - 1)
                    s_image: str = dataz['IMAGE'][idx]
                    if s_image.startswith("https"):
                        return classes.embed_message.EmbedMessage(_isEmbed=False, _description=s_image)
                    else:
                        f_path: str = RES_PATH + s_image
                        f_image = discord.File(f_path)
                        return classes.embed_message.EmbedMessage(_isEmbed=False, _file=f_image)
                else:
                    idx_t = random.randint(0, len(dataz['TITLE']) - 1)
                    idx_d = random.randint(0, len(dataz['DESC']) - 1)
                    idx_i = random.randint(0, len(dataz['IMAGE']) - 1)
                    idx_th = random.randint(0, len(dataz['THUMB']) - 1)
                    return classes.embed_message.EmbedMessage(_isEmbed=True,
                                                              _title=dataz['TITLE'][idx_t],
                                                              _description=dataz['DESC'][idx_d],
                                                              _type='rich',
                                                              _color=0xD37DA3,
                                                              _image=dataz['IMAGE'][idx_i],
                                                              _thumbnail=dataz['THUMB'][idx_th])
    print("No reponse match found")
# --------------------------------------------------------------------- #
