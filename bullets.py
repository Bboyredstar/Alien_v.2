import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen = screen
		#self.image = pygame.image.load('images/bullet.png')
		#self.rect = self.image.get_rect()
		#Создание пули в 0,0 и перемещение в нужное место
		self.rect = pygame.Rect((0, 0),(ai_settings.bullet_width,ai_settings.bullet_height))
		self.rect.centerx = ship.rect.centerx  #позиционирование  пули от центра корабля и от верхней точки корабля 
		self.rect.top = ship.rect.top 
		
		
		#позиция пули 
		#
		self.y = float(self.rect.y)
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	
	def update(self):
		#обновление позиции пули
		self.y -= self.speed_factor
		self.rect.y = self.y
		
	def draw_bullet (self):
		#отрисовка пули 
		pygame.draw.rect(self.screen ,self.color, self.rect)
		#self.screen.blit(self.image, self.rect) 
	
