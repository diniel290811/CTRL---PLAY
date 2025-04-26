class Animal: 
    def identificar(self, vertebra, classe, alimentacao):
        raise NotImplementedError("Este método deve ser implementado nas subclasses")
    
class vertebrado(Animal):
    mapa = {
        ("ave", "carnivoro"): "aguia",
        ("ave", "onivoro"): "pomba",
        ("mamifero", "onivoro"): "homem",
        ("mamifero", "herbivoro"): "vaca",
    }

def identificar(self, vertebra, classe, alimentacao):
    return self.mapa.get((classe, alimentacao))

class invertebrado(Animal):
    mapa = {
        ("inseto", "hematofago"): "pulga",
        ("inseto", "herbivoro"): "lagarta",
        ("anelideo", "hematofago"): "sanguessuga",
        ("anelideo", "onivoro"): "minhoca"
    }

def identificar(self, vertebra, classe, alimentacao):
    return self.mapa.get((classe, alimentacao))

vertebra = input()
classe = input()
alimentacao = input()

if vertebras == "vertebrado":
    Animal = vertebrado()
elif vertebras == "invertebrado":
    Animal = invertebrado()

print(animal.identificar(vertebrado, classe, alimentacao))