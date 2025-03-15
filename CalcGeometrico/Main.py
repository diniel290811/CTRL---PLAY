import Geometria as g

def menu():
    print("Calculadora Geométrica")
    print("1 - Área do Círculo")
    print("2 - Perimetro do Círculo")
    print("3 - Área do Retângulo")
    print("4 - Perimetro do Retângulo")
    print("5 - Área do Triângulo ")
    print("6 - Perimetro do Triângulo")
    print("7 - Área do Cilindro")
    print("8 - Perimetro do Cilindro")
    print("0 - SAIR")

while True:
    menu()
    opcao = int(input("Escolha sua opção: "))

    if opcao == 1:
        raio = float(input("Raio: "))
        print(f"Área: {g.areaCirculo(raio)}")

    elif opcao == 2:
        raio = float(input("Raio: "))
        print(f"Perimetro: {g.perimetroCirculo(raio)}")
    
    elif opcao == 3:
        base = float(input("base: "))
        altura = float(input("altura: "))
        print(f"Área: {g.areaRetangulo(base, altura)}")

    elif opcao == 4:
        base = float(input("base: "))
        altura = float(input("altura: "))
        print(f"Perimetro: {g.perimetroRetangulo(base, altura)}")

    elif opcao == 5:
        base = float(input("base: "))
        altura = float(input("altura: "))
        print(f"Área: {g.areaTriangulo(base, altura)}")

    elif opcao == 6:
        lado1 = float(input("lado1: "))
        lado2 = float(input("lado2: "))
        lado3 = float(input("lado3: "))
        print(f"Perimetro: {g.perimetroTriangulo(lado1, lado2, lado3)}")

    elif opcao == 7:
        base = float(input("base: "))
        altura = float(input("altura: "))
        areaLateral = float(input("areaLateral"))
        print(f"Área: {g.areaCilindro(base, altura, areaLateral)}")

    elif opcao == 8:
        lado1 = float(input("lado1: "))
        lado2 = float(input("lado2: "))
        lado3 = float(input("lado3: "))
        print(f"Perimetro: {g.perimetroCilindro(lado1, lado2, lado3)}")

    elif opcao == 0:
        print("Saindo")
        break