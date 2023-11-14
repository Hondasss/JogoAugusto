#Bibliotecas a serem usadas
import time
import os
#Importação de classes
from mapa import Mapa

def main():
    dimensoesMapa = Mapa(largura=25, altura=25) #Definindo um mapa 25x25

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console
        for linha in dimensoesMapa.plano:
            print(' '.join(linha))
        
if __name__ == "__main__":
    main()

    
