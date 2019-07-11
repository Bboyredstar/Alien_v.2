import pygame.font
#--Класс кнопок--

class Button():
	def __init__(self,ai_settings,screen,msg):
	#--Инициализируем атрибуты кнопки--
		self.screen = screen
		self.ai_settings = ai_settings
		self.screen_rect = self.screen.get_rect()
	
	#--размеры кнопок--
		self.width = 200
		self.height = 50 
		self.button_color = (132,112, 255)
		self.text_color = (250,250,250)
	#--Шрифт по умолчанию 48 размер шрифта--
		self.font = pygame.font.SysFont(None,48,False,True)
	
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center 
		self.prep_msg(msg)
	
	def prep_msg(self,msg):
		#--Преобразует msg в прямоугольник и выравнивает текст по центру--
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
