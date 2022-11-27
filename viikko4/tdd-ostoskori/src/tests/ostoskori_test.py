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

    #5.1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    #5.2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    #5.3
    def test_yhden_tuotteen_jälkeen_korin_hinta_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.assertEqual(self.kori.hinta(), 3)
    
    #5.4
    def test_kahden_tuotteen_jalkeen_korissa_kaksi_tuotetta(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Juusto"])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    #5.5
    def test_kahden_eri_tuotteen_jalkeen_hinta_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Juusto"])
        self.assertEqual(self.kori.hinta(), 7)

    #5.6
    def test_kahden_saman_tuotteen_jalkeen_korissa_kaksi_tuotetta(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    #5.7
    def test_kahden_saman_tuotteen_jalkeen_hinta_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.assertEqual(self.kori.hinta(), 6)
    
    #5.8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    #5.9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos[0], "Maito")
        self.assertEqual(ostos[1], 1)
    
    #5.10
    def test_kahden_eri_tuotteen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Juusto"])
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
    
    #5.11
    def test_kahden_saman_tuotteen_jalkeen_korissa_yksi_olio(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    #5.12
    def test_kahden_saman_tuotteen_jalkeen_nimi_ja_maara_oikein(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos[0], "Maito")
        self.assertEqual(ostos[1], 2)
    
    #5.13
    def test_jos_kaksi_samaa_tuotetta_ja_poistetaan_yksi_jaa_yksi(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.poista_tuote(self.tuotteet["Maito"])
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos[0], "Maito")
        self.assertEqual(ostos[1], 1)
    
    #5.14
    def test_jos_viimeinen_tuote_poistetaan_kori_on_tyhja(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.poista_tuote(self.tuotteet["Maito"])
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)

    #5.15
    def test_tyhjenna_tyhjentaa_ostoskorin(self):
        self.kori.lisaa_tuote(self.tuotteet["Maito"])
        self.kori.lisaa_tuote(self.tuotteet["Juusto"])
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)