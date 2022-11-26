import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuotteet = {
            "maito" : Tuote("Maito", 3),
            "juusto" : Tuote("Juusto", 4)
        }

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.tuotteet["maito"])
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_jälkeen_korin_hinta_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.tuotteet["maito"])
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_tuotteen_jalkeen_korissa_kaksi_tuotetta(self):
        self.kori.lisaa_tuote(self.tuotteet["maito"])
        self.kori.lisaa_tuote(self.tuotteet["juusto"])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
