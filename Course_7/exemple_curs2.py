class Parinte:
    atribut = 10
    def __init__(self):
        print("Parinte")
        
    def metoda(self):
        print("Metoda parinte")
        
    def modificaAtribut(self, val):
        Parinte.atribut = val
        
class Copil(Parinte):
    def __init__(self):
        print("Copil")
        
    def metoda(self):
        print("Metoda Copil")
        
    def metoda2(self):
        super().metoda()
        
if __name__ == "__main__":
    c = Copil()
    c.metoda()
    c.metoda2()
    c.modificaAtribut(99)
    print(Parinte.atribut)