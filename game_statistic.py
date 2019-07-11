
class GameStatistic():
	def __init__ (self,ai_settings):
		self.ai_settings = ai_settings
		self.record = 0
		self.reset_stats()
		#--Запуск игры в неактивном состоянии--
		self.game_active = False
		
		
		
		
		
		
	def reset_stats(self):
		# --инициализируем статистику по ходу игры -- 
		self.health= self.ai_settings.ship_limit 
		self.score = 0
		
		

#--сделать файл со статистикой игры имя-счет
