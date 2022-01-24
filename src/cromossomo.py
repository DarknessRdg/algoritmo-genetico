from dataclasses import dataclass
from typing import List, Any

from src import settings


class Cromossomo:
    def __init__(self, geracao, *genes):
        self.geracao = geracao
        self.genes = genes

        self.fitness = settings.FITNESS_STRATEGY.calcular(self.genes)

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


@dataclass
class Gene:
    alelo: Any
