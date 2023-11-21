import WConio2 as WConio2

#Classe criada para controle da pontuação e exibição no canto inferior esquewrdo do mapa
class Pontuacao:
    def print_pontuacao(pontuacao, dimensoesMapa):
        #Define a posição para exibir a pontuação
        linha_pontuacao = len(dimensoesMapa.plano) - 1
        coluna_pontuacao = len(dimensoesMapa.plano[0]) - 10  # Posição para exibir a pontuação

        #Atualiza a área designada para a pontuação
        dimensoesMapa.plano[linha_pontuacao][coluna_pontuacao:] = list(f'Pontos: {pontuacao:04d}')
        #Imprime o mapa atualizado
        for linha in dimensoesMapa.plano:
            print(' '.join(linha))

        #Posiciona o cursor no início do jogo
        WConio2.gotoxy(0, 0)

    def atualizarPontuacao(pacman, mapa):
        if 0 <= pacman.linha < len(mapa) and 0 <= pacman.coluna < len(mapa[0]):
            if mapa[pacman.linha][pacman.coluna] == '.':
                mapa[pacman.linha][pacman.coluna] = ' '  #Remove o ponto do mapa
                return 1  #Incrementa a pontuação em 1 pontos
        return 0  #Retorna 0 se não houver ponto na posição do Pac-Man
