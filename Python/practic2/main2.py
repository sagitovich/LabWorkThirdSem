import pygame
import random												# Импортируем нужные библиотеки

pygame.init() 												# Инициализируем pygame

win = pygame.display.set_mode((1000,1000)) 					# Создадим окно 600х600

pygame.display.set_caption("Help me please") 			# Дадим окну имя

Triangle = [[500, 50], [100, 900], [900, 900]] 				# Определим вершины треугольника

x, y = random.randint(0, 1000), random.randint(0, 1000)  		# Определим изначальную точку, 
															# от которой мы будем рисовать наш треугольник

RUN = True
while RUN: 													# Главный цикл
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RUN = False
	A = random.randint(0, 2) 								# Рандомная вершина нашего треугольника
	x, y = 0.5 * (x + Triangle[A][0]), 0.5 * (y + Triangle[A][1])# Вычисляем новую точку
	# треугольника Серпинского по середине между прежней точкой и любой вершиной

	pygame.draw.line(win, (255, 255, 255), (x, y), (x, y), 1)   # Рисуем нашу точку
	pygame.display.update() 									# Обновляем экран
	
pygame.quit()