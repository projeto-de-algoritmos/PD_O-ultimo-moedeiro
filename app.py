import pyxel
import graphics.botao as bt
import graphics.text as tx
import utils as ut

class App:
    def __init__(self):
        pyxel.init(ut.WIDTH, ut.HEIGHT, caption="O Último Moedeiro")
        pyxel.mouse(True)

        self.qtd = 1

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.qtd+=1

    def draw(self):
        pyxel.cls(0)
        s = 'teste {}'.format(self.qtd)
        tx.Centered_text(s, 10, 7).draw()
        tx.Centered_text('Testanto texto muito grande', 16, 7).draw()

App()
