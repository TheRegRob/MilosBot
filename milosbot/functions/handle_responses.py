# --- handle_responses.py --------------------------------------------------------- #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
from main import triggers
import classes.embed_message
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
                    return classes.embed_message.EmbedMessage(_isEmbed=False, _description=dataz['IMAGE'][idx])
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
