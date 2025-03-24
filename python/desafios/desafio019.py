# faça um programa que abra e reproduza o audio de um arquivo MP3
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo de música
pygame.mixer.music.load('audio-encerramento.mp3') # ← Adicione o caminho do arquivo aqui

# Reproduz a música
pygame.mixer.music.play()

# Para parar a música
print('Pressione Enter para parar...') # Espera o usuário pressionar Enter

# Parar a música
pygame.mixer.music.stop()
