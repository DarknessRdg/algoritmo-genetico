class FitnessStrategy:

    def calcular(self, genes):
        alelos = [gene.alelo for gene in genes if gene.alelo]

        custo = sum(map(lambda alelo: alelo.peso, alelos))

        return len(alelos), -custo
