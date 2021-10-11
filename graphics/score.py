import pyxel
import utils as ut

class Score:
    def __init__(self, qtdRestante):
        self.qtdRestantes = qtdRestante
        self.text = 'Quantidade de Moedas Restantes: {}'
        self.tam = len(self.text) * pyxel.FONT_WIDTH

    def update(self, qtdMoedas):
        self.qtdRestantes -= qtdMoedas

    def draw(self):
        text = self.text.format(self.qtdRestantes)
        pyxel.text(ut.WIDTH/2 - self.tam/2, pyxel.FONT_HEIGHT - 1, text, 7)
