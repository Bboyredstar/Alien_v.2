import pygame.font

class Score():
	def __init__(self,ai_settings,screen,stats):
		self.ai_settings = ai_settings
		self.screen = screen  
		self.stats = stats 
		
		self.screen_rect = screen.get_rect()
		
		self.text = (60,60,60)
		self.font = pygame.font.SysFont(None,48)
		self.prep()
		
	def prep(self):
		score = int(round(self.stats.score,-1))
		score_str = "{:,}".format(self.stats.score)
		record = int(round(self.stats.record,-1))
		record_str = "{:,}".format(self.stats.record)
		self.record_image = self.font.render(record_str,True,self.text,self.ai_settings.bg_color)
		self.score_image = self.font.render(score_str,True,self.text,self.ai_settings.bg_color)
		self.record_rect= self.record_image.get_rect()
		self.score_rect = self.score_image.get_rect()
		self.record_rect.center = self.screen_rect.center
		self.record_rect.y = 60
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 60 
	def show_score(self):
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.record_image,self.record_rect)
