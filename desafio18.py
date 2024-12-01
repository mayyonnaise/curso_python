import math
angulo=float(input("Digite o ângulo que você deseja: "))
rad = math.radians(angulo)
seno= math.sin(rad)
cosseno= math.cos(rad)
tangente= math.tan(rad)
print("O ângulo de "+str(angulo)+" tem o SENO de {:.2f}".format(seno))
print("O ângulo de "+str(angulo)+" tem o COSSENO de {:.2f}".format(cosseno))
print("O ângulo de "+str(angulo)+"tem o TANGENTE de {:.2f}".format(tangente))