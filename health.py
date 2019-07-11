import pygame 
from pygame.sprite import Sprite
class Health(Sprite):
	def __init__(self,ai_settings,screen, stats):
		super(Health,self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.stats = stats
		self.health = stats.health
		self.ai_settings = ai_settings 
		
		self.image =  pygame.image.load('images/heart.png')
		self.rect = self.image.get_rect()
		
		self.rect.x =   self.rect.width 
		self.rect.y =  self.rect.height
		
		
	
	def blit(self):
		self.screen.blit(self.image,self.rect)
	
	
		

		
		
		
		
