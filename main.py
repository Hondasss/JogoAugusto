#Bibliotecas a serem usadas
import os
import cursor
import msvcrt
import WConio2 as WConio2
import random
import time

#Importação de classes
from mapa import Mapa
from pacman import Pacman
from paredesMapa import Paredes
from fantasmas import Fantasmas
from arquivos import *

def main():
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

        
        
if __name__ == "__main__":
    main()

    
