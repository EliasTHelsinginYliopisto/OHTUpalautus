import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.tuotteet = {
            "Maito" : Tuote("Maito", 3),
            "Juusto" : Tuote("Juusto", 4)
        }

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_jälkeen_korin_hinta_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_tuotteen_jalkeen_korissa_kaksi_tuotetta(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Juusto"])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_jalkeen_korissa_kaksi_tuotetta(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)