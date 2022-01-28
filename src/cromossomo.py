from dataclasses import dataclass
from typing import Any


class Cromossomo:
    """
    Classe que serve como estrutura de dados para salvar os dados do cromossomo:
    - geracao
    - genes
    - fitness
    - cancerigeno
    """
    def __init__(self, geracao, *genes, cancerigeno=False):
        self.geracao = geracao
        self.genes = genes

        self.fitness = None
        self.cancerigeno = cancerigeno

    def __str__(self):
        return f'Cromossomo(geracao={self.geracao}, ' \
               f'cancerigeno={self.cancerigeno} ' \
               f'fitness={self.fitness}, genes={self.genes})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.genes)

    def __eq__(self, other):
        return isinstance(other, Cromossomo) and other.genes == self.genes


@dataclass
class Gene:
    """
    Classe para ser estrutura de dados dos genes dos cromossomos, onde o valor
    do genes pode ser qualquer coisa.
    - Alelo: valor do gene.
    """
    alelo: Any

    def __repr__(self):
        alelo = (
            'EMPTY' if not self.alelo else
            f'Aresta(destino={self.alelo.no_destino.id}, peso={self.alelo.peso})'
        )

        return f'Gene(alelo={alelo})'

    def __bool__(self):
        return bool(self.alelo)

    def __hash__(self):
        return hash(self.alelo)

    def __eq__(self, other):
        return isinstance(other, Gene) and other.alelo == self.alelo
