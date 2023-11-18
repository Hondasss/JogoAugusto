#Bibliotecas a serem usadas
import os
import cursor
import msvcrt
import WConio2 as WConio2
import random
import time
import sys

#Importação de classes
from telaInicial import TelaInicial, TelaNovoJogo, TelaHighScores, TelaGameOver
from mapa import Mapa
from pacman import Pacman
from paredesMapa import Paredes
from fantasmas import Fantasmas
from arquivos import *
from pontuacao import Pontuacao

def main():
    tela_inicial = TelaInicial()
    opcao_jogador = tela_inicial.mostrar_tela_inicial("1")

    if opcao_jogador == "1":
        tela_novo_jogo = TelaNovoJogo()
        nome_jogador = tela_novo_jogo.mostrar_tela_novo_jogo()
        iniciarJogo()

    elif opcao_jogador == "2":
        tela_high_scores = TelaHighScores()
        tela_high_scores.mostrar_tela_high_scores()

    os.system('cls')  # Limpa a tela antes de sair do jogo
    print("Fim do Jogo!")

def iniciarJogo():
    os.system('cls')
    #Declarando instâncias das classes
    dimensoesMapa = Mapa(largura=23, altura=23) #Definindo um mapa 23x23
    pacman = Pacman("C", 4, 11) #Definindo o simbolo do pacman e sua posição inicial
    fantasmas = [
        Fantasmas("R", 1, 1),
        Fantasmas("G", 1, 21),
        Fantasmas("B", 21, 1),
        Fantasmas("Y", 21, 21)
    ]
    simbolo = ''
    paredes = Paredes(dimensoesMapa.plano)
    pontuacaoTotal = 0 

    paredes.configurarMapa() #Aqui colocamos as paredes do mapa

    while (simbolo != "o"):
        #Posiciona o cursor no começo do terminal
        WConio2.gotoxy(0,0)
        cursor.hide() #Esconde o cursor
        dimensoesMapa.atualizaCaractere(pacman.pacman, pacman.linha, pacman.coluna) #Atualiza o caractere do pacman
        dimensoesMapa.atualizaFantasma(fantasmas)
        dimensoesMapa.imprimir() #Imprime o mapa
        
        time.sleep(0.1)
        
        #Captação e movimentação usando a biblioteca msvcrt
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode()
            if tecla == 'a' or tecla == 'A':
                pacman.moverEsquerda(dimensoesMapa.plano)
            elif tecla == 'd' or tecla == 'D':
                pacman.moverDireita(dimensoesMapa.plano)
            elif tecla == 'w' or tecla == 'W':
                pacman.moverCima(dimensoesMapa.plano)
            elif tecla == 's' or tecla == 'S':
                pacman.moverBaixo(dimensoesMapa.plano)
        
    
        #gerado um numero aleatorio entre 1 e 4
        #1 cima, 2 direita, 3 baixo, 4 esquerdo
        for i in range(len(fantasmas)):
            dir = random.randint(1,4)
            if dir == 1:
                fantasmas[i].moverCima(dimensoesMapa.plano)
            elif dir == 2:
                fantasmas[i].moverDireita(dimensoesMapa.plano)
            elif dir == 3:
                fantasmas[i].moverBaixo(dimensoesMapa.plano)
            else:
                fantasmas[i].moverEsquerda(dimensoesMapa.plano)

        # Dentro do loop principal do jogo onde o Pac-Man se move:
        pontuacaoAtual = Pontuacao.atualizar_pontuacao(pacman, dimensoesMapa.plano)
        pontuacaoTotal += pontuacaoAtual
        print(f"\nPontuação: {pontuacaoTotal}", end='', flush=True)

        #Verifica colisão com fantasmas
        for i, fantasma in enumerate(fantasmas):
            if pacman.linha == fantasma.linha and pacman.coluna == fantasma.coluna:
                game_over()
                return

def game_over():
    os.system('cls')  # Limpa a tela
    tela_game_over = TelaGameOver()
    opcao_game_over = tela_game_over.mostrar_tela_game_over()

    while True:  # Loop até que uma ação válida seja escolhida
        if opcao_game_over == "1":
            main()  # Reiniciar o jogo
            break  # Sai do loop depois de reiniciar o jogo
        elif opcao_game_over == "2":
            os.system('cls')
            sys.exit()  # Sair do jogo
            break              
        
if __name__ == "__main__":
    main()

    
