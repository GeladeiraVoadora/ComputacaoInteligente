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
        populacao = []
        for _ in range(self.nParticulas):
            posicao = [random.randint(-100, 100) for _ in range(self.nDimensoes)]
            velocidade = [random.uniform(-1, 1) for _ in range(self.nDimensoes)]
            particula = {
                'posicao': posicao,
                'velocidade': velocidade,
                'melhor_posicao': posicao[:],
                'melhor_valor': float('inf')
            }
            populacao.append(particula)
        return populacao

    # Atualização da posição e velocidade das partículas
    def atualizarParticulas(self, melhorPosicaoGlobal):
        for particula in self.populacao:
            nova_velocidade = []
            nova_posicao = []
            for i in range(self.nDimensoes):
                r1, r2 = random.random(), random.random()
                vel_cognitiva = self.c1 * r1 * (particula['melhor_posicao'][i] - particula['posicao'][i])
                vel_social = self.c2 * r2 * (melhorPosicaoGlobal[i] - particula['posicao'][i])
                velocidade_atualizada = self.w * particula['velocidade'][i] + vel_cognitiva + vel_social
                nova_velocidade.append(velocidade_atualizada)

                nova_posicao.append(round(particula['posicao'][i] + velocidade_atualizada))

            particula['velocidade'] = nova_velocidade
            particula['posicao'] = nova_posicao

    # Função para executar o algoritmo PSO
    def executar(self):
        melhorPosicaoGlobal = None
        melhorValorGlobal = float('inf')

        for iteracao in range(self.nIteracoes):
            print(f"\nIteração nº {iteracao+1}")

            for particula in self.populacao:
                valor = self.funcao(particula['posicao'])

                # Atualizar o melhor valor pessoal da partícula
                if valor < particula['melhor_valor']:
                    particula['melhor_valor'] = valor
                    particula['melhor_posicao'] = particula['posicao'][:]

                # Atualizar o melhor valor global
                if valor < melhorValorGlobal:
                    melhorValorGlobal = valor
                    melhorPosicaoGlobal = particula['posicao'][:]

            print(f"Melhor valor global nesta iteração: {melhorValorGlobal}")
            print(f"Melhor posição global nesta iteração: {melhorPosicaoGlobal}")

            # Atualizar posições e velocidades das partículas
            self.atualizarParticulas(melhorPosicaoGlobal)

        print("\nSolução encontrada:")
        print(f"Melhor valor global: {melhorValorGlobal}")
        print(f"Melhor posição global: {melhorPosicaoGlobal}")