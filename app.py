import pyxel
import graphics.botao as bt
import graphics.text as tx
import utils as ut

class App:
    def __init__(self):
        pyxel.init(ut.WIDTH, ut.HEIGHT, caption="O Último Moedeiro")
        pyxel.mouse(True)

        self.qtdMoedas = 3
        self.retira1 = 2
        self.retira2 = 3

        self.botoes_qtdMoedas= [bt.Retangular_button(ut.WIDTH/2 - 40, ut.HEIGHT - 37, '+'), bt.Retangular_button(ut.WIDTH/2 - 40, ut.HEIGHT - 17, '-')]
        self.botoes_retira1 = [bt.Retangular_button(ut.WIDTH/2 - 30, ut.HEIGHT - 37, '+'), bt.Retangular_button(ut.WIDTH/2 - 30, ut.HEIGHT - 17, '-')]
        self.botoes_retira2 = [bt.Retangular_button(ut.WIDTH/2 - 20, ut.HEIGHT - 37, '+'), bt.Retangular_button(ut.WIDTH/2 - 20, ut.HEIGHT - 17, '-')]
        self.botao_start = bt.Normal_button(ut.WIDTH/2, ut.HEIGHT - 30 , 'Comecar Jogo')

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.botoes_qtdMoedas[0].update() == 1 and self.qtdMoedas + 1 < 100: self.qtdMoedas += 1
        if self.botoes_qtdMoedas[1].update() == 1 and self.qtdMoedas - 1 > self.retira2: self.qtdMoedas -= 1
        if self.botoes_retira1[0].update() == 1 and self.retira1 + 1 < self.retira2: self.retira1 += 1
        if self.botoes_retira1[1].update() == 1 and self.retira1 - 1 > 1: self.retira1 -= 1
        if self.botoes_retira2[0].update() == 1 and self.retira2 + 1 <= self.qtdMoedas: self.retira2 += 1
        if self.botoes_retira2[1].update() == 1 and self.retira2 - 1 > self.retira1: self.retira2 -= 1

    def draw(self):
        pyxel.cls(0)
        s = 'Bem vindo ao ultimo moedeiro\no objetivo desse jogo\ne pegar a ultima moeda\nporem voce so pode pegar\numa quantidade determinada.\nPara iniciar o jogo\nescolha as 2 quantidades possíveis\nincluindo o valor 1.'.splitlines()
        for i in range(len(s)): tx.Centered_text(s[i], 60 + 6 * i, 7).draw()
        for botoes in self.botoes_qtdMoedas: botoes.draw()
        for botoes in self.botoes_retira1: botoes.draw()
        for botoes in self.botoes_retira2: botoes.draw()
        tx.Centered_text(str(self.qtdMoedas), ut.HEIGHT - 25, 7, ut.WIDTH/2 - (38 if len(str(self.qtdMoedas)) == 1 else 40)).draw()
        tx.Centered_text(str(self.retira1), ut.HEIGHT - 25, 7, ut.WIDTH/2 - (28 if len(str(self.retira1)) == 1 else 30)).draw()
        tx.Centered_text(str(self.retira2), ut.HEIGHT - 25, 7, ut.WIDTH/2 - (18 if len(str(self.retira2)) == 1 else 20)).draw()
        self.botao_start.draw()

App()
