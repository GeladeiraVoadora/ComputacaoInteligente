import funcoes
from AlgoritmoGenetico import AlgoritmoGenetico
if __name__ == '__main__':
    ag = AlgoritmoGenetico(funcoes.sphere, 30, 30, 15000, 'roleta')
    ag2 = AlgoritmoGenetico(funcoes.rastrigin, 30, 30, 15000, 'torneio')
    ag3 = AlgoritmoGenetico(funcoes.rosenbrock, 30, 30, 15000, 'roleta')
    ag2.executar()
