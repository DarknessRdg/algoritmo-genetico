from src.cromossomo import Cromossomo
from src.estrategias.populacao import Empty
from src.estrategias.shared import (
    criar_cromossomo, criar_roleta_equilibrada,
    completar_genes,
)
from src.mapa import No


def somente_genes_preenchidos(genes):
    """
    Função auxiliar para descartar os genes `Empty` utilizados
    apenas para preencher os genes para serem do mesmo tamanho.

    :param genes: List[Gene]
    :return: List[Gene]
    """
    return list(filter(bool, genes))


def get_no(gene):
    """
    Função auxiliar para pegar o No (cidade) do gene.

    :param gene: Gene com a aresta.
    :return: No cidade do gene.
    """
    if not gene:
        return gene

    return gene.alelo.no_destino


class CrossOverStrategy:
    """
    Estratégia para realizar cross-over entre dois cromossomos
    """

    def cross_over(self, pai: Cromossomo, mae: Cromossomo, geracao):
        """
        Método principal para realizar cross-over entre dois cromossos.
        Sempre são criados 2 descentes com diferença na ordem dos genes:

        1 - genes pai + genes mae
        2 - genes mae + genes pai

        :param pai: Cromomssomo coms os genes do pai
        :param mae: Cromossomo com os genes da mãe
        :param geracao: Número da geração que os novos cromossomos pertencem
        :return: (Cromossomo, Cromosso)
        """

        return (
            self.cria_descendente(pai, mae, geracao),
            self.cria_descendente(mae, pai, geracao)
        )

    def cria_descendente(self, pai: Cromossomo, mae: Cromossomo, geracao: int):
        """
        Cria 1 descendente com os genes do pai + mae.
        Os genes são compostos dos seguintes passos:
        1 - Encontrar um conjunto de genes iguais (cidades por onde ambos os
            genes passaram);
        2 - Selecionar aleatoriamente 1 das cidades em comum;
        3 - Criar novos genes:
            3.1 - Os primeiros genes do pai até a cidade selecionado, ou seja,
                o percurso do pai até a cidade.
            3.2 - Os genes da mãe à frente dos genes do selecionado, ou seja,
                o percurso da mão após a cidade.

        :param pai: Cromossomo no qual o descendente herdará os primeiros genes
        :param mae: Cromossomo no qual o descendente herdará os últimos genes
        :param geracao: Número da geração que o novo cromossomo pertence
        :return: Cromossomo
        """
        mesmas_cidades = self.lugares_iguais(pai, mae)

        roleta = criar_roleta_equilibrada(mesmas_cidades)
        cidade_sorteada = roleta.pop()

        genes = [
            *self.genes_ate_cidade(cidade_sorteada, pai),
            *self.genes_apos_a_cidade(cidade_sorteada, mae)
        ]

        # completa os genes com valor `Empty` para que
        # todos os cromosso tenham o mesmo tamanho
        completar_genes(genes, Empty(), len(pai.genes))

        return criar_cromossomo(geracao, *genes)

    def genes_ate_cidade(self, cidade: No, pai: Cromossomo):
        """
        Seleciona os genes do início até a cidade desejada.

        :param cidade: No da cidade de destino
        :param pai: Cromo com os genes com as arestas percorridas
        :return: List[Gene] lista com os genes do cromossomo até a cidade.
        """

        genes = []

        for gene in pai.genes:
            # todos os cromossomos devem ter o mesmo tamanho
            if len(genes) == len(pai.genes):
                break

            genes.append(gene)

            if get_no(gene) == cidade:
                break

        return genes

    def genes_apos_a_cidade(self, cidade: No, pai: Cromossomo):
        """
        Seleciona os genes após a cidade desejada até o final do percurso
        do cromossomo.

        :param cidade: No da cidade onde deve começar a selecionar novo percurso
        :param pai: Cromossomo com os genes com as arestas percorridas
        :return: List[Gene] list com os genes finais do cromossomo.
        """
        genes = []

        passou_da_cidade = False
        for gene in pai.genes:
            if passou_da_cidade:
                genes.append(gene)

            if cidade == get_no(gene):
                passou_da_cidade = True

            # todos os genes devem ter o mesmo tamanho
            if len(genes) == len(pai.genes):
                break

        return genes

    def lugares_iguais(self, pai: Cromossomo, mae: Cromossomo):
        """
        Seleciona as cidades no qual cambos os cromossomos passaram.

        :param pai: Cromossomo
        :param mae: Cromossomo
        :return: List[No] lista com os nós das cidades em comum.
        """
        cidades_pai = set(map(get_no, somente_genes_preenchidos(pai.genes)))
        cidades_mae = set(map(get_no, somente_genes_preenchidos(mae.genes)))

        return list(cidades_pai.intersection(cidades_mae))
