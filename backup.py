## MAIN ##
#Bibliotecas a serem usadas
import os
import cursor
import msvcrt
import WConio2 as WConio2

#Importação de classes
from mapa import Mapa
from pacman import Pacman

def main():
    os.system('cls')
    #Declarando instâncias das classes
    dimensoesMapa = Mapa(largura=25, altura=15) #Definindo um mapa 25x25
    pacman = Pacman("a", 5, 15)
    simbolo = ''

    while (simbolo != "o"):
        #Posiciona o cursor no começo do terminal
        WConio2.gotoxy(0,0)
        cursor.hide() #Esconde o cursor
        dimensoesMapa.atualizaCaractere(pacman.pacman, pacman.linha, pacman.coluna) #Atualiza o caractere do pacman
        dimensoesMapa.imprimir() #Imprime o mapa

        #Captação e movimentação usando a biblioteca msvcrt
        if msvcrt.kbhit():
            tecla = msvcrt.getch().decode()
            if tecla == 'a' or tecla == 'A':
                pacman.moverEsquerda()
            elif tecla == 'd' or tecla == 'D':
                pacman.moverDireita()
            elif tecla == 'w' or tecla == 'W':
                pacman.moverCima()
            elif tecla == 's' or tecla == 'S':
                pacman.moverBaixo()
        
if __name__ == "__main__":
    main()

##MAPA##
class Mapa:
    #Definição da função INIT, que armazenará variáveis de controle da largura e altura
    def __init__(self, largura, altura):
        #Iniciando altura e largura
        self.largura = largura 
        self.altura = altura

        #Iniciando uma matriz que representará toda a área do jogo, sendo essa ALTURA x LARGURA
        self.plano = [[' ' for coluna in range(largura)] for linha in range(altura)] #O ponto representa o valor inicial de cada célula na matriz
        self.bordas() #O método é chamado aqui para criar as bordas desde o inicio do jogo, garantindo solidez e evitando erros
        self.linhaPacmanAnterior = 0  
        self.colunaPacmanAnterior = 0  

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

    def limparPosicao(self, linha,  coluna):
        # Limpa a posição anterior do Pacman
        self.plano[linha][coluna] = ' '

    def imprimir(self): #Impressão
        for linha in self.plano:
            print(''.join(linha))

##PACMAN##
class Pacman:
    def __init__(self, pacman, linhaInicial, colunaInicial):
        self.pacman = pacman
        self.linha = linhaInicial
        self.coluna = colunaInicial

    def moverEsquerda(self):
        self.coluna -= 1

    def moverDireita(self):
        self.coluna += 1

    def moverCima(self):
        self.linha -= 1

    def moverBaixo(self):
        self.linha += 1
