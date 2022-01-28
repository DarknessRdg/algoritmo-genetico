class FitnessStrategy:

    def calcular(self, genes):
        alelos = set([gene.alelo for gene in genes if gene.alelo])

        custo = sum(map(lambda alelo: alelo.peso, alelos))

        return len(alelos), -custo
