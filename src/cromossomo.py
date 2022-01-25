from dataclasses import dataclass
from typing import Any


class Cromossomo:
    def __init__(self, geracao, *genes):
        self.geracao = geracao
        self.genes = genes

        self.fitness = None

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

    def __repr__(self):
        alelo = 'EMPTY' if not self.alelo else f'Aresta(destino={self.alelo.no_destino.id}, peso={self.alelo.peso})'

        return f'Gene(alelo={alelo})'

    def __bool__(self):
        return bool(self.alelo)
