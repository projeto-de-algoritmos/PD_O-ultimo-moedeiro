import pyxel
import utils as ut

class Centered_text:
    def __init__(self, text, y, col):
        self.text = text
        self.tam = len(self.text) * pyxel.FONT_WIDTH
        self.y = y
        self.col = col

    def update(self, text):
        self.text = text

    def draw(self):
        pyxel.text(ut.WIDTH/2 - self.tam/2, self.y, self.text, self.col)
