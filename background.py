import pygame

class BackGround:

	def __init__(self, ai_game, height, width, image_path):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		self.image = pygame.image.load(image_path)

		size  = (height, width)
		self.image = pygame.transform.scale(self.image, size)
	
		self.rect = self.image.get_rect()

	def put_bg_on_screen(self):

		self.screen.blit(self.image, self.rect)