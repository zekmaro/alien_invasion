import pygame

class Heart:

	def __init__(self, ai_game, offset):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		self.image = pygame.image.load('images/heart.png')

		size  = (50, 50)
		self.image = pygame.transform.scale(self.image, size)
	
		self.rect = self.image.get_rect()
		self.rect.x = offset
		self.rect.y = self.screen_rect.bottom - 50

	def put_heart_on_screen(self):

		self.screen.blit(self.image, self.rect)