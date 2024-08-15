import pygame
import random
from bullet import Bullet

class EnemyShip:

	def __init__(self, ai_game):

		self.ai_game = ai_game

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

		self.bullet_list = []

		self.last_shot_time = pygame.time.get_ticks()
		self.shoot_delay = random.randint(1000, 2000)

	def put_enemy_on_screen(self):

		self.screen.blit(self.image, self.rect)
	
	def shoot(self):
		current_time = pygame.time.get_ticks()
		if current_time - self.last_shot_time >= self.shoot_delay:
			bullet = Bullet(self.ai_game, self, 'images/enemy_bullet.png', direction='down')
			self.bullet_list.append(bullet)
			self.last_shot_time = pygame.time.get_ticks()
