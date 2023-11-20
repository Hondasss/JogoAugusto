#Bibliotecas a serem usadas
import os
import cursor
import msvcrt
import WConio2 as WConio2
import random
import time
import sys

#Importação de classes⥀
from telaInicial import TelaInicial, TelaNovoJogo, TelaHighScores, TelaGameOver
from mapa import Mapa
from pacman import Pacman
from paredesMapa import Paredes
from fantasmas import Fantasmas
from arquivos import *
from pontuacao import Pontuacao

def main():
    telaInicial = TelaInicial()
    opcaoJogador = telaInicial.showTelaInicial("1")

    if opcaoJogador == "1":
        telaNovoJogo = TelaNovoJogo()
        nomeJogador = telaNovoJogo.mostrarNovoJogo()
        iniciarJogo(nomeJogador,"1")
    if opcaoJogador == "2":
        telaNovoJogo = TelaNovoJogo()
        nomeJogador = telaNovoJogo.mostrarNovoJogo()
        iniciarJogo(nomeJogador,"2")

    elif opcaoJogador == "3":
        telaHighScore = TelaHighScores()
        telaHighScore.mostrarHighscore()

    elif opcaoJogador == "4":
        os.system('cls')  # Limpa a tela antes de sair do jogo
        print("Fim do Jogo!")
        sys.exit()


# Função para salvar a pontuação
def salvarPontuacao(nome_jogador, pontuacao):
    with open('ranking.txt', 'a') as arquivo:
        arquivo.write(f"{nome_jogador}: {pontuacao}\n")

# Função para mostrar os high scores
def mostrarHighScore():
    try:
        with open('ranking.txt', 'r') as arquivo:
            pontuacoes = []
            for linha in arquivo:
                nome, pontuacao = linha.strip().split(': ')
                pontuacoes.append((nome, int(pontuacao)))
            
            pontuacoesOrdenadas = sorted(pontuacoes, key=lambda x: x[1], reverse=True)
            
            print("Pontuações mais altas:")
            for idx, (nome, pontuacao) in enumerate(pontuacoesOrdenadas, start=1):
                print(f"{idx}. {nome}: {pontuacao}")
    except FileNotFoundError:
        print("Ainda não há pontuações salvas.")

def iniciarJogo(nomeJogador, opcaoJogador):
    os.system('cls')
    #Declarando instâncias das classes
    dimensoesMapa = Mapa(largura=23, altura=23) #Definindo um mapa 23x23
    pacman = Pacman("\033[33mC\033[m", 4, 11) #Definindo o simbolo do pacman e sua posição inicial
    fantasmas = [
        Fantasmas("\033[0;31mR\033[m", 1, 1),
        Fantasmas("\033[32mG\033[m", 1, 21),
        Fantasmas("\033[94mB\033[m", 21, 1),
        Fantasmas("\033[33mY\033[m", 21, 21)
    ]
    simbolo = ''
    paredes = Paredes(dimensoesMapa.plano)
    pontuacaoTotal = 0 

    if opcaoJogador == "1":
        paredes.configurarMapa() #Aqui colocamos as paredes do mapa
    elif opcaoJogador == "2":
        paredes.configurarMapa2()

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
        pontuacaoAtual = Pontuacao.atualizarPontuacao(pacman, dimensoesMapa.plano)
        pontuacaoTotal += pontuacaoAtual
        print(f"\nPontuação: {pontuacaoTotal}", end='', flush=True)
        

        #Verifica colisão com fantasmas
        for i, fantasma in enumerate(fantasmas):
            if pacman.linha == fantasma.linha and pacman.coluna == fantasma.coluna:
                gameOver(nomeJogador, pontuacaoTotal)
                return

def gameOver(nomeJogador, pontuacaoTotal):
    telaGameOver = TelaGameOver()
    opcaoGameOver = telaGameOver.showGameOver()
    
    if opcaoGameOver == "1":
        salvarPontuacao(nomeJogador, pontuacaoTotal)  # Salvar pontuação ao final da partida
        WConio2.gotoxy(12, 2)
        opcaoHighscore = input("Deseja ver os high scores? (S/N): ")
        while opcaoHighscore.upper() == "S":
            os.system('cls') 
            telaHighScore = TelaHighScores()
            telaHighScore.mostrarHighscore()
            break
        
        main()  # Reiniciar o jogo
        return  # Sai da função gameOver após reiniciar o jogo

    elif opcaoGameOver == "2":
        os.system('cls')
        print("Fim do Jogo!")
        sys.exit()  # Sair do jogo
        return 
        
if __name__ == "__main__":
    while True:
        main()