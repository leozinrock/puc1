import math

exp = math.log(1000, 10)

print("Logaritmo base 10 de 1000 = {:.2f}".format(exp))

print("Logaritmo base 2 de 32 = {:.2f}".format(math.log(32,2)))

print("Potenciacao e Radiciacao ----")
#exemplo 1
print("Potência: 2^3 * 4^3 = (:.2f)".format((2**3)*(4**3)))

#exemplo 2
print("Potência: 4^3 / 2^3 = {:.2f}".format((4**3)/(2**3)))

#exemplo 3
print("Potência: 2 ^ -5 = {:.5f}".format(2**-5))

#exemplo 4
print("Raiz Quadrada: (5^6) ^ (1/2) = [:.2f)".format((5**6)**(1/2)))

#exemplo 5
print("Raiz Cubica: (4^9) ^ (1/3) = {:.2f}".format((4**9)**(1/3)))

#Exercicios de Logaritmo:
print("Logaritmo ----")

#exemplo 1
print("Logaritmo base 2 de 64 = {:.2f}".format(math.log(64,2)))

#exemplo 2
print("Logaritmo base 2 de 1/128={:.2f}".format(math.log(1/128,2)))

#exemplo 3
print("Logaritmo base 10 de (1000 **(1/2) = [:.2f]".format(math.log((1000 ** (1/2)), 10)))