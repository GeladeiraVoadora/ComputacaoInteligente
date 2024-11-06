import funcoes
from AlgoritmoGenetico import AlgoritmoGenetico
from Pso import Pso

if __name__ == '__main__':
    #ag = AlgoritmoGenetico(funcoes.sphere, 30, 30, 15000, 'roleta')
    #ag2 = AlgoritmoGenetico(funcoes.rastrigin, 30, 30, 15000, 'torneio')
    #ag3 = AlgoritmoGenetico(funcoes.rosenbrock, 30, 30, 15000, 'roleta')
    #ag2.executar()
    pso = Pso(funcao=funcoes.sphere, nParticulas=30, nDimensoes=30, nIteracoes=15000)
    pso.executar()
