from src.aleatorio import Roleta, ElementoRoleta
from src.cromossomo import Gene
from src.estrategias.shared import criar_roleta_equilibrada, criar_cromossomo


class MutacaoStrategy:
    def __init__(self, taxa_mutacao):
        self.deve_mutar = 'DEVE MUTAR'
        self.nao_mutar = 'NÃO DEVE MUTAR'

        self.roleta = Roleta(
            ElementoRoleta(elemento=self.deve_mutar, probablidade=taxa_mutacao),
            ElementoRoleta(elemento=self.nao_mutar, probablidade=100),
            remover_apos_selecionar=False
        )

    def mutar(self, cromosso):
        acao = self.roleta.pop()
        if acao == self.deve_mutar:
            genes_mutados = self._genes_mutados(cromosso)
            return criar_cromossomo(
                cromosso.geracao,
                *genes_mutados
            )
        return cromosso

    def _genes_mutados(self, cromossomo):
        genes = list(filter(bool, cromossomo.genes))

        penultimo = genes[-2].alelo.no_destino
        ultimo = genes[-1]

        roleta = criar_roleta_equilibrada(penultimo.arestas)

        nova_aresta = roleta.pop()
        while nova_aresta == ultimo:
            nova_aresta = roleta.pop()

        genes[-1] = Gene(alelo=nova_aresta)
        return genes
