#Bibliotecas a serem usadas
import os
import cursor
import msvcrt
import WConio2 as WConio2

#Importação de classes
from mapa import Mapa
from pacman import Pacman
from paredesMapa import Paredes
from fantasmas import Fantasmas

def main():
    os.system('cls')
    #Declarando instâncias das classes
    dimensoesMapa = Mapa(largura=23, altura=23) #Definindo um mapa 23x23
    pacman = Pacman("©", 4, 11) #Definindo o simbolo do pacman e sua posição inicial
    fantasma1 = Fantasmas("R", 10 , 9) #Definindo o simbolo do fantasma 1 e sua posição inicial
    fantasma2 = Fantasmas("Y", 10 , 10) #Definindo o simbolo do fantasma 2 e sua posição inicial
    fantasma3 = Fantasmas("B", 10 , 12) #Definindo o simbolo do fantasma 3 e sua posição inicial
    fantasma4 = Fantasmas("O", 10 , 13) #Definindo o simbolo do fantasma 4 e sua posição inicial
    simbolo = ''
    paredes = Paredes(dimensoesMapa.plano)

    paredes.configurarMapa() #Aqui colocamos as paredes do mapa

    while (simbolo != "o"):
        #Posiciona o cursor no começo do terminal
        WConio2.gotoxy(0,0)
        cursor.hide() #Esconde o cursor
        dimensoesMapa.atualizaCaractere(pacman.pacman, pacman.linha, pacman.coluna) #Atualiza o caractere do pacman
        dimensoesMapa.atualizaFantasma1(fantasma1.fantasma, fantasma1.linha, fantasma1.coluna) #Atualiza o caractere do fantasma 1
        dimensoesMapa.atualizaFantasma2(fantasma2.fantasma, fantasma2.linha, fantasma2.coluna) #Atualiza o caractere do fantasma 2
        dimensoesMapa.atualizaFantasma3(fantasma3.fantasma, fantasma3.linha, fantasma3.coluna) #Atualiza o caractere do fantasma 3
        dimensoesMapa.atualizaFantasma4(fantasma4.fantasma, fantasma4.linha, fantasma4.coluna) #Atualiza o caractere do fantasma 4
        dimensoesMapa.imprimir() #Imprime o mapa

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
        
if __name__ == "__main__":
    main()
