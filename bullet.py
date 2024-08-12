import pygame

class Bullet:

	def __init__(self, ai_game, ship):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		self.image = pygame.image.load('images/bullet.png')
		size = (50, 50)
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()

		self.rect.x = ship.rect.x + 24
		self.rect.y = ship.rect.y - 20
	
	def put_bullet_on_screen(self):

		self.screen.blit(self.image, self.rect)
