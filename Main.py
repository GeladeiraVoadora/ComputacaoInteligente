import funcoes
from AlgoritmoGenetico import AlgoritmoGenetico
if __name__ == '__main__':
    ag = AlgoritmoGenetico(funcoes.sphere, 30, 30, 15000, 'roleta')
    ag.executar()
