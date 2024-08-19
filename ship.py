import pygame

class Ship:

	def __init__(self, ai_game):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		self.image = pygame.image.load('images/ship_images/star_ship.png')
		size = (100, 100)
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

		self.move_up = False
		self.move_down = False
		self.move_left = False
		self.move_right = False
	
	def put_ship_on_screen(self):

		self.screen.blit(self.image, self.rect)