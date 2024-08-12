import sys
import pygame
from ship import Ship
from background import BackGround

class ALienInvasion:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Alien Invasion")
		self.bg_color = (230, 230, 230)
		self.ship = Ship(self)
		self.back_ground = BackGround(self)

	def update_screen(self):
		self.back_ground.put_bg_on_screen()
		self.ship.put_ship_on_screen()
		pygame.display.flip()

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			
			self.update_screen()

if __name__ == '__main__':
	ai = ALienInvasion()
	ai.run_game()