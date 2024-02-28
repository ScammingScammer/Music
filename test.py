import pygame
import time

def check_keyboard_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print("Paused")
            elif event.key == pygame.K_b:
                print("Previous song")
            elif event.key == pygame.K_n:
                print("Next song")

if __name__ == "__main__":
    pygame.init()

    while True:
        check_keyboard_input()
        time.sleep(0.1)