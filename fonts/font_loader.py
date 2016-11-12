import pygame.font as pyfont


class UIFont(object):
    def __init__(self, font, size, font_name):
        self.font = font
        self.size = size
        self.font_name = font_name

    def __str__(self):
        return "{} - Size {}".format(self.font_name, self.size)

    def __repr__(self):
        return self.__str__()

class FontLoader(object):

    def __init__(self, default_font=pyfont.get_default_font(), default_size=16):
        pyfont.init()
        self.default_font = UIFont(pyfont.Font(default_font, default_size), default_size, default_font)
        self.fonts = {self.serialize(default_font, default_size) : self.default_font}

    def serialize(self, font_name, size):
        return "{} - Size {}".format(font_name, size)


    def get_default_font(self):
        return self.default_font

    def get_font(self, font_name, size):
        s_name = self.serialize(font_name, size)
        if s_name in self.fonts.iterkeys():
            return self.fonts[s_name]
        uif = UIFont(pyfont.Font(font_name, size), size, font_name)
        self.fonts[s_name] = uif
        return uif

