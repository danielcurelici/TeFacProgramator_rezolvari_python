class Angajat:
    "Clasa care gestioneaza angajatii unei firme"
    
    nr_angajati = 0
    
    def __init__(self, nume, salariu):
        self.nume = nume
        self.salariu = salariu
        Angajat.nr_angajati += 1
        
    def info(self):
        print("Nume: %s\nSalariu: %i" % (self.nume, self.salariu))
        
if __name__ == "__main__":
    ang1 = Angajat("Gigel", 1000)
    ang2 = Angajat("Gigel", 1000)
    ang1.info()
    print(Angajat.__doc__)
    print(Angajat.nr_angajati)