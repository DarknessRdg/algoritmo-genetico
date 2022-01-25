from dataclasses import dataclass
from typing import List

from src.cromossomo import Gene
from src.estrategias.shared import criar_cromossomo, criar_roleta_equilibrada
from src.mapa import Aresta


@dataclass
class Empty:
    def __bool__(self):
        return False


class PopulacaoInicialStrategy:

    def __init__(self, inicio, tamanho_cromossos):
        self.inicio = inicio
        self.tamanho_cromossos = tamanho_cromossos

    def criar(self, tamanho_populacao):
        geracao = 1

        return [
            criar_cromossomo(geracao, *self.criar_genes())
            for _ in range(tamanho_populacao)
        ]

    def criar_genes(self) -> List[Gene]:
        visitados = []

        aresta = Aresta(no_destino=self.inicio, peso=0)

        genes = []
        while (
            aresta.no_destino not in visitados
            and len(genes) < self.tamanho_cromossos
        ):
            genes.append(Gene(alelo=aresta))
            visitados.append(aresta.no_destino)

            vizinhos = aresta.no_destino.arestas

            roleta = criar_roleta_equilibrada(vizinhos)

            for possivel_elemento in roleta.selecionar(len(vizinhos)):
                aresta = possivel_elemento

                if aresta.no_destino not in visitados:
                    break

        while len(genes) < self.tamanho_cromossos:
            genes.append(Gene(alelo=Empty()))

        return genes
