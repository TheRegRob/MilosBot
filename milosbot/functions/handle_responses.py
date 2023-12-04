# --- handle_responses.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
from main import triggers
import data.resources.gifs.linked
import classes.embed_message
import random
# --------------------------------------------------------------------- #

# --- Data structures ------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Variables ------------------------------------------------------- #
# --------------------------------------------------------------------- #


# --- Methods & Functions --------------------------------------------- #
def handle_situani_response() -> classes.embed_message.EmbedMessage:
    print("Preparing situani response...")

    title = "YOU LIKE EMBARASSING ME AH?"
    description = "<@!140743498209951744>"
    type = 'rich'
    color = 0xD37DA3
    image = "https://c.tenor.com/VDb2gH3UgN4AAAAd/billy-herrington-shocked.gif"
    thumbnail = "https://c.tenor.com/xizbYp13rqEAAAAd/gachi-gachimuchi.gif"

    embed = classes.embed_message.EmbedMessage(_isEmbed=True,
                                               _title=title,
                                               _description=description,
                                               _type=type,
                                               _color=color,
                                               _image=image,
                                               _thumbnail=thumbnail)
    return embed


def handle_response(message) -> classes.embed_message.EmbedMessage:
    p_message = message.lower()

    match p_message:
        case p_message if triggers["str_gogo"] in p_message:
            print("'gogo' matched!")
            return classes.embed_message.EmbedMessage(_isEmbed=False, _description=data.resources.gifs.linked.GOGO_GIF)
        case p_message if any(x in p_message for x in triggers["str_cracra"]):
            print("'cracra' matched!")
            idx = random.randint(0, len(data.resources.gifs.linked.CRACRA_GIFS) - 1)
            return classes.embed_message.EmbedMessage(_isEmbed=False, _description=data.resources.gifs.linked.CRACRA_GIFS[idx])
        case p_message if triggers["str_situani"] in p_message:
            print("'situani' matched!")
            return handle_situani_response()
        case _:
            print("No reponse match found")
# --------------------------------------------------------------------- #
