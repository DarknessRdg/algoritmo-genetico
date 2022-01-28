from src.cromossomo import Cromossomo, Gene
from src.aleatorio import Roleta, ElementoRoleta
from .cancer import VerificarCancerEstrategy
from .fitness import FitnessStrategy


def criar_cromossomo(*args, **kwargs) -> Cromossomo:
    """
    Cria um cromosso e já atribui o valor fitness utilizando
    o strategy de fitness para o cálculo.
    """
    cromossomo = Cromossomo(*args, **kwargs)
    cromossomo.fitness = FitnessStrategy().calcular(cromossomo.genes)
    cromossomo.cancerigeno = VerificarCancerEstrategy().tem_cancer(cromossomo)

    return cromossomo


def criar_roleta_equilibrada(conjunto) -> Roleta:
    """
    Cria uma roleta com os pesos iguais para todos o elementos, de modo que
    todos terão a mesma probabilidade de ser sorteado.
    """
    elemetos_roleta = (
        ElementoRoleta(elemento=elemento, probablidade=1)
        for elemento in conjunto
    )

    return Roleta(*elemetos_roleta)


def completar_genes(genes, alelo, quantidade):
    while len(genes) < quantidade:
        genes.append(Gene(alelo=alelo))
