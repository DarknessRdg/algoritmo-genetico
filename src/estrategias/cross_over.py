from typing import List

from src.cromossomo import Cromossomo
from src.estrategias.populacao import Empty
from src.estrategias.shared import (
    criar_cromossomo, criar_roleta_equilibrada,
    completar_genes,
)
from src.mapa import No


def somente_genes_preenchidos(genes):
    return filter(bool, genes)


def get_no(gene):
    if not gene:
        return gene

    return gene.alelo.no_destino


class CrossOverStrategy:
    def cross_over(self, pai: Cromossomo, mae: Cromossomo, geracao):
        return (
            self.cria_descendente(pai, mae, geracao),
            self.cria_descendente(mae, pai, geracao)
        )

    def cria_descendente(self, pai: Cromossomo, mae: Cromossomo, geracao: int):
        mesmas_cidades = self.lugares_iguais(pai, mae)

        roleta = criar_roleta_equilibrada(mesmas_cidades)
        cidade_sorteada = roleta.pop()

        genes = [
            *self.genes_ate_cidade(cidade_sorteada, pai),
            *self.genes_apos_a_cidade(cidade_sorteada, mae)
        ]

        completar_genes(genes, Empty(), len(pai.genes))

        return criar_cromossomo(geracao, *genes)

    def genes_ate_cidade(
        self, cidade: No, pai: Cromossomo
    ) -> List[Cromossomo]:

        genes = []

        for gene in pai.genes:
            genes.append(gene)

            if len(genes) == len(pai.genes):
                break

            if get_no(gene) == cidade:
                break

        return genes

    def genes_apos_a_cidade(
        self, cidade: No, pai: Cromossomo
    ) -> List[Cromossomo]:
        genes = []

        passou_da_cidade = False
        for gene in pai.genes:
            if passou_da_cidade:
                genes.append(gene)

            if cidade == get_no(gene):
                passou_da_cidade = True

            if len(genes) == len(pai.genes):
                break

        return genes

    def lugares_iguais(self, pai, mae):

        cidades_pai = set(map(get_no, somente_genes_preenchidos(pai.genes)))
        cidades_mae = set(map(get_no, somente_genes_preenchidos(mae.genes)))

        return list(cidades_pai.intersection(cidades_mae))
