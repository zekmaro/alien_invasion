import pygame

class BackGround:

	def __init__(self, ai_game):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		self.image = pygame.image.load('images/bg_space.png')

		size  = (1200, 900)
		self.image = pygame.transform.scale(self.image, size)
	
		self.rect = self.image.get_rect()

	def put_bg_on_screen(self):

		self.screen.blit(self.image, self.rect)