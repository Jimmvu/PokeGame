import pygame
import time
import os

pygame.init()


name = os.path.dirname(__file__) + '\Battle.mp3'

pygame.mixer.music.load("Battle.mp3")
pygame.mixer.music.play()

time.sleep(5)


pygame.mixer.music.stop()
