# faça um programa que abra e reproduza o audio de um arquivo MP3
import pygame

# inicializa o pygame
pygame.init()

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo de música
try:
    pygame.mixer.music.load('desafio019.mp3') # Adicione o caminho do arquivo aqui
    print('Musica carregada com sucesso !')

    # Reproduz a música
    pygame.mixer.music.play()
    print('Tocando musica...')

    # Manter o programa rodando enquanto a musica toca
    while pygame.mixer.music.get_busy():
        continue

    print('Musica terminou sozinha !')

finally:
    pygame.quit()
