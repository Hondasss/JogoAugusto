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
from pontuacao import Pontuacao

def main():
    telaInicial = TelaInicial()
    opcaoJogador = telaInicial.showTelaInicial("1")

    #Entrada do usuario para escolher a opção seguinte

    if opcaoJogador == "1": 
        telaNovoJogo = TelaNovoJogo()
        nomeJogador = telaNovoJogo.mostrarNovoJogo()
        iniciarJogo(nomeJogador,"1") #Inicia o jogo com parametros do nome do jogador e um numero, o qual vai definir a contrução da fase posteriormente (FACIL)

    if opcaoJogador == "2":
        telaNovoJogo = TelaNovoJogo()
        nomeJogador = telaNovoJogo.mostrarNovoJogo()
        iniciarJogo(nomeJogador,"2") #Inicia o jogo com parametros do nome do jogador e um numero, o qual vai definir a contrução da fase posteriormente (DIFICIL)

    elif opcaoJogador == "3":
        telaHighScore = TelaHighScores() #Instancia da tela dos highscores é criada (cria um objeto pra aplicar métodos e atributos definidos na classe)
        telaHighScore.mostrarHighscore() #Função que vai chamar a tela do highscore

    elif opcaoJogador == "4":
        os.system('cls')  #Limpa a tela antes de sair do jogo
        print("Fim do Jogo!")
        sys.exit() #Saí do jogo


#Função para salvar a pontuação
def salvarPontuacao(nomeJogador, pontuacao): #Define uma função para salvar com esses argumentos do nome e pontuação
    with open('ranking.txt', 'a') as arquivo: #With fecha o arquivo automaticamente no final das alterações. 
        arquivo.write(f"{nomeJogador}: {pontuacao}\n") #Formatação do salvamento do arquivo

#Função para mostrar os high scores
def mostrarHighScore():
    try: #Método try except pra pegar os erros
        with open('ranking.txt', 'r') as arquivo:
            pontuacoes = [] 
            for linha in arquivo: 
                nome, pontuacao = linha.strip().split(': ') #Strip limpa a linha dos espaços em brando e o split divide em duas listas, do nome e da pontuação
                pontuacoes.append((nome, int(pontuacao))) #Armazenando essas informações em uma TUPLA, na qual é formatada para receber o nome e posteriormente a pontuação em inteiro

            pontuacoesOrdenadas = sorted(pontuacoes, key=lambda x: x[1], reverse=True) #Maneira do chat gpt de ordenar a pontuação da tupla em ordem descrescente

            print("Pontuações mais altas:")
            for indice, (nome, pontuacao) in enumerate(pontuacoesOrdenadas, start=1): #Aqui basicamente é atribuido um índice começando em 1 para cada elemento para mostrar uma espécie de ranking
                print(f"{indice}. {nome}: {pontuacao}") #Formatação da maneira pela qual deve ser impressa o highscore
    except FileNotFoundError:
        print("Ainda não há pontuações salvas.") #Caso o arquivo nao tenha nenhum registro

def iniciarJogo(nomeJogador, opcaoJogador):
    os.system('cls')
    #Declarando instâncias das classes
    dimensoesMapa = Mapa(largura=23, altura=23) #Definindo um mapa 23x23
    pacman = Pacman("\033[33mC\033[m", 4, 11) #Definindo o simbolo do pacman e sua posição inicial
    fantasmas = [
        Fantasmas("\033[0;31mR\033[m", 1, 1), #Códigos das cores
        Fantasmas("\033[32mG\033[m", 1, 21),
        Fantasmas("\033[94mB\033[m", 21, 1),
        Fantasmas("\033[33mY\033[m", 21, 21)
    ]
    simbolo = ''
    paredes = Paredes(dimensoesMapa.plano)
    pontuacaoTotal = 0

    if opcaoJogador == "1":
        paredes.configurarMapa() #Aqui colocamos as paredes do mapa fácil
    elif opcaoJogador == "2":
        paredes.configurarMapa2() #Aqui colocamos as paredes do mapa difícil

    while (simbolo != "o"): #Loop principal do jogo  
        WConio2.gotoxy(0,0)#Posiciona o cursor no começo do terminal
        cursor.hide() #Esconde o cursor
        dimensoesMapa.atualizaCaractere(pacman.pacman, pacman.linha, pacman.coluna) #Atualiza o caractere do pacman
        dimensoesMapa.atualizaFantasma(fantasmas) #Atualiza os fantasmas
        dimensoesMapa.imprimir() #Imprime o mapa

        time.sleep(0.1) #Controla a velocidade do jogo

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

        #Gerado um numero aleatorio entre 1 e 4 para a movimentação do fantasma
        #1 cima, 2 direita, 3 baixo, 4 esquerdo
        for i in range(len(fantasmas)):
            fantasmas[i].mover(dimensoesMapa.plano)

        #Atualização constante da pontuação para ser exibida
        pontuacaoAtual = Pontuacao.atualizarPontuacao(pacman, dimensoesMapa.plano)
        pontuacaoTotal += pontuacaoAtual
        print(f"\nPontuação: {pontuacaoTotal}", end='', flush=True)


        #Verifica colisão com fantasmas
        for i, fantasma in enumerate(fantasmas):
            if pacman.linha == fantasma.linha and pacman.coluna == fantasma.coluna: #Método usado: equivalencia dos pontos X e Y
                gameOver(nomeJogador, pontuacaoTotal)
                return

def gameOver(nomeJogador, pontuacaoTotal): #Definição da função de fim de jogo
    telaGameOver = TelaGameOver()
    opcaoGameOver = telaGameOver.showGameOver()

    #Salva o score no arquivo e retorna a tela principal do jogo
    if opcaoGameOver == "1":
        salvarPontuacao(nomeJogador, pontuacaoTotal)  # Salvar pontuação ao final da partida
        WConio2.gotoxy(12, 2)
        opcaoHighscore = input("Deseja ver os high scores? (S/N): ")
        while opcaoHighscore.upper() == "S":
            os.system('cls')
            telaHighScore = TelaHighScores()
            telaHighScore.mostrarHighscore()
            break

        main()  #Reiniciar o jogo
        return  #Sai da função gameOver após reiniciar o jogo

    #Não salva o score e sai do jogo
    elif opcaoGameOver == "2": 
        os.system('cls')
        print("Fim do Jogo!")
        sys.exit()  # Sair do jogo
        return

if __name__ == "__main__":
    while True:
        main()