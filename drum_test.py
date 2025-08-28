import pygame
import time

# init mixer
pygame.mixer.init()

# load sounds
kick = pygame.mixer.Sound("sounds/kick.wav")
snare = pygame.mixer.Sound("sounds/snare.wav")
hihat = pygame.mixer.Sound("sounds/hihat.wav")

# play them one by one
kick.play()
time.sleep(1)

snare.play()
time.sleep(1)

hihat.play()
time.sleep(1)

print("All sounds tested!")
