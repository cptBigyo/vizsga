from datetime import  date


class Szoba:
    ar: int
    szobaszam: int

    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super.__init__(3, szobaszam)
        self.ferohely = 1


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super.__init__(5, szobaszam)
        self.ferohely = 2


class Foglalas:
    datum: date
    szobaszam: int

    def __init__(self, datum: date, szobaszam: int):
        self.datum = datum
        self.szobaszam = szobaszam


class Szalloda:
    szobak: list[Szoba]
    foglalasok: list[Foglalas]
    nev: str

    def __init__(self, nev):
        self.szobak = []
        self.foglalasok = []
        self.nev = nev

    def foglalas(self, datum: date, szobaszam: int):
        if datum < date.today():
            print("Csak jövőbeni dátumra fogadunk foglalásokat")
        if len(list(filter(lambda f: f.datum == datum and f.szobaszam == szobaszam, self.foglalasok))) == 0:
            self.foglalasok.append(Foglalas(datum, szobaszam))
        else:
            print("A szoba nem elérhető a kért dátumon")

    def listazas(self):
        for index, foglalas in enumerate(self.foglalasok):
            print(f"{index} {foglalas.datum} - {foglalas.szobaszam} ")

    def lemondas(self, foglalas: Foglalas):
        try:
            self.foglalasok.remove(foglalas)
        except ValueError:
            print("Nincsen ilyen foglalás")

def str_to_date(string: str):
    return date.fromisoformat(string)

sz = Szalloda("Szálloda")

print(sz.nev)
while True:
    print("Válaszd ki a kívánt műveletet:")
    print("1 Foglalás")
    print("2 Lemondás")
    print("3 Listázás")
    print("4 Kilépés")
    option = 0
    try:
        option = int(input(""))
    except ValueError:
        continue
    print()

    if option == 1:
        print("Szobafoglalás")
        rossz_datum = True
        datum = date(1999, 7,  11)
        while datum < date.today():
            datum_str = input("Dátum: (2023-11-30 formátumban)")
            try:
                datum = str_to_date(datum_str)
            except:
                print("Rossz dátum!")
                continue
        szobaszam = int(input("Szobaszám: "))
        sz.foglalas(datum, szobaszam)
    elif option == 2:
        print("Foglalás lemondása")
        print()
        if len(sz.foglalasok) == 0:
            print("Nincsen foglalás")
            continue
        print("Jelenlegi foglalások:")
        sz.listazas()
        lemondas_index = int(input("Foglalás sorszáma: "))
        sz.lemondas(sz.foglalasok[lemondas_index])
        print("Lemondás sikeres!")
    elif option == 3:
        print("Jelenlegi foglalások:")
        sz.listazas()
    elif option == 4:
        print("Kilépés")
        break
    else:
        continue

