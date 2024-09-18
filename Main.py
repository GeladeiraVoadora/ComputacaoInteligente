import random

import funcoes

#A atividade consiste em criar indivíduos com 30 genes, e selecionar os melhores indivíduos.
#Para que sejam os melhores, eles deverão alcançar o menor valor ao serem avaliados pela sphere.
# Os cromossomos serão valores reais(-100 a 100), e o indivídio um vetor de 30 elementos.

# fazer uma função para geração da população inicial
def geraPopulacao(nItens, nIndividuos):
    listaIndividuos = [[random.randrange(-100,100) for _ in range(nItens)] for _ in range(nIndividuos)]

    return listaIndividuos

# Função de avaliação dos indivíduos (funções propostas)
def avaliacao(funcao, populacao):
    resultados = list(map(funcao,populacao))

    return resultados

# Função torneio
def torneio(populacao, funcao):
    lista = []
    listaDeFitness = avaliacao(funcao, populacao)
    melhorFitness = min(listaDeFitness)
    melhorIndividuo = populacao[listaDeFitness.index(melhorFitness)]
    print(f"Melhor Indivíduo: {melhorIndividuo}\nFitness: {melhorFitness}")
    for i in range(len(populacao)):
        lutador1 = populacao[random.randint(0, len(populacao)-1)]
        lutador2 = populacao[random.randint(0, len(populacao)-1)]

        if lutador2 == lutador1:
            lutador2 = populacao[random.randint(0, len(populacao)-1)]

        if funcao(lutador1) < funcao(lutador2):
            lista.append(lutador1)
        else:
            lista.append(lutador2)

    return lista

# Função de seleção (Roleta) função fitnes.
def roleta (avaliacao, populacao):
    numeroIndividuos = len(populacao)
    fitnessTotal = sum(avaliacao)
    fitness = min(avaliacao)

    print(f"Fitness Total: {fitnessTotal}")
    print(f"Fitness: {fitness}")

    probabilidades = [fitnessTotal/x for x in avaliacao]
    print(probabilidades)

    melhorIndividuo = populacao[probabilidades.index(max(probabilidades))]

    print(f"Melhor Indivíduo: {melhorIndividuo}")
    selecao = random.choices(populacao, weights=probabilidades, k=numeroIndividuos)

    return selecao

# Função de cruzamento (Crossover)
def crossover(selecao):
    i = 0
    novaPopulacao = []
    for _ in range(len(selecao)//2):
        pai1 = selecao[i]
        pai2 = selecao[i+1]
        probCruzamento = random.random()

        if probCruzamento > 0.1:
            posicao1 = len(pai1)//2
            posicao2 = len(pai2)//2

            #primeira metade
            primeiraMetadePai1 = pai1[:posicao1]
            primeiraMetadePai2 = pai2[:posicao2]
            #segunda metade
            segundaMetadePai1 = pai1[posicao1:]
            segundaMetadePai2 = pai2[posicao2:]

            filho1 = mutacao((primeiraMetadePai1 + segundaMetadePai2))
            filho2 = mutacao((primeiraMetadePai2 + segundaMetadePai1))

            pai1 = filho1
            pai2 = filho2

        i =+2
        pais = [pai1, pai2]
        novaPopulacao = novaPopulacao + pais

    return novaPopulacao

# Função de Mutação
def mutacao(filho):
    cromossomo = []
    for gene in filho:
        probMutacao = random.random()
        geneAtual = gene
        if probMutacao <= 0.01:
            geneMutante = random.randrange(-100,100)
            geneAtual = geneMutante

        cromossomo = cromossomo + [geneAtual]

    return cromossomo

def algoritimoGenetico(funcao, nItens, nIndividuos, nGeracoes):
    populacaoInicial = geraPopulacao(nItens,nIndividuos)
    populacao = populacaoInicial
    for i in range(nGeracoes):
        print(f"\nGeração nº{i+1}")
        #resultados = avaliacao(funcao,populacao)
        selecao = torneio(populacao, funcao)
        cruzamento = crossover(selecao)
        populacao = cruzamento

if __name__ == '__main__':
    algoritimoGenetico(funcoes.sphere, 30,30,15000)