from src.aleatorio import Roleta, ElementoRoleta
from src.cromossomo import Gene
from src.estrategias.shared import criar_roleta_equilibrada, criar_cromossomo


class MutacaoStrategy:
    """
    Estratégia para realizar mutação.

    - deve_mutar: String com o valor indicando que o
        elemento sorteado deve ser mutado
    - nao_mutar: String com o valor indicando que o
        elemento sorteado não ser mutado
    - roleta: estratégia para sortear se deve ou não mutar
    - taxa_mutacao: [0-100] Int com o a porcentagem de 0 a 100
        do genes que devem ser mutados
    """

    def __init__(self, taxa_mutacao):
        self.deve_mutar = 'DEVE MUTAR'
        self.nao_mutar = 'NÃO DEVE MUTAR'

        # role com as probabilidades corretas de mutação para cada elemento,
        # onde não mutar é sempre 100% - taxa mutação
        self.roleta = Roleta(
            ElementoRoleta(
                elemento=self.deve_mutar,
                probablidade=taxa_mutacao
            ),
            ElementoRoleta(
                elemento=self.nao_mutar,
                probablidade=100 - taxa_mutacao
            ),
            remover_apos_selecionar=False
        )

    def mutar(self, cromosso):
        """
        Função principal para mutar um cromossomo.
        Se no sortei ele for mutado, é criado um novo cromossomo com os genes
        mutadaos. Se não for sorteado, é retornado o próprio cromossomo.

        :param cromosso: Cromossomo para ser mutado
        :return: Cromosso mutado ou o próprio cromossomo se não for sorteado
        """

        # sorteia se deve mutar ou não
        acao = self.roleta.pop()

        if acao == self.deve_mutar:
            genes_mutados = self._genes_mutados(cromosso)
            return criar_cromossomo(
                cromosso.geracao,
                *genes_mutados
            )

        # não deve mutar o cromossomo
        return cromosso

    def _genes_mutados(self, cromossomo):
        """
        Seleciona o ultimo gene do cromosso e altera para um novo, seguindo
        a regra de selecionar 1 aresta disponível do penúltimo cromossomo
        para que ele ainda se mantenha sem cancer.

        :param cromossomo: Cromosso para ser mutado
        :return: List[Gene] lista com os genes mutados
        """
        genes = list(filter(bool, cromossomo.genes))

        # penultima cidade para seelcionar 1 nova aresta para substituir o
        # uiltmmo gene
        penultimo = genes[-2].alelo.no_destino
        ultimo = genes[-1]

        # cria uma role com a mesma probabilidade de sorteio
        # para cada aresta
        roleta = criar_roleta_equilibrada(penultimo.arestas)

        # seleciona aresta diferente do ultimo
        nova_aresta = roleta.pop()
        while nova_aresta == ultimo:
            nova_aresta = roleta.pop()

        genes[-1] = Gene(alelo=nova_aresta)
        return genes
