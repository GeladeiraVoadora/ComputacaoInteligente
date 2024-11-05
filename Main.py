import random
import funcoes

# Função para geração da população inicial
def geraPopulacao(nItens, nIndividuos):
    return [[int(random.uniform(-100, 100)) for _ in range(nItens)] for _ in range(nIndividuos)]

# Função de avaliação dos indivíduos (funções propostas)
def avaliacao(funcao, populacao):
    return list(map(funcao, populacao))

# Função torneio
def torneio(populacao, funcao):
    lista = []
    listaDeFitness = avaliacao(funcao, populacao)
    melhorFitness = min(listaDeFitness)
    melhorIndividuo = populacao[listaDeFitness.index(melhorFitness)]
    print(f"Melhor Indivíduo: {melhorIndividuo}\nFitness: {melhorFitness}")

    for _ in range(len(populacao)):
        lutador1, lutador2 = random.sample(populacao, 2)
        if funcao(lutador1) < funcao(lutador2):
            lista.append(lutador1)
        else:
            lista.append(lutador2)
    return lista

# Função de seleção (Roleta) para seleção proporcional ao fitness
def roleta(populacao, funcao):
    listaDeFitness = avaliacao(funcao, populacao)
    melhorFitness = min(listaDeFitness)

    probabilidades = [1/x for x in listaDeFitness]
    melhorIndividuo = populacao[listaDeFitness.index(melhorFitness)]
    print(f"Melhor Indivíduo: {melhorIndividuo}\nFitness: {melhorFitness}")

    selecao = random.choices(populacao, weights=probabilidades, k=len(populacao))
    return selecao

# Função de cruzamento (Crossover)
def crossover(selecao):
    novaPopulacao = []
    i = 0
    for _ in range(len(selecao) // 2):
        pai1, pai2 = selecao[i], selecao[i + 1]
        probCruzamento = random.random()

        if probCruzamento > 0.70:
            pontoCorte = len(pai1) // 2
            filho1 = mutacao(pai1[:pontoCorte] + pai2[pontoCorte:])
            filho2 = mutacao(pai2[:pontoCorte] + pai1[pontoCorte:])
        else:
            filho1, filho2 = pai1, pai2

        novaPopulacao.extend([filho1, filho2])
        i += 2
    return novaPopulacao

# Função de Mutação
def mutacao(filho):
    return [int(random.uniform(-100, 100)) if random.random() < 0.01 else gene for gene in filho]

# Função do algoritmo genético
def algoritmoGenetico(funcao, nItens, nIndividuos, nGeracoes):
    populacao = geraPopulacao(nItens, nIndividuos)
    for i in range(nGeracoes):
        print(f"\nGeração nº {i+1}")
        selecao = torneio(populacao, funcao)
        populacao = crossover(selecao)

if __name__ == '__main__':
    algoritmoGenetico(funcoes.sphere, 30, 30, 15000)
