from dataclasses import dataclass
from typing import List

from src.cromossomo import Gene
from src.estrategias.shared import criar_cromossomo, criar_roleta_equilibrada
from src.mapa import Aresta


@dataclass
class Empty:
    """
    Classe vazia utilizada na criação dos Genes para indicar que o gene
    está vazio e está presente apenas para completar os espaços necessários
    para o tamanho dos genes.
    """

    def __bool__(self):
        return False


class PopulacaoInicialStrategy:
    """
    Estratégia para criar a população inicial

    inicio: No - cidade ponto de partida
    tamanho_cromossomos: Int - tamnaho padrão dos cromossomos gerados.
    """

    def __init__(self, inicio, tamanho_cromossos):
        self.inicio = inicio
        self.tamanho_cromossos = tamanho_cromossos

    def criar(self, tamanho_populacao: int):
        """
        Cria uma lista de cromossos que será a população inicial.

        :param tamanho_populacao: Int quantidade de cromossomos presente
            na população inicial.
        :return: List[Cromossomo]
        """
        geracao = 1

        return [
            criar_cromossomo(geracao, *self.criar_genes())
            for _ in range(tamanho_populacao)
        ]

    def criar_genes(self) -> List[Gene]:
        """
        Cria uma lista de genes
        """
        visitados = []

        aresta = Aresta(no_destino=self.inicio, peso=0)

        genes = []

        # enquanto ainda houver cidade não visitada
        # e o tamanho do cromossomo não atingiu o limite
        while (
            aresta.no_destino not in visitados
            and len(genes) < self.tamanho_cromossos
        ):
            # cria novo gene
            genes.append(Gene(alelo=aresta))

            # maraca a cidade como visitada
            cidade = aresta.no_destino
            visitados.append(cidade)

            # pega as arestas vizinhas da cidade visitada
            vizinhos = cidade.arestas

            # cria um role de probabilidade igual de sorteio
            # para qualquer uma das arestas vizinhas
            roleta = criar_roleta_equilibrada(vizinhos)

            # for auxiliar para selecionar sempre uma cidade não visitada
            # e caso a cidade esteja visitada, continuar selecionando outras
            # até encontrar uma não visitada, ou terminar o loop se todas
            # estiverem visitadas
            for possivel_elemento in roleta.selecionar(len(vizinhos)):
                aresta = possivel_elemento

                if aresta.no_destino not in visitados:
                    break

        # completar as posições restantes dos genes com genes `Empty`
        while len(genes) < self.tamanho_cromossos:
            genes.append(Gene(alelo=Empty()))

        return genes


class ControlePopulacionalStrategy:
    # quantidade de gerações 1 cromossomo com cancer pode
    # permacer na população
    geracoes_de_vida_cancer = 2

    def controlar_populacao(self, populacao, quantidade_maxima, geracao):
        populacao = self.remover_cancerigenos(populacao, geracao)
        return self.controle_quantidade_populacao(populacao, quantidade_maxima)

    def controle_quantidade_populacao(self, populacao, quantidade_maxima):
        return populacao[:quantidade_maxima]

    def remover_cancerigenos(self, populacao, geracao):
        return [
            cromossomo for cromossomo in populacao
            if not (
                cromossomo.cancerigeno
                and geracao - self.geracoes_de_vida_cancer == cromossomo.geracao
            )
        ]

    def remover_todos_cancerigenos(self, populacao):
        return [
            cromossomo for cromossomo in populacao
            if not cromossomo.cancerigeno
        ]
