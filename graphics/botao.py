import pyxel
import random
import math

class Vect2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button:
    def __init__(self, x, y, text):
        self.pos = Vect2(x, y)
        self.size = len(text) * pyxel.FONT_WIDTH - 6
        self.text = text

    def update(self):
        mouse_pos = [pyxel.mouse_x, pyxel.mouse_y]
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.__check_button_hitbox(mouse_pos):
            return 1

    def draw(self):
        pyxel.rect(self.pos.x, self.pos.y + 2, self.size, 15, 3)
        pyxel.circ(self.pos.x, self.pos.y + 2 + 7, 7, 3)
        pyxel.circ(self.pos.x + self.size, self.pos.y + 2 + 7, 7, 3)
        pyxel.rect(self.pos.x, self.pos.y, self.size, 15, 11)
        pyxel.circ(self.pos.x, self.pos.y + 7, 7, 11)
        pyxel.circ(self.pos.x + self.size, self.pos.y + 7, 7, 11)
        pyxel.text(self.pos.x - 2, self.pos.y + pyxel.FONT_HEIGHT - 1, self.text, 7)

    def __check_button_hitbox(self, mouse_pos):
        if math.dist([self.pos.x, self.pos.y + 7], mouse_pos) < 7: return True
        elif mouse_pos[0] >= self.pos.x and mouse_pos[0] <= self.pos.x + 15 and mouse_pos[1] >= self.pos.y and mouse_pos[1] <= self.pos.y + 15: return True
        elif math.dist([self.pos.x + 15, self.pos.y + 7], mouse_pos) < 7: return True
        return False
        
class App:
    def __init__(self):
        pyxel.init(200, 150, caption="O Último Moedeiro")
        pyxel.mouse(True)
        self.botao = Button(20, 20, '7')
        self.botao2 = Button(60, 20, 'ASfa')

        self.pixels_tela = []

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.botao.update() == 1:
            print('clicou')

    def draw(self):
        pyxel.cls(0)
        self.botao.draw()
        self.botao2.draw()

App()
