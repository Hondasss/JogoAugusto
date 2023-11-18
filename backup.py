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

        # Verifica colisão com fantasmas
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

class Fantasmas:
    def __init__(self, fantasma, linhaInicial, colunaInicial):
        self.fantasma = fantasma
        self.linha = linhaInicial
        self.coluna = colunaInicial
        
    def moverEsquerda(self, mapa):
        if mapa[self.linha][self.coluna - 1] != '#':
            self.coluna -= 1

    def moverDireita(self, mapa):
        if mapa[self.linha][self.coluna + 1] != '#':
            self.coluna += 1

    def moverCima(self, mapa):
        if mapa[self.linha - 1][self.coluna] != '#':
            self.linha -= 1

    def moverBaixo(self, mapa):
        if mapa[self.linha + 1][self.coluna] != '#':
            self.linha += 1

class Mapa:
    #Definição da função INIT, que armazenará variáveis de controle da largura e altura
    def __init__(self, largura, altura):
        #Iniciando altura e largura
        self.largura = largura 
        self.altura = altura

        #Iniciando uma matriz que representará toda a área do jogo, sendo essa ALTURA x LARGURA
        self.plano = [['.' for coluna in range(largura)] for linha in range(altura)] #O ponto representa o valor inicial de cada célula na matriz
        self.bordas() #O método é chamado aqui para criar as bordas desde o inicio do jogo, garantindo solidez e evitando erros
        self.linhaPacmanAnterior = 0  
        self.colunaPacmanAnterior = 0  
        self.FantasmaAnterior = {
            "LinhaFantasma1": 0,
            "ColunaFantasma1": 0,
            "LinhaFantasma2": 0,
            "ColunaFantasma2": 0,
            "LinhaFantasma3": 0,
            "ColunaFantasma3": 0,
            "LinhaFantasma4": 0,
            "ColunaFantasma4": 0
        }
            

    def bordas(self):
        #Método que adiciona as bordas delimitadas por #
        for i in range(self.largura):
            self.plano[0][i] = '#' #Tampa
            self.plano[self.altura - 1][i] = '#' #Fundo

        for i in range(self.altura):
            self.plano[i][0] = '#' #Lateral esquerda
            self.plano[i][self.largura - 1] = '#' #Lateral direita 

    def atualizaCaractere(self, caractere, linha, coluna):
        # Limpa a posição anterior do Pacman
        self.limparPosicao(self.linhaPacmanAnterior, self.colunaPacmanAnterior)

        # Proteção do script para verificação da linha e coluna dentro do limite máximo
        if 0 <= linha < self.altura and 0 <= coluna < self.largura:
            self.linhaPacmanAnterior, self.colunaPacmanAnterior = linha, coluna
            self.plano[linha][coluna] = caractere

    def atualizaFantasma(self, fantasmas):
        for i in range(len(fantasmas)):
            f = fantasmas[i]
            # Verifica se a próxima posição está vazia ou é o símbolo do Pac-Man antes de mover o fantasma
            if self.plano[f.linha][f.coluna] == ' ' or self.plano[f.linha][f.coluna] == 'C':
                self.plano[self.FantasmaAnterior[f"LinhaFantasma{i+1}"]][self.FantasmaAnterior[f"ColunaFantasma{i+1}"]] = ' '  # Limpa a posição anterior do fantasma
            else:
                self.plano[self.FantasmaAnterior[f"LinhaFantasma{i+1}"]][self.FantasmaAnterior[f"ColunaFantasma{i+1}"]] = '.'  # Volta o caractere original
            self.plano[f.linha][f.coluna] = f.fantasma
            self.FantasmaAnterior[f"LinhaFantasma{i+1}"] = f.linha
            self.FantasmaAnterior[f"ColunaFantasma{i+1}"] = f.coluna


            
    def limparPosicao(self, linha,  coluna):
        # Limpa a posição anterior do Pacman para dar impressao de movimento
        self.plano[linha][coluna] = ' '

    def imprimir(self): #Impressão
        for linha in self.plano:
            for caractere in linha:
                print(caractere, end=' ')
            print()

class Pacman:
    def __init__(self, pacman, linhaInicial, colunaInicial):
        self.pacman = pacman
        self.linha = linhaInicial
        self.coluna = colunaInicial

    def moverEsquerda(self, mapa):
        if mapa[self.linha][self.coluna - 1] != '#':
            self.coluna -= 1

    def moverDireita(self, mapa):
        if mapa[self.linha][self.coluna + 1] != '#':
            self.coluna += 1

    def moverCima(self, mapa):
        if mapa[self.linha - 1][self.coluna] != '#':
            self.linha -= 1

    def moverBaixo(self, mapa):
        if mapa[self.linha + 1][self.coluna] != '#':
            self.linha += 1

class Paredes:
    def __init__(self, mapa):
        self.mapa = mapa

    #Função que adiciona as paredes verticais no mapa
    def addLinhaVertical(self, coluna, linhaInicial, altura):
        for i in range(linhaInicial, linhaInicial + altura):
            self.mapa[i][coluna] = '#'
    

    def addLinhaHorizontal(self, linha, colunaInicial, largura):
        for i in range(colunaInicial, colunaInicial + largura):
            self.mapa[linha][i] = '#'

    def configurarMapa(paredes):
     #Linhas verticais do mapa
        paredes.addLinhaVertical(coluna=11, linhaInicial=1, altura=3)
        paredes.addLinhaVertical(coluna=6, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=16, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=11, linhaInicial=6, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=18, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=8, linhaInicial=10, altura=2)
        paredes.addLinhaVertical(coluna=14, linhaInicial=10, altura=2)
        paredes.addLinhaVertical(coluna=11, linhaInicial=15, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=18, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=6, linhaInicial=18, altura=2)
        paredes.addLinhaVertical(coluna=16, linhaInicial=18, altura=2)
        paredes.addLinhaVertical(coluna=20, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=2, linhaInicial=7, altura=6)

    #Linhas horizontais do mapa
        paredes.addLinhaHorizontal(linha=2, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=3, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=2, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=3, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=2, colunaInicial=13, largura=4)    
        paredes.addLinhaHorizontal(linha=3, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=2, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=3, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=5, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=5, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=5, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=14, colunaInicial=1, largura=4)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=14, colunaInicial=19, largura=4)
        paredes.addLinhaHorizontal(linha=9, colunaInicial=8, largura=3)
        paredes.addLinhaHorizontal(linha=9, colunaInicial=12, largura=3)
        paredes.addLinhaHorizontal(linha=12, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=14, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=1, largura=2)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=20, largura=2)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=20, colunaInicial=2, largura=8)
        paredes.addLinhaHorizontal(linha=20, colunaInicial=13, largura=8)











