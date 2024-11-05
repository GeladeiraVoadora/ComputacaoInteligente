import random

class AlgoritmoGenetico:
    def __init__(self, funcao, nItens, nIndividuos, nGeracoes, selecao):
        self.funcao = funcao
        self.nItens = nItens
        self.nIndividuos = nIndividuos
        self.nGeracoes = nGeracoes
        self.populacao = self.geraPopulacao()
        if selecao.lower().strip() == 'torneio':
            self.selecao = self.torneio
        else:
            self.selecao = self.roleta

    # Função para geração da população inicial
    def geraPopulacao(self):
        return [[int(random.uniform(-100, 100)) for _ in range(self.nItens)] for _ in range(self.nIndividuos)]

    # Função de avaliação dos indivíduos
    def avaliacao(self):
        return list(map(self.funcao, self.populacao))

    # Função torneio
    def torneio(self):
        lista = []
        listaDeFitness = self.avaliacao()
        melhorFitness = min(listaDeFitness)
        melhorIndividuo = self.populacao[listaDeFitness.index(melhorFitness)]
        print(f"Melhor Indivíduo: {melhorIndividuo}\nFitness: {melhorFitness}")

        for _ in range(len(self.populacao)):
            lutador1, lutador2 = random.sample(self.populacao, 2)
            if self.funcao(lutador1) < self.funcao(lutador2):
                lista.append(lutador1)
            else:
                lista.append(lutador2)
        return lista

    # Função de seleção (Roleta) para seleção proporcional ao fitness
    def roleta(self):
        listaDeFitness = self.avaliacao()
        melhorFitness = min(listaDeFitness)

        probabilidades = [1 / x for x in listaDeFitness]
        melhorIndividuo = self.populacao[listaDeFitness.index(melhorFitness)]
        print(f"Melhor Indivíduo: {melhorIndividuo}\nFitness: {melhorFitness}")

        selecao = random.choices(self.populacao, weights=probabilidades, k=len(self.populacao))
        return selecao

    # Função de cruzamento (Crossover)
    def crossover(self, selecao):
        novaPopulacao = []
        i = 0
        for _ in range(len(selecao) // 2):
            pai1, pai2 = selecao[i], selecao[i + 1]
            probCruzamento = random.random()

            if probCruzamento > 0.7:
                pontoCorte = len(pai1) // 2
                filho1 = self.mutacao(pai1[:pontoCorte] + pai2[pontoCorte:])
                filho2 = self.mutacao(pai2[:pontoCorte] + pai1[pontoCorte:])
            else:
                filho1, filho2 = pai1, pai2

            novaPopulacao.extend([filho1, filho2])
            i += 2
        return novaPopulacao

    # Função de Mutação
    def mutacao(self, filho):
        return [int(random.uniform(-100, 100)) if random.random() < 0.01 else gene for gene in filho]

    # Função para executar o algoritmo genético
    def executar(self):
        for i in range(self.nGeracoes):
            print(f"\nGeração nº {i+1}")
            selecao_atual = self.selecao()
            self.populacao = self.crossover(selecao_atual)