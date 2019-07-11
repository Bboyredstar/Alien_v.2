import pygame
import random 
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super(Alien,self).__init__()
		
		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image = pygame.image.load("images/alien.png") 
		self.rect = self.image.get_rect()
		
		#стартовая позиция корабля пришельцев
		#х-координата - отступ на ширину корабля пришельцев 
		self.rect.x = self.rect.width 
		#у-координата - отступ половина от высоты пришельцев
		self.rect.y = self.rect.height 
		# position of alien ship in x
		self.x = float(self.rect.x)  

	#функция проверяет позицию пришельца, 
	# если находится у границы экрана возвращает True	
	def check_direction(self): 
		screen_rect = self.screen.get_rect() #получаем размер экрана 
		if self.rect.right >= screen_rect.right:
    			return True
		if self.rect.left <= 0:
    			return True
	#функция предвижения флота 
	def update(self):
		self.rect.x += (self.ai_settings.alien_speed * self.ai_settings.alien_direction)
		
			
	#функция отрисовки корабля, используется в aliens	
	def blit (self):
		self.screen.blit(self.image,self.rect)
