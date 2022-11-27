from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        lukumaara = 0
        for ostos in self.ostoskori:
            lukumaara += ostos.lukumaara()
        return lukumaara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        for ostos in self.ostoskori:
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        tuote = Ostos(lisattava)
        self.ostoskori.append(tuote)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoskori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                if ostos.lukumaara() == 1:
                    self.ostoskori.remove(ostos)
                else:
                    ostos.muuta_lukumaaraa(-1)


    def tyhjenna(self):
        self.ostoskori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        lista = []
        for ostos in self.ostoskori:
            lista.append((ostos.tuotteen_nimi(), ostos.lukumaara()))
        return lista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
