from src import estrategias
from src.aleatorio import ElementoRoleta, Roleta
from src.estrategias.mutacao import MutacaoStrategy
from src.mapa import CIDADES

TAMANHO_POPULACAO_INICIAL = 10
TAMANHO_MAXIMO_POPULACAO = 100
TAXA_DE_REPRODUCAO = 1
TAXA_MUTACAO = 50

MAX_GERACOES = 70

CIDADE_INICIAL = CIDADES.get_cidade('A')

POPULACAO_INICIAL_STRATEGY = estrategias.PopulacaoInicialStrategy(
    inicio=CIDADE_INICIAL,
    tamanho_cromossos=CIDADES.tamanho
)

CROSS_OVER_STRATEGY = estrategias.CrossOverStrategy()

CONTROLE_POPULACIONAL = estrategias.ControlePopulacionalStrategy()

MUTACAO = MutacaoStrategy(taxa_mutacao=TAXA_MUTACAO)


def ordenar_populacao(populacao):
    def by_fitness(cromossomo):
        return cromossomo.fitness

    populacao.sort(key=by_fitness, reverse=True)


def criar_roleta(populacao):
    tamanho_populacional = len(populacao)

    elementos = (
        ElementoRoleta(
            elemento=cromossomo,
            probablidade=tamanho_populacional - index
        )
        for (index, cromossomo) in enumerate(populacao)
    )

    return Roleta(*elementos)


def gerar_descentedes(populacao, geracao):
    roleta = criar_roleta(populacao)

    quantidade_reproducao = int((len(populacao) * TAXA_DE_REPRODUCAO) / 2)
    print('total reproducao', quantidade_reproducao)
    descendentes = []
    for _ in range(quantidade_reproducao):
        pai, mae = roleta.selecionar(2)

        filhos = CROSS_OVER_STRATEGY.cross_over(pai, mae, geracao)
        descendentes.extend(filhos)

    descendentes_com_mutacao = map(
        MUTACAO.mutar,
        descendentes
    )

    return list(descendentes_com_mutacao)


def main():
    populacao = POPULACAO_INICIAL_STRATEGY.criar(TAMANHO_POPULACAO_INICIAL)

    historico_populacional = [
        {'geracao': 1, 'populacao': populacao}
    ]

    for geracao in range(2, MAX_GERACOES + 1):
        historico_populacional.append(populacao)

        populacao = CONTROLE_POPULACIONAL.controlar_populacao(
            populacao=populacao,
            geracao=geracao,
            quantidade_maxima=TAMANHO_MAXIMO_POPULACAO
        )

        ordenar_populacao(populacao)

        novos_descendentes = gerar_descentedes(populacao, geracao)

        populacao.extend(novos_descendentes)

    populacao = CONTROLE_POPULACIONAL.remover_todos_cancerigenos(populacao)
    ordenar_populacao(populacao)

    for i in populacao:
        print(i)

    equivalentes = melhores_cromossomos(populacao)

    print('Melhores comossomos (equivalentes por fitness):')
    for cromo in equivalentes:
        print('\n\n')

        print('geracao', cromo.geracao)
        print('quantidade cidade', cromo.fitness[0])
        print('distancia percorrida', abs(cromo.fitness[1]))

        caminho = map(
            lambda it: str(it.alelo.no_destino.id),
            filter(bool, cromo.genes)
        )
        print('Caminho:', ' -> '.join(caminho))


def melhores_cromossomos(populacao):
    fit = populacao[0].fitness

    melhores = []
    for cromossomo in populacao:
        if cromossomo.fitness == fit:
            if cromossomo not in melhores:
                melhores.append(cromossomo)
        else:
            break

    return melhores


if __name__ == '__main__':
    main()
