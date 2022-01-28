class FitnessStrategy:
    """
    Estratégia para criar o fitness de 1 cromossomo.
    """

    def calcular(self, genes):
        """
        Calula o fitness de 1 cromossomo para serem ordenados. O fitness
        atende a dois critérios, de modo que os melhores cromossomos tenham:

        1. Maior número de cidades visitadas
        2. Menor distância percorrida

        :param genes: Tupe[Genes] genes do cromossomo
        :return: Tupe[Int, Int] - quantidade de cidades, menor distância
            respectivamente
        """
        alelos = set([gene.alelo for gene in genes if gene.alelo])

        custo = sum(map(lambda alelo: alelo.peso, alelos))

        # custo negativo para que o melhor cromossomo seja o de menor custo.
        return len(alelos), -custo

