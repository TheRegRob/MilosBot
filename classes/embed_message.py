class EmbedMessage():
    def __init__(self, _isEmbed, _description, _title=None, _type=None, _color=None, _image=None, _thumbnail=None):
        self.isEmbed = _isEmbed
        self.title = _title
        self.description = _description
        self.type = _type
        self.color = _color
        self.image = _image
        self.thumbnail = _thumbnail