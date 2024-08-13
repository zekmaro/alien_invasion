import	sys
import	random
import	pygame
from	ship import Ship
from	background import BackGround
from	bullet import Bullet
from	enemy import Enemy

class ALienInvasion:

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		self.screen_rect = self.screen.get_rect()

		pygame.display.set_caption("Alien Invasion")
		self.bg_color = (230, 230, 230)

		self.ship = Ship(self)
		self.back_ground = BackGround(self)
		
		self.bullet_list = []
		self.enemy_list = []
		self.draw_bullet = 0

	def	check_enemy_exist_at_x(self, existing_enemy, current_enemy_coor_x):
		return abs(existing_enemy.rect.x - current_enemy_coor_x) >= 50
	
	def initialise_enemies(self, amount_enemies):
		while amount_enemies:
			enemy = Enemy(self)
			valid_position = False
			while not valid_position:
				spawn_coor_x = random.randint(0, self.screen_rect.width - enemy.rect.width)
				valid_position = True
				
				for existing_enemy in self.enemy_list:
					if not self.check_enemy_exist_at_x(existing_enemy, spawn_coor_x):
						valid_position = False
						break  # No need to check further, find a new position

			enemy.rect.x = spawn_coor_x
			self.enemy_list.append(enemy)
			amount_enemies -= 1

	def	handle_bullet(self, bullet_list):
		for bullet in bullet_list[:]:
			if bullet.rect.y > 0:
				bullet.put_bullet_on_screen()
				bullet.rect.y -= 10
			else:
				bullet_list.remove(bullet)

	def	handle_enemies(self, enemy_list, bullet_list):
		for enemy in enemy_list[:]:
			if enemy.rect.y < self.screen_rect.bottom:
				enemy.put_enemy_on_screen()
				enemy.rect.y += 1
				for bullet in bullet_list[:]:
					if abs(bullet.rect.y - enemy.rect.y) < 30 and abs(bullet.rect.x - enemy.rect.x) < 30:
						enemy_list.remove(enemy)
						bullet_list.remove(bullet)
			else:
				enemy_list.remove(enemy)
			# add collision logic

	def	check_keydown_events()

	def	check_keybord_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:

				if event.key == pygame.K_ESCAPE:
					sys.exit()
					
				elif event.key == pygame.K_UP:
					self.ship.rect.y -= 20
				elif event.key == pygame.K_DOWN:
					self.ship.rect.y += 20
				elif event.key == pygame.K_LEFT:
					self.ship.rect.x -= 20
				elif event.key == pygame.K_RIGHT:
					self.ship.rect.x += 20

				elif event.key == pygame.K_SPACE:
					temp_bullet = Bullet(self, self.ship)
					self.bullet_list.append(temp_bullet)
		
	def update_screen(self):
		self.back_ground.put_bg_on_screen()
		self.ship.put_ship_on_screen()

	def run_game(self):
		amount_enemies = 10
		self.initialise_enemies(amount_enemies)
		self.update_screen()
		pygame.display.flip()
		while True:
			self.check_keybord_event()
			if (len(self.bullet_list) > 0):
				self.handle_bullet(self.bullet_list)
			if (len(self.enemy_list) > 0):
				self.handle_enemies(self.enemy_list, self.bullet_list)
			pygame.display.flip()
			self.update_screen()

if __name__ == '__main__':
	ai = ALienInvasion()
	ai.run_game()

# ADD RANDOMIZED OBSTACLES LIKE ROCKS
# ADD EXPLOTIONS WHEN ENEMY DESTROYED