import	sys
import	random
import	pygame
from	ship import Ship
from	background import BackGround
from	bullet import Bullet
from	enemy import Enemy
from	enemy_ship import EnemyShip
from	heart import Heart

class ALienInvasion:

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		self.screen_rect = self.screen.get_rect()

		pygame.display.set_caption("Alien Invasion")
		self.bg_color = (230, 230, 230)

		self.ship = Ship(self)
		self.back_ground = BackGround(self, 1200, 900, 'images/maps/void.png')
		self.game_over = BackGround(self, 600, 600, 'images/game_over.png')
		self.game_over.rect.x += 320
		
		self.bullet_list = []
		self.enemy_list = []
		self.enemy_ship_list = []
		self.last_move_time = pygame.time.get_ticks()

		self.health_list = []

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

	def handle_enemy_shooting(self, enemy_list, direction):
		"""Handle shooting for each enemy and update their bullets."""
		for enemy in enemy_list:
			enemy.shoot()
			self.handle_bullet(enemy.bullet_list, direction)

	def	handle_bullet(self, bullet_list, direction):
		"""Update and render bullets; remove bullets that are off-screen."""
		for bullet in bullet_list[:]:
			if not bullet.update_bullet_position(direction):
				bullet_list.remove(bullet)
			else:
				bullet.put_bullet_on_screen()

	def	handle_enemies(self, enemy_list, bullet_list):
		"""Handle enemies, check for collisions with player bullets."""
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
	
	def define_dir_enemy_ships(self, enemy_ship_list, delay=1000):
		current_time = pygame.time.get_ticks()
		if current_time - self.last_move_time > delay:
			for enemy in enemy_ship_list:
				flag = random.randint(1000, 2000)
				if flag < 1500:
					enemy.move_left = True
					enemy.move_right = False
				else:
					enemy.move_right = True
					enemy.move_left = False
			self.last_move_time = current_time
	
	def switch_enemy_ship_direction(self, enemy):
		if enemy.move_left == True:
			enemy.move_left = False
			enemy.move_right = True
		elif enemy.move_right == True:
			enemy.move_right = False
			enemy.move_false = True

	def check_collision_enemy_ships(self, enemy_ship_list):
		for enemy in enemy_ship_list:
			if enemy.move_left == True and enemy.rect.left > 0:
				enemy.rect.x -= 1
			elif enemy.move_right == True and enemy.rect.right < self.screen_rect.right:
				enemy.rect.x += 1
			for other in enemy_ship_list:
				if other != enemy and abs(enemy.rect.x - other.rect.x) < 100:
					self.switch_enemy_ship_direction(enemy)
					self.switch_enemy_ship_direction(other)
					break 
	
	def move_enemy_ships(self, enemy_ship_list):
		self.define_dir_enemy_ships(enemy_ship_list)
		self.check_collision_enemy_ships(enemy_ship_list)
			
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
					temp_bullet = Bullet(self, self.ship, 'images/bullet.png', direction='up')
					self.bullet_list.append(temp_bullet)
			
			elif event.type == pygame.KEYUP:

				self.check_keyup_movement_events(event, self.ship)
	
	def	check_player_damaged(self, ship, enemy_list, heart_list):
		for enemy in enemy_list:
			for bullet in enemy.bullet_list:
				if abs(bullet.rect.y - ship.rect.y) < 30 and abs(bullet.rect.x - ship.rect.x) < 35:
					if heart_list:
						heart_list.pop()
						enemy.bullet_list.remove(bullet)
						return
	
	def initialise_health(self, health_list):
		offset = 0
		for i in range (0, 3):
			heart = Heart(self, offset)
			health_list.append(heart)
			offset += 50

	def put_health_list_on_screen(self, health_list):
		for heart in health_list:
			heart.put_heart_on_screen()
	
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
	
	def end_game(self):
		while True:
			pygame.display.flip()
			self.back_ground.put_bg_on_screen()
			self.game_over.put_bg_on_screen()
			self.check_keybord_event()

	def run_game(self):

		amount_enemies = 5
		self.initialise_enemies(Enemy, self.enemy_list, amount_enemies)
		self.initialise_enemies(EnemyShip, self.enemy_ship_list, amount_enemies)
		self.initialise_health(self.health_list)
		self.update_screen()
		pygame.display.flip()

		while True:

			self.check_keybord_event()
			self.update_ship_position(self.ship)
			self.move_enemy_ships(self.enemy_ship_list)

			# Handle player's bullets
			if len(self.bullet_list) > 0:
				self.handle_bullet(self.bullet_list, direction='up')

			# Handle mosters, enemy ships and their bullets
			if len(self.enemy_list) > 0:
				self.handle_enemies(self.enemy_list, self.bullet_list)
			if len(self.enemy_ship_list) > 0:
				self.handle_enemies(self.enemy_ship_list, self.bullet_list)
			
			self.handle_enemy_shooting(self.enemy_ship_list, direction='down')
			
			# Reinitialize enemies if all are destroyed
			if len(self.enemy_list) == 0:
				self.initialise_enemies(Enemy, self.enemy_list, amount_enemies)
			if len(self.enemy_ship_list) == 0:
				self.initialise_enemies(EnemyShip, self.enemy_ship_list, amount_enemies)

			self.check_player_damaged(self.ship, self.enemy_ship_list, self.health_list)
			if not self.health_list:
				self.end_game()

			self.put_health_list_on_screen(self.health_list)

			# Update the display
			pygame.display.flip()
			self.update_screen()

if __name__ == '__main__':
	ai = ALienInvasion()
	ai.run_game()

# ADD RANDOMIZED OBSTACLES LIKE ROCKS
# ADD EXPLOTIONS WHEN ENEMY IS DESTROYED
# FINITE AMOUNT OF BULLETS
# KILL COUNT
# SHILDS
# MENU
# PAUSE
# REFACTOR CODE
# MAKE GAMEPLAY MORE INTERESTING
# ADD POWERUPS
# RIGHT/LEFT MOVEMENT OF ENEMYSHIPS
# BLACK HOLE AS LEVEL ENDING
# ADD COINS (CAN BUY NEW SHIPS ANS SHOTS)
# ADD MUSIC
# ADD RANDOM AMOUNT OF ENEMIES AT RANDOM TIMINGS
# ADD PLANET HEALTH BAR
# ADD COLISION WITH LITTLE ENEMIES