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
    kori.poista_tuote(juusto)
    print(kori.ostokset())

if __name__ == "__main__":
    main()
