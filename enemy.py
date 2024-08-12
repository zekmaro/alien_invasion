import pygame
import random

class Enemy:

	def __init__(self, ai_game):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		self.image = pygame.image.load('images/enemy1.png')
		size = (50, 50)
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()

		self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
		self.rect.y = 0
	
	def put_enemy_on_screen(self):

		self.screen.blit(self.image, self.rect)
