import pygame
import time
import sys
import os
import random

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGTH = 720

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
buttons = [263, 0, 0, 0, 0, 0]
pygame.display.set_caption("PythonMC Launcher v2026.00")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def getFPS():
    text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
    screen.blit(text, (50, 50))

def load():
    global background, v263
    v263 = pygame.transform.scale(pygame.image.load("assets/Launcher/263.png"), (1280, 720))
    loading = pygame.transform.scale(pygame.image.load("assets/Launcher/loading.png"), (1280, 720))
    pythonlogo = pygame.transform.scale(pygame.image.load("assets/Launcher/pythonlogo.png"), (1280, 720))
    minecraftlogo = pygame.transform.scale(pygame.image.load("assets/Launcher/loading.png"), (1280, 720))
    background = pygame.transform.scale(pygame.image.load("assets/Launcher/background.png"), (1280, 720))
    screen.blit(loading, (0, 0))
    pygame.display.flip()
    time.sleep(1)

def main():
    #White box
    pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 500, WINDOW_HEIGTH // 2 - 250, 1000, 500), border_radius=35)
    #Bar
    pygame.draw.rect(screen, (125, 133, 130), (WINDOW_WIDTH // 2 + 460, WINDOW_HEIGTH // 2 - 225, 30, 450), border_radius=35)
    #Slide bar
    #slidebar = pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH / 2 - 500, WINDOW_HEIGTH / 2 - 250, 1000 , 500), border_radius=35)
    #Newest version box
    version_1 = pygame.draw.rect(screen, (125, 133, 130), (WINDOW_WIDTH // 2 - 475, WINDOW_HEIGTH // 2 - 225, 200 , 225), border_radius=20)
    #New_2 version box
    version_2 = pygame.draw.rect(screen, (125, 133, 130), (WINDOW_WIDTH // 2 - 240, WINDOW_HEIGTH // 2 - 225, 200 , 225), border_radius=20)
    #New_3 version box
    version_3 = pygame.draw.rect(screen, (125, 133, 130), (WINDOW_WIDTH // 2, WINDOW_HEIGTH // 2 - 225, 200 , 225), border_radius=20)
    #New_4 version box
    version_4 = pygame.draw.rect(screen, (125, 133, 130), (WINDOW_WIDTH // 2 + 240, WINDOW_HEIGTH // 2 - 225, 200 , 225), border_radius=20)
    text = font.render("26.3", True, (255, 255, 255))
    screen.blit(text, (WINDOW_WIDTH / 2 - 125, WINDOW_HEIGTH / 2 - 215))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and version_1.collidepoint(event.pos):
            return launchmc(buttons[1])
        if event.button == 1 and version_2.collidepoint(event.pos):
            return launchmc(buttons[2])
        if event.button == 1 and version_3.collidepoint(event.pos):
            return launchmc(buttons[3])
        if event.button == 1 and version_4.collidepoint(event.pos):
            return launchmc(buttons[4])

def launchmc(version):
    length = 0
    delay = random.randint(5, 10)
    for i in range(1000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                while True:
                    break
        screen.blit(v263, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (WINDOW_WIDTH // 2 - 640, WINDOW_HEIGTH // 2 + 335, int(length * 1.28), 25))
        pygame.display.flip()
        time.sleep(delay / 1000)
        length += 1
    os.system(f"python3 -u {os.getcwd()}/mcversions/mc{version}.py")
    pygame.quit()
    sys.exit()

load()

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