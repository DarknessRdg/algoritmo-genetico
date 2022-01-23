import random
from dataclasses import dataclass
from typing import Any, List


@dataclass
class ElementoRoleta:
    id: Any
    probablidade: int  # probablidade de escolha do elemento
    # variando entre 0 - 100


class Roleta:
    remover_apos_selecionar: bool
    elementos: List[ElementoRoleta]

    def __init__(self, *elementos: ElementoRoleta,
                 remover_apos_selecionar=True):
        self.remover_apos_selecionar = remover_apos_selecionar
        self.elementos_distribuidos = []
        self.elementos = list(elementos)

    def selecionar(self, quantidade):
        for _ in range(quantidade):
            opcoes = random.choices(
                population=self.elementos,
                weights=self.get_probabilidades(),
                k=1
            )
            aleatorio = opcoes[0]

            self.remover_elemento(aleatorio)

            yield aleatorio

    def get_probabilidades(self):
        return [
            elemento.probablidade
            for elemento in self.elementos
        ]

    def remover_elemento(self, elemento):
        if self.remover_apos_selecionar:
            self.elementos.remove(elemento)
