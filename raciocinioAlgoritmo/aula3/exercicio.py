ladoA = int
ladoB = int
ladoC = int

ladoA = int(imput("digite o ladoA = "))
ladoB = int(imput("digite o ladoB = "))
ladoC = int(imput(" digite o ladoC = "))

if (ladoA < (ladoB + ladoC)) and (ladoB < (ladoA + ladoC)) and (ladoC <
(ladoA + ladoB)):
    if ((ladoA == ladoB) and (ladoB == ladoC)):
        print("Triangulo Equilatero!")
    elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
        print("Triangulo Isosceles!")
    else:
        print("Triangulo Escaleno!")
else:
    print("Lados não formam um triangulo!")

