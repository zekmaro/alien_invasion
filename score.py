import pygame
from background import BackGround

class Score:

	def __init__(self, ai_game):

		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.score_value = 0
		self.digit_list = self.get_score_array()

	def get_score_array(self):
		score_arr = []
		word_arr = [
			'zero',
			'one',
			'two',
			'three',
			'four',
			'five',
			'six',
			'seven',
			'eight',
			'nine',
		]
		for word in word_arr:
			image_path = f'images/digits/{word}.png'
			temp =	BackGround(self.ai_game, 50, 50, image_path)
			score_arr.append(temp)
		return score_arr
	
	def increase_score(self, amount=1):
		self.score_value += amount

	def put_score_on_screen(self, score, screen_width):
		offset = 0
		while score > 0:
			index = score % 10
			score //= 10
			digit = self.digit_list[index]
			digit.rect.y = 20
			digit.rect.x = screen_width - offset
			self.screen.blit(digit.image, digit.rect)
			offset += 50