import random
# CRIANDO A PRIMEIRA POPULAÇÃO
Geracoes = int(input("QUANTA GERAÇÕES VOCÊ QUER GERAR?"))
num_elementos = int(input("QUANTOS ELEMENTOS POR GERACOES?"))

# FUNÇÃO


def calculo_funcao(a, b):
    funcao = ((a**5) - 10*(a**3) + 30*a - b**2 + 21*b)
    return funcao

# GERA OS VALORES ENTRE O INTERVALO DE -2.5 - 2.5


def geraValores():
    num = random.uniform(-2.5, 2.5)
    return num

# funcao de achar o numero mais proximo de um valor


def valorProximo(lst, K):

    return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-K))]

# SELECAO


def selecao(populacao, nElementos):
    melhorFitness = 67.5637720154459
    vetFitness = []
    vetAux = []
    nRanking = random.randint(5, nElementos)

    # seleciona apenas os fitness da populacao
    for i in range(nRanking):
        vetAux.append(populacao[i]['fitness'])

    # pega fitness aleatorio e coloca no vetor vetFitness
    for i in range(nRanking):
        escolhido = random.choice(vetAux)
        vetFitness.append(escolhido)

    # seleciona o fitness com mais aptdião do vetFitness
    selecionado = valorProximo(vetFitness, melhorFitness)

    # procura a posição do numero selecionado
    for i in range(nRanking):
        if(populacao[i]['fitness'] == selecionado):
            pos = i

    return pos

# CRUZAMENTO


def cruzamentoX(pai1, pai2):
    media = (pai1['X'] + pai2['X']/2)
    return media


def cruzamentoY(pai1, pai2):
    media = (pai1['Y'] + pai2['Y']/2)
    return media

 # ELETISMO


def calcElitismo(pop):
    n = len(pop)
    fitness = 67.56377  # melhor valor que a gente pode ter
    pos = 0
    vetFit = []  # vetor que vai armazenar todos os fitness
    for i in range(0, n):
        vetFit.append(float(pop[i]['fitness']))

    selecionado = valorProximo(vetFit, fitness)
    print(selecionado)
    # procura a posição do numero selecionado
    for i in range(n):
        if(pop[i]['fitness'] == selecionado):
            pos = i
            break
    return(pos)

# MUTAÇÃO NÃO UNIFORME


def mutacao(filho):
    if(random.uniform(0, 100) <= 5):
        filho = random.uniform(-2.5, 2.5)
    return filho


##################GERANDO A PRIMEIRA POPULACAO###############
    ##TESTE DA FUNÇÃO CALCULO_FUNCAO##
    # x = 1.126033
    # y = 2.5
    # print("MELHOR FITNESS")
    # print(calculo_funcao(x, y))
    ##VARIAVEIS/VETORES##
POP_INICIAL = []  # Populacao inicial
POPULACAO = []  # POPULACOES SEGUINTES
DADOS = []  # Para a plotagem do gráfico
for i in range(num_elementos):
    cromossomo = {'X': geraValores(), 'Y': geraValores(),
                  'fitness': 0.0}  # gera o X e Y
    cromossomo['fitness'] = calculo_funcao(
        cromossomo['X'], cromossomo['Y'])  # gera o Fitness
    POP_INICIAL.append(cromossomo)
##PRINTA A POPULACAO INICIAL##
print("================POPULAÇAO INICIAL========================")
for i in range(num_elementos):
    print(POP_INICIAL[i])
## ELETISMO ##
posM = calcElitismo(POP_INICIAL)  # Pega o melhhor Fitness da População
# Passa um indivíduo para a próxima população
POPULACAO.append(POP_INICIAL[posM])

j = 0
while(j < num_elementos - 1):
    # SELECAO #
    pos1 = selecao(POP_INICIAL, num_elementos)
    pos2 = selecao(POP_INICIAL, num_elementos)
    # Caso os pais sejam iguais
    while(POP_INICIAL[pos1] == POP_INICIAL[pos2]):
        pos2 = selecao(POP_INICIAL, num_elementos)
    # print(POP_INICIAL[pos1])  # teste pai1
    # print(POP_INICIAL[pos2])  # teste pai2
    ## CRUZAMENTO ##
    if(random.uniform(0, 100) <= 85):
        filhoX = cruzamentoX(POP_INICIAL[pos1], POP_INICIAL[pos2])
        filhoY = cruzamentoY(POP_INICIAL[pos1], POP_INICIAL[pos2])
        filhoX = mutacao(filhoX)
        filhoY = mutacao(filhoY)
        cromossomo = {'X': filhoX, 'Y': filhoY,
                      'fitness': 0.0}  # gera o X e Y
        cromossomo['fitness'] = calculo_funcao(
            cromossomo['X'], cromossomo['Y'])  # gera o Fitness
        POPULACAO.append(cromossomo)
    else:
        taxa = random.uniform(0, 1)
        if(taxa < 0.5):
            POPULACAO.append(POP_INICIAL[pos1])
        elif(taxa > 0.5):
            POPULACAO.append(POP_INICIAL[pos2])

    j += 1

geracao = 2

# OI PEDROOOOO. Então eu fiz a populção inicial e a 'primeira', pq tinha que testar a seleção/mutação
# Ai so precisa deixar recursivo e plotar o gráfico mostrando a evolução dos melhores fitness da gereção
# Não fizemos o algoritmo até convergir, então so temos como critério de parada o num de gerações
