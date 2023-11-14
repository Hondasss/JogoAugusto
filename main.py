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
    #Declarando instâncias das classes
    dimensoesMapa = Mapa(largura=25, altura=15) #Definindo um mapa 25x25
    pacman = Pacman("a", 5, 15)
    simbolo = ''

    while (simbolo != "o"): #Impressão do mapa em um loop WHILE, com saída somente caso a tecla O seja inserida
        WConio2.gotoxy(0,0) #Posiciona o cursor no começo da tela, não sendo necessário apagar a impressão anterior do mapa
        cursor.hide() #Esconde o cursor
        dimensoesMapa.atualizaCaractere(pacman.pacman, pacman.linha, pacman.coluna)
        dimensoesMapa.imprimir() #Chama a função de impressão

        if WConio2.kbhit(): #Pega interação do usuário
            (tecla, simbolo) = WConio2.getch()
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

    
