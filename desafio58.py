import random
from time import sleep

palpite = 1
pc = random.randint(0,5)
adv = int(input('1)Adivinhe o numero que estou pensando de 0 a 5: '))

sleep(1)
print("Processando...")
sleep(1)

while adv != pc:
  adv = int(input(f"{palpite + 1})Adivinhe outro numero: \n"))
  palpite += 1    
print("\n")  
print(f"Acertou o numero {pc}!\nPrecisou de {palpite} palpite(s)")