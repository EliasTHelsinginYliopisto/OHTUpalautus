# testikoodi tänne jos tarvetta
from ostos import Ostos
from ostoskori import Ostoskori
from tuote import Tuote

def main():
    kori = Ostoskori()
    maito = Tuote("Maito", 3)
    juusto = Tuote("Juusto", 4)
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(juusto)
    print(kori.ostokset())
    print(kori.ostokset()[0][0])
    kori.poista_tuote(maito)
    print(kori.ostokset())

if __name__ == "__main__":
    main()
