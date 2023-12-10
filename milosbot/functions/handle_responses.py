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
import data.resources.pictures as res
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
    idxf_th: int
    idxf_i: int
    thumb_name_fold: str = ""
    img_name_fold: str = ""
    thumb_file: discord.File = None
    img_file: discord.File = None
    if data['FOLD_THUMB'] != "":
        # Thumbnail val is from local
        if str(data['FOLD_THUMB']).startswith("gifs/"):
            s = str(data['FOLD_THUMB'].replace("gifs/", ''))
            thumb_name_fold = RES_GIFS_PATH + s
            thumb_path = os.listdir(thumb_name_fold)
        else:
            s = str(data['FOLD_THUMB'].replace("pictures/", ''))
            thumb_name_fold = RES_PICTURES_PATH + s
            thumb_path = os.listdir(thumb_name_fold)
        idxf_th = random.randint(0,  len(thumb_path) - 1)
        thumb_file_name = thumb_path[idxf_th]
        thumb_file = discord.File(thumb_name_fold + "/" + thumb_file_name)

    if data['FOLD_IMG'] != "":
        # Img val is from local
        if str(data['FOLD_IMG']).startswith("gifs/"):
            s = str(data['FOLD_IMG'].replace("gifs/", ''))
            img_name_fold = RES_GIFS_PATH + s
            img_path = os.listdir(img_name_fold)
        else:
            s = str(data['FOLD_IMG'].replace("pictures/", ''))
            img_name_fold = RES_PICTURES_PATH + s
            img_path = os.listdir(img_name_fold)
        idxf_i = random.randint(0,  len(img_path) - 1)
        img_file_name = img_path[idxf_i]
        img_file = discord.File(img_name_fold + "/" + img_file_name)

    idx_i = random.randint(0, len(data['IMAGE']) - 1)
    idx_th = random.randint(0, len(data['THUMB']) - 1)
    idx_t = random.randint(0,  len(data['TITLE']) - 1)
    idx_d = random.randint(0,  len(data['DESC']) - 1)
    return classes.embed_message.EmbedMessage(_isEmbed=True,
                                              _title=data['TITLE'][idx_t],
                                              _description=data['DESC'][idx_d],
                                              _type='rich',
                                              _color=0xD37DA3,
                                              _image=data['IMAGE'][idx_i],
                                              _thumbnail=data['THUMB'][idx_th],
                                              _thumbfile=thumb_file,
                                              _imgfile=img_file)


def build_not_embed_response(data) -> classes.embed_message.EmbedMessage:
    idx_ig = 0
    idx_ii = 0
    gifs_list = []
    imgs_list = []
    img_name_fold: str = ""
    img_file: discord.File = None
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
            dict_copy = gifs_dict.copy()
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
                    for lk in gifs_dict.get(gf):
                        for f in data['IMAGE']:
                            if lk == f:
                                gifs_list.append(lk)
            idx_ig = 0 if len(gifs_list) == 0 else random.randint(0, len(gifs_list) - 1)
    idx_t = random.randint(0, len(data['TITLE']) - 1)
    idx_d = random.randint(0, len(data['DESC']) - 1)
    return classes.embed_message.EmbedMessage(_isEmbed=False,
                                               _description= None if len(gifs_list) == 0 else gifs_list[idx_ig],
                                               _imgfile=None if len(imgs_list) == 0 else imgs_list[idx_ii])



    #     # Img val is from dict
    #     for i in data['FOLD_IMG']:
    #
    #     if str(data['FOLD_IMG']).startswith("gifs/"):
    #         s = str(data['FOLD_IMG'].replace("gifs/", ''))
    #         img_name_fold = RES_GIFS_PATH + s
    #         img_path = os.listdir(img_name_fold)
    #     else:
    #         s = str(data['FOLD_IMG'].replace("pictures/", ''))
    #         img_name_fold = RES_PICTURES_PATH + s
    #         img_path = os.listdir(img_name_fold)
    #     idx_i = random.randint(0, len(img_path) - 1)
    #     img_file_name = img_path[idx_i]
    #     img_file = discord.File(img_name_fold + "/" + img_file_name)
    # else:
    #     idxf_i = random.randint(0, len(data['IMAGE']) - 1)
    #
    # idx_i = random.randint(0, len(data['IMAGE']) - 1)
    # idx_t = random.randint(0, len(data['TITLE']) - 1)
    # idx_d = random.randint(0, len(data['DESC']) - 1)
    # return classes.embed_message.EmbedMessage(_isEmbed=False,
    #                                           _description=data['IMAGE'][idx_i],
    #                                           _imgfile=img_file)


def manage_response(isEmbed: bool, data) -> classes.embed_message.EmbedMessage:
    if isEmbed:
        return build_embed_response(data)
    else:
        return build_not_embed_response(data)


def handle_response(message) -> classes.embed_message.EmbedMessage:
    p_message = message.lower()

    dataz = parse_trigger_data(p_message)
    if dataz is None:
        print("No reponse match found")
    else:
        return manage_response(dataz['EMBED'], dataz)

# --------------------------------------------------------------------- #
