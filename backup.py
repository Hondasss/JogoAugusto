#Bibliotecas a serem usadas
import time
import os
import cursor
import WConio2 as WConio2

#Importação de classes
from mapa import Mapa
from pacman import Pacman

def main():
    os.system('cls')
    cursor.hide()
    
    dimensoesMapa = Mapa(largura=25, altura=15)
    pacman = Pacman("a", 5, 15)
    simbolo = ''

    while (simbolo != "o"):
        os.system('cls')

        if pacman.linha > 10:
            pacman.linha = 0

        if dimensoesMapa.contador % 600 == 0:
            pacman.linha += 1

        dimensoesMapa.atualizaCaractere(pacman.pacman, pacman.linha, pacman.coluna)
        dimensoesMapa.imprimir()

        time.sleep(0.1)

        if WConio2.kbhit():
            (tecla, simbolo) = WConio2.getch()
            if simbolo == 'a' or simbolo == 'A':
                pacman.moverEsquerda()
            elif simbolo == 'd' or simbolo == 'D':
                pacman.moverDireita()
                
    print("Fim do Jogo!")