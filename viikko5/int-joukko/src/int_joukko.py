KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        
        self.kapasiteetti = KAPASITEETTI
        self.kasvatuskoko = OLETUSKASVATUS

        if kapasiteetti:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_maara = 0

    def kuuluu_jonoon(self, luku):
        if luku in self.lukujono:
            return True
        return False


    def lisaa_luku(self, luku):

        if not self.kuuluu_jonoon(luku):
            self.lukujono[self.alkioiden_maara] = luku
            self.alkioiden_maara += 1

            if self.alkioiden_maara == len(self.lukujono):
                self.lukujono.append([0]*self.kasvatuskoko)

            return True

        return False

    def poista(self, luku):

        if luku in self.lukujono:
            self.lukujono.remove(luku)
            self.lukujono.append(0)
            self.alkioiden_maara -= 1
            return True
        return False


    def kopioi_taulukko(self, taytettava, kopioitava):
        for i in range(0, len(taytettava)-1):
            kopioitava[i] = taytettava[i]

    def alkioita_taulussa(self):
        return self.alkioiden_maara

    
    def to_int_list(self):
        taulu = [0] * self.alkioiden_maara

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a_taulu, b_taulu):
        yhdiste_taulu = IntJoukko()

        for i in range(0, a_taulu.alkioita_taulussa()):
            yhdiste_taulu.lisaa_luku(a_taulu.lukujono[i])

        for i in range(0, b_taulu.alkioita_taulussa()):
            yhdiste_taulu.lisaa_luku(b_taulu.lukujono[i])

        return yhdiste_taulu

    @staticmethod
    def leikkaus(a_taulu, b_taulu):
        leikkaus_talulu = IntJoukko()
        for i in range(0, a_taulu.alkioita_taulussa()):
            if a_taulu.lukujono[i] in b_taulu.lukujono:
                leikkaus_talulu.lisaa_luku(a_taulu.lukujono[i])
        return leikkaus_talulu

    @staticmethod
    def erotus(a_taulu, b_taulu):
        erotus_taulu = IntJoukko()
        for i in range(0, a_taulu.alkioita_taulussa()):
            erotus_taulu.lisaa_luku(a_taulu.lukujono[i])

        for i in range(0, b_taulu.alkioita_taulussa()):
            erotus_taulu.poista(b_taulu.lukujono[i])
        return erotus_taulu

    def __str__(self):
        
        tuloste = "{"
        for i in range(0, self.alkioiden_maara - 1):
            tuloste += str(self.lukujono[i])
            tuloste += ", "
        if self.alkioiden_maara > 0:
            tuloste += str(self.lukujono[self.alkioiden_maara - 1])
        tuloste += "}"
        return tuloste
