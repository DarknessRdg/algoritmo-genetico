from typing import List


def fitness_strategy(genes):
    return 1


class Cromossomo:
    def __init__(self, geracao, *genes):
        self.geracao = geracao
        self.genes = genes

        self.fitness = fitness_strategy(self.genes)

    def cross_over(self,
                   outro: 'Cromossomo',
                   quantidade_pontos: int = 1) -> List['Cromossomo']:

        proxima_geracao = self.geracao + 1

        return [
            Cromossomo(
                proxima_geracao,
                *outro.primeiros_genes(quantidade_pontos),
                *self.ultimos_genes(quantidade_pontos)
            ),

            Cromossomo(
                proxima_geracao,
                *self.primeiros_genes(quantidade_pontos),
                *outro.ultimos_genes(quantidade_pontos)
            ),

        ]

    def primeiros_genes(self, n):
        return self.genes[:n]

    def ultimos_genes(self, n):
        return self.genes[n:]

    def __str__(self):
        return f'Cromossomo(geracao={self.geracao}, ' \
               f'fitness={self.fitness}, genes={self.genes})'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    a = Cromossomo(1, 2, 3, 4, 5)
    b = Cromossomo(1, 6, 7, 8, 9)
