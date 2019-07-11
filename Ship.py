import pygame 


class Ship():
	def __init__(self,screen,ai_settings):
		self.screen = screen 
		self.ai_settings=ai_settings
		self.image = pygame.image.load('images/space_ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx= self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom - 10
		self.moving_right = False
		self.moving_left = False 
		self.center = float(self.rect.centerx)
		
		
	def ship_center(self):
		#--Возвращение корабля в центр--
		self.center = self.screen_rect.centerx
		
	def update(self):
		if self.moving_right and self.rect.right <= self.screen_rect.right:
			self.center += self.ai_settings.ship_speed
		if self.moving_left and self.rect.left >0:
			self.center -= self.ai_settings.ship_speed
		self.rect.centerx = self.center
	
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
