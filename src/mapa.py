from dataclasses import dataclass
from typing import List, Any


@dataclass
class Aresta:
    no_destino: Any
    peso: int


class No:
    def __init__(self, identificador: str):
        self.id = identificador
        self.arestas: List[Aresta] = []

    @property
    def adjacentes(self):
        return [aresta.no_destino for aresta in self.arestas]

    def add_adjacente(self, destino, peso: int):
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
    def __init__(self):
        self.cidades: List[No] = []

    def add_aresta(self, de: str, para: str, peso: int):
        no_de = self._get_no(de)
        no_para = self._get_no(para)

        no_de.add_adjacente(no_para, peso)
        no_para.add_adjacente(no_de, peso)

    def _get_no(self, id_no) -> No:
        no = No(id_no)

        try:
            index = self.cidades.index(no)
            no = self.cidades[index]
        except ValueError:
            self.cidades.append(no)

        return no


CIDADES = Mapa()

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


for i in CIDADES.cidades:
    print(i)
