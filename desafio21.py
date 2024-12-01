import pygame
pygame.init()

# Carrega e toca a música
pygame.mixer.music.load('r.mp3')
pygame.mixer.music.play()

# Loop para manter o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():  # Retorna True enquanto a música está tocando
    pygame.time.Clock().tick(10)  # Aguarda um pouco para não sobrecarregar a CPU

pygame.quit()
