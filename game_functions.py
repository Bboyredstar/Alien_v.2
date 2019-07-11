
import sys 
from time import sleep
import pygame 
from bullets import Bullet 
from Alien import Alien 
from health import Health 
def check_KeyDown(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		 ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()


def check_KeyUp(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets,play_button,stats,aliens,healths,score):
	for event in pygame.event.get():
		if event.type  == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_KeyDown(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_KeyUp(event,ship)		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,aliens,bullets,ship,healths,score)
	
def check_play_button(stats,play_button,mouse_x,mouse_y,ai_settings,screen,aliens,bullets,ship,healths,score):
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		stats.game_active = True
		ai_settings.initializing_par()
		
		#--Сброс статистики--
		stats.reset_stats()
		score.prep()
		#--Отрисовка здоровья--
		healths.empty()
		health_bar(ai_settings,screen,stats,healths)
		
		#--Очистка пришельцев--
		aliens.empty()
		#--Очистка пуль--
		bullets.empty()
		#--Создание флота--
		create_fleet(ai_settings,screen,aliens,ship)
		#--Центрирование корабля--
		ship.ship_center()
		#--Скрываем курсор мыши--
		pygame.mouse.set_visible(False)

def fire_bullets(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
def number_of_aliens(ai_settings,alien_width):
	#--Вычисляет количество приешельцев в ряду--
	#--Количество пришельцев = свободное место на экране с учетом отступов / 2* ширина пришельца
	avaible_space = ai_settings.screen_width - 2 * alien_width
	number_aliens = int(avaible_space / (2*alien_width))
	
	return number_aliens
	
def number_of_row(ai_settings,ship_height,alien_height):
	#--Вычисляет количество  рядов--
	#--Количество рядов = свободное место на экране с учетом отступов / 2* высоты пришельца
	avaible_space = ai_settings.screen_height - (alien_height) - ship_height
	number_rows = int(avaible_space / (1.5*alien_height))
	
	return number_rows
	
def create_alien(ai_settings,screen,aliens,num_alien,num_row):
	alien = Alien(ai_settings, screen)
	#--Сдвиг пришельцев если нечетный ряд--
	if num_row%2!=0:
		num_alien +=1
		alien.rect.x = int(alien.rect.width/2) + (2*alien.rect.width * num_alien) 
		alien.rect.y = int(alien.rect.height/2) + (1.5*alien.rect.height * num_row)
	else:
		alien.rect.x = alien.rect.width  + (2*alien.rect.width * num_alien) 
		alien.rect.y = int(alien.rect.height/2) + (1.5*alien.rect.height * num_row)
	
	aliens.add(alien)
		
def create_fleet(ai_settings,screen,aliens,ship):
	#-- Создание флота --
	new_alien = Alien(ai_settings,screen)
	num_aliens = int(number_of_aliens(ai_settings,new_alien.rect.width))
	num_row = int(number_of_row(ai_settings,ship.rect.height,new_alien.rect.height))
	for rw in range(num_row):
		for al in range (num_aliens):
			create_alien(ai_settings,screen,aliens,al,rw)
	
def check_edges (ai_settings,aliens):
	 #--Меняем направление движения при достижения края--
	for alien in aliens.sprites():
		if alien.check_direction():
			change_direction(ai_settings,aliens)
			break
			
def change_direction (ai_settings,aliens):
	# --Меняем направление--
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.alien_drop_speed
	ai_settings.alien_direction *= -1

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	#--Обновляет позиции пришельцев--
	check_edges(ai_settings,aliens)
	aliens.update()
	check_collision(ai_settings,stats,screen,ship,aliens,bullets)
	check_bottom(ai_settings,stats,screen,ship,aliens,bullets)
	
def check_bottom(ai_settings,stats,screen,ship,aliens,bullets):
	screen_ = screen.get_rect()
	for alien_ in aliens.sprites():
		if alien_.rect.bottom >= screen_.bottom:
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
			break
	
def check_collision (ai_settings,stats,screen,ship,aliens,bullets):
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
	
	
def health_bar(ai_settings,screen,stats,healths):
		for i in range(stats.health):
			heart = Health(ai_settings,screen,stats)
			heart.rect.x =heart.rect.width * (i+1)
			healths.add(heart)
			
def update_bar(healths, stats):
	bar = len(healths) - stats.health
	last = len(healths)
	if bar!=0:
		 for i in range(bar):
			 for health in healths.copy():
				 healths.remove(health)
				 break

	 
def update_bullets(bullets,aliens,ai_settings,screen,ship,stats,score):
	#--Обновляет позицию пули и удаляет вышеджшие за экран--
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# -- Обнаружение коллизий с пришельцем --
	collisions = pygame.sprite.groupcollide (bullets,aliens,True,True)
	if collisions:
		for alien in collisions.values(): 
			stats.score += ai_settings.alien_kill_point * len(alien)
			
			if stats.score > stats.record :
				stats.record = stats.score
			score.prep()
	refreshing_fleet(aliens,ai_settings,screen,ship)
	
	
def refreshing_fleet(aliens,ai_settings,screen,ship):
	# -- Восстановление флота --
	if len(aliens) == 0:
		ai_settings.increase_par()
		create_fleet(ai_settings,screen,aliens,ship)
				
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	#--Обработка столкновения пришельцев с кораблем--
	if stats.health >1:
		stats.health = stats.health - 1
		
	#--Очистка пуль и пришельцев--
		aliens.empty()
		bullets.empty()
	#--Создание флота и центрирование корабля--
		create_fleet(ai_settings,screen,aliens,ship)
		ship.ship_center()
	#--Пауза--
		sleep(0.5)
		
	else:
		
		aliens.empty()
		bullets.empty()		
		stats.game_active = False
		pygame.mouse.set_visible(True)
	
def update_screen(ai_settings,screen,ship,bullets,aliens,healths,score):
	#--Обновляет экран, отрисовывает фон, пули, корабль, флот пришельцев--
	screen.fill(ai_settings.bg_color)#
	
	for health in healths:
		health.blit()
		
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	score.show_score()
	ship.blitme()
	for alien_ in aliens:
		alien_.blit()
	
	pygame.display.flip()#
	
def Start_Game(ai_settings,screen,play_button):
	screen.fill(ai_settings.bg_color)
	play_button.draw_button()
	pygame.display.flip()
	
	

