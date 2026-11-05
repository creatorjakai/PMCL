import pygame
import time
import sys
import math
import os

pygame.init()

WINDOW_HEIGTH = 1280
WINDOW_WIDTH = 720

screen = pygame.display.set_mode((WINDOW_HEIGTH, WINDOW_WIDTH))
chosenversion = "26.3"
pygame.display.set_caption("PythonMC Launcher v2026.00")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def getFPS():
    text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
    screen.blit(text, (50, 50))

def loading():
    global background
    background = pygame.transform.scale(pygame.image.load("assets/Launcher/background.png"), (1280, 720))

def main():
    pygame.draw.rect(screen, (255, 255, 255), (WINDOW_HEIGTH / 2 - 250, WINDOW_WIDTH / 2 - 250, 500 , 500), border_radius=35)
    pygame.draw.rect(screen, (43, 151, 251), (WINDOW_HEIGTH / 2 - 200, WINDOW_WIDTH / 2 + 180, 400 , 50), border_radius=35)
    pygame.draw.rect(screen, (125, 133, 130), (WINDOW_HEIGTH / 2 - 200, WINDOW_WIDTH / 2 - 180, 400 , 50), border_radius=20)
    text = font.render(f"Launch Minecraft {chosenversion}", True, (255, 255, 255))
    screen.blit(text, (540 - (18 + 2 * len(chosenversion)), 555))

loading()

#Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    getFPS()

    main()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()