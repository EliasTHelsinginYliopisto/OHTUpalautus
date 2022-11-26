# testikoodi tänne jos tarvetta
from ostos import Ostos
from ostoskori import Ostoskori
from tuote import Tuote

def main():
    kori = Ostoskori()
    maito = Tuote("Maito", 3)
    kori.lisaa_tuote(maito)
    print(kori.ostokset)

if __name__ == "__main__":
    main()
