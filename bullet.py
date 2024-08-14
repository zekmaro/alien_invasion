import pygame

class Bullet:

	def __init__(self, ai_game, ship, image_path, direction):

		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		self.image = pygame.image.load(image_path)
		size = (50, 50)
		self.image = pygame.transform.scale(self.image, size)
		self.rect = self.image.get_rect()

		if direction == "up":
			self.rect.x = ship.rect.x + 24
			self.rect.y = ship.rect.y - 20
		elif direction == "down":
			self.rect.x = ship.rect.x + 24
			self.rect.y = ship.rect.y + ship.rect.height
	
		self.direction = direction
	
	def put_bullet_on_screen(self):

		self.screen.blit(self.image, self.rect)

	def update_bullet_position(self, direction):
		"""Move the bullet and check if it's still on the screen."""
		if self.direction == "up":
			self.rect.y -= 10
		elif self.direction == "down":
			self.rect.y += 10

		if self.rect.y < 0 or self.rect.y > self.screen_rect.height:
			return False
		return True
