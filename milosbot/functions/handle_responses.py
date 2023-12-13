# --- handle_responses.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #
import math
from typing import Any
import os.path
from random import random
import discord
import os
# --- Imports --------------------------------------------------------- #
from main import triggers, gifs_dict, imgs_dict
from main import RES_PICTURES_PATH
from main import RES_GIFS_PATH
import classes.embed_message
import random


# --------------------------------------------------------------------- #

# --- Data structures ------------------------------------------------- #
# --------------------------------------------------------------------- #
class EmbedResponseParam:
    thumbnail_val: str
    image_val: str


class NotEmbedResponseParam:
    image_val: str


# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #


# --- Methods & Functions --------------------------------------------- #
def parse_trigger_data(p_msg) -> dict:
    for t in triggers:
        dataz = triggers[t]
        for s in dataz['TRIGGER']:
            if s in p_msg:
                return dataz

    return None


def build_embed_response(data) -> classes.embed_message.EmbedMessage:
    idx_thg = 0
    idx_thi = 0
    idx_ig = 0
    idx_ii = 0
    gifs_list_thumb = []
    imgs_list_thumb = []
    gifs_list_img = []
    imgs_list_img = []
    if data['FOLD_THUMB'][0] != "":
        # Sono selezionate le gifs_dict
        if data['THUMB'][0] == "":
            # Non ci sono filtri
            for gf in data['FOLD_THUMB']:
                dct = gifs_dict.get(gf)
                for e in dct:
                    gifs_list_thumb.append(dct[e])
        else:
            # Sono selezionati filtri
            for gf in data['FOLD_THUMB']:
                dct = gifs_dict.get(gf)
                for e in dct:
                    for f in data['THUMB']:
                        if e == f:
                            gifs_list_thumb.append(dct[e])
                            break
        idx_thg = 0 if len(gifs_list_thumb) == 0 else random.randint(0, len(gifs_list_thumb) - 1)

    if data['FOLD_IMG'][0] != "":
        # Sono selezionate le gifs_dict
        if data['IMAGE'][0] == "":
            # Non ci sono filtri
            for gf in data['FOLD_IMG']:
                dct = gifs_dict.get(gf)
                for e in dct:
                    gifs_list_img.append(dct[e])
        else:
            # Sono selezionati filtri
            for gf in data['FOLD_IMG']:
                dct = gifs_dict.get(gf)
                for e in dct:
                    for f in data['IMAGE']:
                        if e == f:
                            gifs_list_img.append(dct[e])
        idx_ig = 0 if len(gifs_list_img) == 0 else random.randint(0, len(gifs_list_img) - 1)

    idx_t = random.randint(0, len(data['TITLE']) - 1)
    idx_d = random.randint(0, len(data['DESC']) - 1)
    return classes.embed_message.EmbedMessage(_isEmbed=True,
                                              _title="_" if data['TITLE'][idx_t] == "" else data['TITLE'][idx_t],
                                              _description="_" if data['DESC'][idx_d] == "" else data['DESC'][idx_d],
                                              _type='rich',
                                              _color=0x007FFF,
                                              _thumbnail=None if len(gifs_list_thumb) == 0 else gifs_list_thumb[
                                                  idx_thg],
                                              _image=None if len(gifs_list_img) == 0 else gifs_list_img[idx_ig],
                                              _thumbfile=None if len(imgs_list_thumb) == 0 else imgs_list_thumb[
                                                  idx_thi],
                                              _imgfile=None if len(imgs_list_img) == 0 else imgs_list_img[idx_ii])


def build_not_embed_response(data) -> classes.embed_message.EmbedMessage:
    idx_ig = 0
    idx_ii = 0
    gifs_list = []
    imgs_list = []
    if data['FOLD_IMG'][0] != "":
        if data['FOLD_IMG'][0] == "Pictures":
            if data['IMAGE'][0] == "":
                # Seleziono random da tutti
                for e in imgs_dict("Pictures"):
                    imgs_list.append(imgs_dict[e])
            else:
                # Seleziono i file specificati
                for e in imgs_dict:
                    for f in data['IMAGE']:
                        if e == f:
                            imgs_list.append(imgs_dict[e])
            idx_ii = 0 if len(imgs_list) == 0 else random.randint(0, len(imgs_list) - 1)
        else:
            # Sono selezionate le gifs_dict
            if data['IMAGE'][0] == "":
                # Non ci sono filtri
                for gf in data['FOLD_IMG']:
                    dct = gifs_dict.get(gf)
                    for e in dct:
                        gifs_list.append(dct[e])
            else:
                # Sono selezionati filtri
                for gf in data['FOLD_IMG']:
                    dct = gifs_dict.get(gf)
                    for e in dct:
                        for f in data['IMAGE']:
                            if e == f:
                                gifs_list.append(dct[e])
                                break
            idx_ig = 0 if len(gifs_list) == 0 else random.randint(0, len(gifs_list) - 1)
    idx_t = random.randint(0, len(data['TITLE']) - 1)
    idx_d = random.randint(0, len(data['DESC']) - 1)
    return classes.embed_message.EmbedMessage(_isEmbed=False,
                                              _description=None if len(gifs_list) == 0 else gifs_list[idx_ig],
                                              _imgfile=None if len(imgs_list) == 0 else imgs_list[idx_ii])


def manage_response(isEmbed: bool, data) -> classes.embed_message.EmbedMessage:
    if isEmbed:
        return build_embed_response(data)
    else:
        return build_not_embed_response(data)


def handle_response(message) -> classes.embed_message.EmbedMessage:
    p_message = message.lower()

    dataz = parse_trigger_data(p_message)
    if dataz is None:
        pass
    else:
        return manage_response(dataz['EMBED'], dataz)
# --------------------------------------------------------------------- #
