import sys
import pygame
from ship import Ship
from background import BackGround
from bullet import Bullet

class ALienInvasion:

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))

		pygame.display.set_caption("Alien Invasion")
		self.bg_color = (230, 230, 230)

		self.ship = Ship(self)
		self.back_ground = BackGround(self)
		
		self.bullet_list = []
		self.draw_bullet = 0

	def	handle_bullet(self, bullet_list):
		for bullet in bullet_list[:]:
			if bullet.rect.y > 0:
				bullet.put_bullet_on_screen()
				bullet.rect.y -= 10
				pygame.display.flip()
			else:
				bullet_list.remove(bullet)

	def	check_keybord_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()

				elif event.key == pygame.K_UP:
					self.ship.rect.y -= 20
					pygame.display.flip()
				elif event.key == pygame.K_DOWN:
					self.ship.rect.y += 20
					pygame.display.flip()
				elif event.key == pygame.K_LEFT:
					self.ship.rect.x -= 20
					pygame.display.flip()
				elif event.key == pygame.K_RIGHT:
					self.ship.rect.x += 20
					pygame.display.flip()

				elif event.key == pygame.K_SPACE:
					temp_bullet = Bullet(self, self.ship)
					self.bullet_list.append(temp_bullet)
		
	def update_screen(self):
		self.back_ground.put_bg_on_screen()
		self.ship.put_ship_on_screen()

	def run_game(self):
		self.update_screen()
		pygame.display.flip()
		while True:
			self.check_keybord_event()
			if (len(self.bullet_list) > 0):
				self.handle_bullet(self.bullet_list)
			self.update_screen()

if __name__ == '__main__':
	ai = ALienInvasion()
	ai.run_game()

# ADD RANDOMIZED OBSTACLES LIKE ROCKS
# ADD EXPLOTIONS WHEN ENEMY DESTROYED