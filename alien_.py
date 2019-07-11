
import sys 
from settings import  Settings 
from Ship import Ship
import game_functions as gf 
import pygame 
from pygame.sprite import Sprite, Group
from game_statistic import GameStatistic as GS
from button import Button
from health import Health
from score import Score as sc
#initializing and creating gama screen 
def run_game():
	pygame.init()
	ai_settings = Settings()
	screen=pygame.display.set_mode(( ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(screen,ai_settings)
	bullets = Group()
	aliens = Group()
	healths = Group()
	stats = GS(ai_settings)
	score = sc(ai_settings,screen,stats)
	play_button = Button(ai_settings,screen,'Play')
	gf.create_fleet(ai_settings,screen,aliens,ship)
	gf.health_bar(ai_settings,screen,stats,healths)
	

#start 
	
	
	while True:
		
	#Check the pressing of keyboard and mouse
		gf.check_events(ai_settings,screen,ship,bullets,play_button,stats,aliens,healths,score)
		
#last display every iteration of screen 
		if stats.game_active:
			ship.update()
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
			gf.update_bullets(bullets,aliens,ai_settings,screen,ship,stats,score)
			gf.update_bar(healths, stats)
			gf.update_screen(ai_settings,screen,ship,bullets,aliens,healths,score)
		else:
			gf.Start_Game(ai_settings,screen,play_button)
	
run_game()
