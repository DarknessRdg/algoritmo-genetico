def _get_cidade(gene):
    """
    Função auxiliar para pegar o No (cidade) do gene.

    :param gene: Gene com a aresta.
    :return: No cidade do gene.
    """
    return gene.alelo.no_destino


class VerificarCancerEstrategy:
    """
    Estratégia para validar 1 cromosomo e verificar se
    o caminho percorrido é válido.
    """

    def tem_cancer(self, comossomo):
        """
        Verifica se o cromossomo é váilido. Para ser válido, deve atender
        a 2 requisitos:

        1 - Não pode haver repetíção de cidades
        2 - Deve ser possível andar pelo mapa seguindo a ordem das arestas
            presente nos genes do cromossomo.

        :param comossomo: Cromossomo a ser validado
        :return: String contendo o motivo do cancer, ou uma string vazia
            se não for encontrado cancer.
        """
        genes_validos = list(filter(bool, comossomo.genes))
        todas_cidades = set(map(_get_cidade, genes_validos))

        if len(genes_validos) != len(todas_cidades):
            return 'Invalido: tem repitação de cidade'

        for index in range(len(genes_validos) - 2):
            aresta = genes_validos[index].alelo
            proxima_aresta = genes_validos[index + 1].alelo

            if proxima_aresta not in aresta.no_destino.arestas:
                return 'Invalido: caminho impossível'

        return ''
