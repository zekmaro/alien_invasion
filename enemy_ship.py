import pygame
import random

class EnemyShip:

	def __init__(self, ai_game):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		self.image = pygame.image.load('images/enemy_ship.png')
		size = (70, 70)
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()

		self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
		self.rect.y = 20

		self.move_up = False
		self.move_down = True
		self.move_left = False
		self.move_right = False

		self.can_move = False
	
	def put_enemy_on_screen(self):

		self.screen.blit(self.image, self.rect)