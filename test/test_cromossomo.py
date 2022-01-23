import unittest

from src.cromossomo import Cromossomo


class TestCrossOver(unittest.TestCase):
    def setUp(self) -> None:
        self.geracao = 21
        self.a = Cromossomo(self.geracao, 2, 3, 4, 5)
        self.b = Cromossomo(self.geracao, 6, 7, 8, 9)

    def test_proxima_geracao(self):
        cross_a, cross_b = self.a.cross_over(self.b)

        assert cross_a.geracao == self.geracao + 1
        assert cross_b.geracao == self.geracao + 1

    def test_genes(self):
        cross_a, cross_b = self.a.cross_over(self.b)

        assert cross_a.genes == (6, 3, 4, 5)
        assert cross_b.genes == (2, 7, 8, 9)

    def test_quantidade_de_pontos(self):
        cross_a, cross_b = self.a.cross_over(self.b, quantidade_pontos=3)

        assert cross_a.genes == (6, 7, 8, 5)
        assert cross_b.genes == (2, 3, 4, 9)
