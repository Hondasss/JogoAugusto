# Pega os dados de PontuacaoJogadores.txt, os manipula e os ordena.
def ordenar_pontuacoes():
    try:
        # Com o arquivo PontuacaoJogadores.txt aberto pega os dados e armazena na variavel linhas
        with open('PontuacaoJogadores.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        # Criar um dicionário para armazenar nomes e pontuações
        pontuacoes_dict = {}
        
        '''Para cada linha, remove espaços em branco extras no início e no final 
        com strip() e, em seguida, divide a linha em duas partes (nome e pontuação) usando split()'''
        for linha in linhas:
            nome, pontuacao = linha.strip().split()
            # Adiciona no dicionário 
            pontuacoes_dict[nome] = int(pontuacao)
        

        # Ordenar o dicionário pelo valor (pontuação)
        # reverse=True: Indica que a ordenação deve ser realizada em ordem decrescente.
        pontuacoesOrdenadas = sorted(pontuacoes_dict.items(), key=lambda item: item[1], reverse=True)

        return pontuacoesOrdenadas

    except FileNotFoundError:
        return []  # Retorna uma lista vazia se o arquivo não for encontrados
    
    except Exception as e:
        return f"Erro ao ordenar pontuações: {str(e)}"



# Função que grava o nome do jogador em PontuacaoJogadores.txt
def gravaNomeJogador(nome):
    with open('PontuacaoJogadores.txt', 'a') as arquivo:
        arquivo.write(nome)
        arquivo.write('\t')

# Função que grava a pontuação do jogador em PontuacaoJogadores.txt
def gravaPontuacao(pontuacao):
    with open('PontuacaoJogadores.txt', 'a') as arquivo:        
        arquivo.write(pontuacao)
        arquivo.write("\n")
