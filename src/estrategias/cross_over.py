class CrossOverStrategy:
    def cross_over(self, cromossomo_a, cromossomo_b):
        quantidade_pontos = 1

        proxima_geracao = cromossomo_a.geracao + 1

        return (
            self.cria_descendente(cromossomo_a, cromossomo_b),
            self.cria_descendente(cromossomo_b, cromossomo_a)
        )

    def cria_descendente(self, pai, mae):
        from src.cromossomo import Cromossomo

        mesmas_casas = self.lugares_iguais(pai, mae)

    def lugares_iguais(self, pai, mae):
        uniao = []
        for (gene_pai, gene_mae) in zip(pai.genes, mae.genes):
            if gene_pai == gene_mae:
                uniao.append(gene_pai)
        return uniao
