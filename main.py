#Bibliotecas a serem usadas
import time
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
        WConio2.gotoxy(0,0)
        #os.system('cls')
        cursor.hide()
        dimensoesMapa.atualizaCaractere(pacman.pacman, pacman.linha, pacman.coluna)
        dimensoesMapa.imprimir()

       # time.sleep(0.1)

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

    
