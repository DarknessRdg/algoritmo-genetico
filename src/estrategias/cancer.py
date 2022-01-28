def _get_cidade(gene):
    return gene.alelo.no_destino


def _achar_cidade(cidades, procurada):
    for cidade in cidades:
        if cidade == procurada:
            return cidade


TEM_CANCER = True
NAO_TEM_CANCER = False


class VerificarCancerEstrategy:
    def tem_cancer(self, comossomo):
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
