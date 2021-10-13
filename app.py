import pyxel
import graphics.botao as bt
import graphics.text as tx
import utils as ut
import moedeiro as md

class App:
    def __init__(self):
        pyxel.init(ut.WIDTH, ut.HEIGHT, caption="O Último Moedeiro")
        pyxel.mouse(True)

        self.game_state = 0

        self.qtdMoedas = 3
        self.retira1 = 2
        self.retira2 = 3

        self.rodada = 0
        self.jogador = 1
        self.memoization = []

        self.botoes_qtdMoedas= [bt.Retangular_button(ut.WIDTH/2 - 40, ut.HEIGHT - 37, '+'), bt.Retangular_button(ut.WIDTH/2 - 40, ut.HEIGHT - 17, '-')]
        self.botoes_retira1 = [bt.Retangular_button(ut.WIDTH/2 - 30, ut.HEIGHT - 37, '+'), bt.Retangular_button(ut.WIDTH/2 - 30, ut.HEIGHT - 17, '-')]
        self.botoes_retira2 = [bt.Retangular_button(ut.WIDTH/2 - 20, ut.HEIGHT - 37, '+'), bt.Retangular_button(ut.WIDTH/2 - 20, ut.HEIGHT - 17, '-')]
        self.botao_start = bt.Normal_button(ut.WIDTH/2, ut.HEIGHT - 30, 'Comecar Jogo')

        self.botoes_qtd = [bt.Normal_button(ut.WIDTH/2 - 30, ut.HEIGHT - 30, '1'),
                bt.Normal_button(ut.WIDTH/2, ut.HEIGHT - 30, str(self.retira1)),
                bt.Normal_button(ut.WIDTH/2 + 30, ut.HEIGHT - 30, str(self.retira2))]

        pyxel.run(self.update, self.draw)

    def restart_game(self):
        self.game_state = 0
        self.qtdMoedas = 3
        self.retira1 = 2
        self.retira2 = 3
        self.jogador = 1
        self.rodada = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_R):
            self.restart_game()

        if self.game_state == 0: self.update_state_0()
        elif self.game_state == 1: self.update_state_1()

    def update_state_0(self):
        if self.botoes_qtdMoedas[0].update() == 1 and self.qtdMoedas + 1 < 100: self.qtdMoedas += 1
        if self.botoes_qtdMoedas[1].update() == 1 and self.qtdMoedas - 1 >= self.retira2: self.qtdMoedas -= 1
        if self.botoes_retira1[0].update() == 1 and self.retira1 + 1 < self.retira2: self.retira1 += 1
        if self.botoes_retira1[1].update() == 1 and self.retira1 - 1 > 1: self.retira1 -= 1
        if self.botoes_retira2[0].update() == 1 and self.retira2 + 1 <= self.qtdMoedas: self.retira2 += 1
        if self.botoes_retira2[1].update() == 1 and self.retira2 - 1 > self.retira1: self.retira2 -= 1

        if self.botao_start.update() == 1:
            self.game_state = 1
            self.botoes_qtd[1].update_value(str(self.retira1))
            self.botoes_qtd[2].update_value(str(self.retira2))
            self.memoization = md.moedeiro(self.qtdMoedas, self.retira1, self.retira2)

    def update_state_1(self):
        if self.jogador == 1:
            if self.botoes_qtd[0].update() == 1 and self.qtdMoedas - 1 >= 0:
                self.qtdMoedas -= 1
                self.jogador = 0
            elif self.botoes_qtd[1].update() == 1 and self.qtdMoedas - self.retira1 >= 0:
                self.qtdMoedas -= self.retira1
                self.jogador = 0
            elif self.botoes_qtd[2].update() == 1 and self.qtdMoedas - self.retira2 >= 0:
                self.qtdMoedas -= self.retira2
                self.jogador = 0
        elif self.qtdMoedas > 0 and self.jogador == 0:
            self.qtdMoedas -= md.logicaBot(self.memoization, self.qtdMoedas, self.retira1, self.retira2)
            self.jogador = 1
            self.rodada += 1

        if self.qtdMoedas == 0:
            self.game_state = 2
            if self.rodada == 0: self.rodada += 1

    def draw(self):
        pyxel.cls(0)

        if self.game_state == 0: self.draw_state_0()
        elif self.game_state == 1: self.draw_state_1()
        elif self.game_state == 2: self.draw_state_2()

    def draw_state_0(self):
        s = 'Bem vindo ao ultimo moedeiro\no objetivo desse jogo\ne pegar a ultima moeda\nporem voce so pode pegar\numa quantidade determinada.\nPara iniciar o jogo\nescolha a quantidade de moedas\ne 2 quantidades possíveis\npara se retirar as moedas.'.splitlines()
        for i in range(len(s)): tx.Centered_text(s[i], 50 + 6 * i, 7).draw()
        for botoes in self.botoes_qtdMoedas: botoes.draw()
        for botoes in self.botoes_retira1: botoes.draw()
        for botoes in self.botoes_retira2: botoes.draw()
        tx.Centered_text(str(self.qtdMoedas), ut.HEIGHT - 25, 7, ut.WIDTH/2 - (38 if len(str(self.qtdMoedas)) == 1 else 40)).draw()
        tx.Centered_text(str(self.retira1), ut.HEIGHT - 25, 7, ut.WIDTH/2 - (28 if len(str(self.retira1)) == 1 else 30)).draw()
        tx.Centered_text(str(self.retira2), ut.HEIGHT - 25, 7, ut.WIDTH/2 - (18 if len(str(self.retira2)) == 1 else 20)).draw()
        self.botao_start.draw()

    def draw_state_1(self):
        s = 'TOTAL DE MOEDAS RESTANTES: {}'.format(self.qtdMoedas)
        tx.Centered_text(s, 6, 7).draw()
        for botoes in self.botoes_qtd: botoes.draw()

    def draw_state_2(self):
        s = 'VOCE GANHOU' if self.jogador == 0 else 'VOCE PERDEU'
        s += '\nEM {} RODADA{}\nAPERTE "R" PARA REINICIAR.'.format(self.rodada, "S" if self.rodada > 1 else "")
        s = s.splitlines()
        for i in range(len(s)): tx.Centered_text(s[i], 70 + 6 * i, 10).draw()

App()
