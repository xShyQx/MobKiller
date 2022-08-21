import pygame

from mobkiller.objects.game import Game

pygame.init()

game = Game()

while(game.isRunning()):
    game.update()
    game.render()

pygame.quit()