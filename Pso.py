import random

class Pso:
    def __init__(self, funcao, nParticulas, nDimensoes, nIteracoes, w=0.5, c1=1.5, c2=1.5):
        self.funcao = funcao
        self.nParticulas = nParticulas
        self.nDimensoes = nDimensoes
        self.nIteracoes = nIteracoes
        self.w = w  #Inércia da velocidade
        self.c1 = c1  #Coeficiente de aprendizado individual
        self.c2 = c2  #Coeficiente de aprendizado global
        self.populacao = self.geraPopulacao()

    # Função para geração da população inicial
    def geraPopulacao(self):
        return [[int(random.uniform(-100, 100)) for _ in range(self.nItens)] for _ in range(self.nParticulas)]