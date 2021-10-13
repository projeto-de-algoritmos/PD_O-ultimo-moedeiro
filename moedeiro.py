def moedeiro (qtdMoedas, retira1, retira2):
    memoization = [0 for i in range(qtdMoedas+1)]
    memoization[0] = False
    memoization[1] = True

    for i in range(2, qtdMoedas+1):
        if (i - 1 >= 0 and not memoization[i - 1]): memoization[i] = True
        elif (i - retira1 >= 0 and not memoization[i - retira1]): memoization[i] = True
        elif (i - retira2 >= 0 and not memoization[i - retira2]): memoization[i] = True
        else: memoization[i] = False

    return memoization

def logicaBot (memoization, qtdMoedas, retira1, retira2):
    if not memoization[qtdMoedas - retira1] and qtdMoedas - retira1 >= 0: return retira1
    elif not memoization[qtdMoedas - retira2] and qtdMoedas - retira2 >= 0: return retira2
    elif qtdMoedas - 1 >= 0: return 1

#      else:
#          if rodada == 1: memoization = moedeiro(qtdMoedas, retira1, retira2)
#          rodada += 1
#          bot = logicaBot(memoization, qtdMoedas, retira1, retira2)
#          qtdMoedas -= bot
#      jogador *= -1

#  print(f"VITORIA JOGADOR {'A' if jogador == -1 else 'B'} EM {rodada} RODADAS")
