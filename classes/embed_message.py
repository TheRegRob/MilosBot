# --- embed_message.py ------------------------------------------------ #
# --------------------------------------------------------------------- #
# Date   :	02/12/2023                                                  #
# Author :	Robin Reggiani                                              #
# --------------------------------------------------------------------- #

# --- Imports --------------------------------------------------------- #
# --------------------------------------------------------------------- #

# --- Constants ------------------------------------------------------- #
# --------------------------------------------------------------------- #


# --- Constructors ---------------------------------------------------- #
class EmbedMessage:
    def __init__(self, _isEmbed, _description=None, _title=None, _type=None,
                 _color=None, _image=None, _thumbnail=None, _thumbfile=None, _imgfile=None):
        self.isEmbed = _isEmbed
        self.title = _title
        self.description = _description
        self.type = _type
        self.color = _color
        self.image = _image
        self.thumbnail = _thumbnail
        self.thumbfile = _thumbfile
        self.imgfile = _imgfile
# --------------------------------------------------------------------- #

# --- Methods & Functions --------------------------------------------- #
# --------------------------------------------------------------------- #
