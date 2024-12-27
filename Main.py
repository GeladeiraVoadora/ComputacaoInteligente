import funcoes
from AlgoritmoGenetico import AlgoritmoGenetico
from Pso import Pso

if __name__ == '__main__':
    ag = AlgoritmoGenetico(funcoes.sphere, 30, 30, 1000, 'torneio')
    #ag2 = AlgoritmoGenetico(funcoes.rastrigin, 30, 30, 100, 'torneio')
    #ag3 = AlgoritmoGenetico(funcoes.rosenbrock, 30, 30, 100, 'roleta')
    #ag.executar()
    pso = Pso(funcao=funcoes.sphere, nParticulas=30, nDimensoes=30, nIteracoes=15000)
    pso.executar()
