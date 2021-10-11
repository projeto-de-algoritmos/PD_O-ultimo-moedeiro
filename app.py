import pyxel
import graphics.botao as bt
import graphics.score as sc
import utils as ut

class App:
    def __init__(self):
        pyxel.init(ut.WIDTH, ut.HEIGHT, caption="O Último Moedeiro")
        pyxel.mouse(True)

        self.score = sc.Score(10)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.score.update(1)

    def draw(self):
        pyxel.cls(0)

        self.score.draw()

App()
