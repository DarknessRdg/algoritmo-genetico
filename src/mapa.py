from dataclasses import dataclass
from typing import List, Any


@dataclass
class Aresta:
    """
    Estrutura de dados para salvar uma aresta de 1 no.
    - no_destino: No que representa a direçaão do destino
    - peso: Int distancia da aresta.
    """
    no_destino: 'No'
    peso: int

    def __hash__(self):
        return hash(self.no_destino)


class No:
    """
    Nó com a lista de arestas possíveis para caminhar no mapa.
    """
    def __init__(self, identificador: str):
        self.id = identificador
        self.arestas: List[Aresta] = []

    @property
    def adjacentes(self):
        """
        Retorna as cidades adjacentes ao no
        """
        return [aresta.no_destino for aresta in self.arestas]

    def add_adjacente(self, destino, peso: int):
        """Adiciona uma cidade adjacente ao nó, com seu peso"""
        self.arestas.append(Aresta(no_destino=destino, peso=peso))

    def __repr__(self):
        aresta = []
        for a in self.arestas:
            aresta.append(f'Aresta(destino={a.no_destino.id}, peso={a.peso})')

        return f'{self.id} -> ' + ', '.join(aresta)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, No) and other.id == self.id


class Mapa:
    """
    Grafo que representa o mapa da cidade
    """
    def __init__(self):
        # lista de nós cidades presentes no mapa
        self.cidades: List[No] = []

    @property
    def tamanho(self):
        return len(self.cidades)

    def add_aresta(self, de: str, para: str, peso: int):
        """Adiciona uma nova aresta bi-direcional no mapa"""
        no_de = self.get_cidade(de)
        no_para = self.get_cidade(para)

        no_de.add_adjacente(no_para, peso)
        no_para.add_adjacente(no_de, peso)

    def get_cidade(self, id_no) -> No:
        no = No(id_no)

        try:
            index = self.cidades.index(no)
            no = self.cidades[index]
        except ValueError:
            self.cidades.append(no)

        return no


CIDADES = Mapa()

# Construção do mapa com as cidades e pesos
CIDADES.add_aresta('A', 'F', 3)
CIDADES.add_aresta('A', 'G', 4)
CIDADES.add_aresta('A', 'E', 6)
CIDADES.add_aresta('A', 'B', 5)
CIDADES.add_aresta('E', 'D', 2)
CIDADES.add_aresta('D', 'I', 5)
CIDADES.add_aresta('D', 'C', 8)
CIDADES.add_aresta('C', 'B', 9)
CIDADES.add_aresta('C', 'H', 9)
CIDADES.add_aresta('H', 'K', 3)
CIDADES.add_aresta('J', 'K', 4)
CIDADES.add_aresta('J', 'B', 7)
