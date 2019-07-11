# 
#
#
#
#
#
#
#--Класс хранит настройки для игры -- 
#--Парамеры экрана--
#--Количество жизней и скорость корабля--
#--Параметры пуль--
#--Параметры пришельцев--
class Settings():
	
	
	def __init__(self):
		#--параметры экрана (Ширина/Высота/Фон)--
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (250,250,250)
		
		#--Парамеетры корабля (Скорость/Количсетво жизней)--
		
		
		
		#--Парметры пуль (Размеры/Цвет/Скорость/Количетсво пуль за один фрейм)--
		self.bullet_width = 3
		self.bullet_height = 12
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3 
		
		
		#--Парметры пришельцев (Скорость по оси Х, Скорость снижения, Направление движения, Направление Снижения)
		self.ship_limit = 2
		self.alien_drop_dir = 1
		#--пареметр ускорения игры--
		self.speedup = 1.1
		self.initializing_par()
		self.increase_par()
		
	def initializing_par(self):
		#--Инициализируем параметры влияющие на игровой процесс--
		self.ship_speed = 3.5 
		self.bullet_speed_factor = 5.5
		self.alien_speed = 2.5
		self.alien_direction = 1
		self.alien_kill_point = 30
		self.alien_drop_speed = 5
		
	
	def increase_par(self):
		self.ship_speed *= self.speedup
		self.bullet_speed_factor *= self.speedup
		self.alien_speed *= self.speedup
		self.alien_kill_point = int(self.alien_kill_point*1.1)
		self.alien_drop_speed *= self.speedup
