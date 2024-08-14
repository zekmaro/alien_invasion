import	sys
import	random
import	pygame
from	ship import Ship
from	background import BackGround
from	bullet import Bullet
from	enemy import Enemy
from	enemy_ship import EnemyShip

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
		self.enemy_ship_list = []
		self.enemy_ship_bullet_list = []

	def	check_enemy_exist_at_x(self, existing_enemy, current_enemy_coor_x):
		return abs(existing_enemy.rect.x - current_enemy_coor_x) >= 50
	
	def initialise_enemies(self, enemy_class, enemy_list, amount_enemies):
		while amount_enemies:
			enemy = enemy_class(self)
			valid_position = False
			while not valid_position:
				spawn_coor_x = random.randint(0, self.screen_rect.width - enemy.rect.width)
				valid_position = True
				
				for existing_enemy in enemy_list:
					if not self.check_enemy_exist_at_x(existing_enemy, spawn_coor_x):
						valid_position = False
						break  # No need to check further, find a new position

			enemy.rect.x = spawn_coor_x
			enemy_list.append(enemy)
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
			if enemy.rect.bottom < self.screen_rect.bottom:
				enemy.put_enemy_on_screen()
				if enemy.can_move == True:
					enemy.rect.y += 1
				for bullet in bullet_list[:]:
					if abs(bullet.rect.y - enemy.rect.y) < 30 and abs(bullet.rect.x - enemy.rect.x) < 30:
						enemy_list.remove(enemy)
						bullet_list.remove(bullet)
			else:
				enemy_list.remove(enemy)

	def	check_keydown_movement_events(self, event, ship):
		if event.key == pygame.K_UP:
			ship.move_up = True
		elif event.key == pygame.K_DOWN:
			ship.move_down = True
		elif event.key == pygame.K_LEFT:
			ship.move_left = True
		elif event.key == pygame.K_RIGHT:
			ship.move_right = True
	
	def	check_keyup_movement_events(self, event, ship):
		if event.key == pygame.K_UP:
			ship.move_up = False
		elif event.key == pygame.K_DOWN:
			ship.move_down = False
		elif event.key == pygame.K_LEFT:
			ship.move_left = False
		elif event.key == pygame.K_RIGHT:
			ship.move_right = False

	def	check_keybord_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:

				if event.key == pygame.K_ESCAPE:
					sys.exit()
					
				self.check_keydown_movement_events(event, self.ship)

				if event.key == pygame.K_SPACE:
					temp_bullet = Bullet(self, self.ship)
					self.bullet_list.append(temp_bullet)
			
			elif event.type == pygame.KEYUP:

				self.check_keyup_movement_events(event, self.ship)
		
	def	update_ship_position(self, ship):
		if ship.move_up == True:
			ship.rect.y -= 3
		if ship.move_down == True:
			ship.rect.y += 3
		if ship.move_right == True:
			ship.rect.x += 3
		if ship.move_left == True:
			ship.rect.x -= 3
	
	def update_screen(self):
		self.back_ground.put_bg_on_screen()
		self.ship.put_ship_on_screen()

	def run_game(self):
		amount_enemies = 2
		self.initialise_enemies(Enemy, self.enemy_list, amount_enemies)
		self.initialise_enemies(EnemyShip, self.enemy_ship_list, amount_enemies)
		self.update_screen()
		pygame.display.flip()
		while True:
			self.check_keybord_event()
			if len(self.bullet_list) > 0:
				self.handle_bullet(self.bullet_list)
			if len(self.enemy_list) > 0:
				self.handle_enemies(self.enemy_list, self.bullet_list)
			if len(self.enemy_ship_list) > 0:
				self.handle_enemies(self.enemy_ship_list, self.bullet_list)
			if len(self.enemy_list) == 0:
				self.initialise_enemies(Enemy, self.enemy_list, amount_enemies)
			if len(self.enemy_ship_list) == 0:
				self.initialise_enemies(EnemyShip, self.enemy_ship_list, amount_enemies)
			self.update_ship_position(self.ship)
			pygame.display.flip()
			self.update_screen()

if __name__ == '__main__':
	ai = ALienInvasion()
	ai.run_game()

# ADD RANDOMIZED OBSTACLES LIKE ROCKS
# ADD EXPLOTIONS WHEN ENEMY IS DESTROYED
# FINITE AMOUNT OF BULLETS
# ENEMY SHIPS
# HEALTH BAR
# KILL COUNT
# SHILDS
# MENU
# PAUSE
# ENEMIES SHOOTING AND MOVING
# REFACTOR CODE
# MAKE GAMEPLAY MORE INTERESTING

# if movement key pressed flag to change position is true till the keyup event took place