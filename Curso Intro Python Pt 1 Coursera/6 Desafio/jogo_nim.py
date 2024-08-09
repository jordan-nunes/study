def computador_escolhe_jogada(n, m):
    jogada = 1
    if n <= m:
        jogada = n
        if jogada == 1:
            print("\nO computador tirou uma peça.")
        else:
            print("\nO computador tirou", jogada, "peças.")
        return jogada
    else:    
        while ((n - jogada) % (m + 1) != 0) and jogada <= m:
            jogada += 1
        if jogada == 1:
            print("\nO computador tirou uma peça.")
        else:
            print("\nO computador tirou", jogada, "peças.")
        return jogada


def usuario_escolhe_jogada(n, m):
    jogada_valida = True
    while jogada_valida == True:
        jogada = int(input("\nQuantas peças você vai tirar? "))
        if jogada > n or jogada > m or jogada <= 0:
            print("\nOops! Jogada inválida! Tente de novo.")
        elif jogada == 1:
            print("\nVocê tirou uma peça.")
            return jogada
        else:
            print("\nVoce tirou", jogada, "peças.")
            return jogada

def partida():
    fim_da_partida = False
    numero_valido = False
    while numero_valido == False:
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if n < m:
            print("Você digitou número inválido, tente de novo")
        else:
            numero_valido = True
    vez_do_usuario = True
    if n % (m + 1) == 0:
            print("\nVocê começa!")   
    else:
            print("\nComputador começa!")
            vez_do_usuario = False
    while fim_da_partida == False:
            while n > 0:
                if vez_do_usuario == True:
                    n -= usuario_escolhe_jogada(n, m)
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    else:
                        print("Agora restam", n, "peças no tabuleiro.")
                    vez_do_usuario = False
                else:
                    n -= computador_escolhe_jogada(n, m)
                    if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                    elif n == 0:
                        print("Fim do jogo! O computador ganhou!")
                    else:
                        print("Agora restam", n, "peças no tabuleiro.")
                    vez_do_usuario = True
            fim_da_partida = True

def campeonato():
    i = 1
    while i <= 3:
        print("\n**** Rodada", i, "****\n")
        partida()
        i += 1
    print("\n*** Final do campeonato! ****\n\nPlacar: Você 0 X 3 Computador")

def main():
    tipo_partida = int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    if tipo_partida == 1:
        print("\nVoce escolheu partida isolada!\n")
        partida()
    else:
        print("\nVoce escolheu partida campeonato!\n")
        campeonato()
main()