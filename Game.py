import pygame as pg

cBackground = (150,150,150)
cGreen = (0,255,0)

(width,height) = (640,480)
screen = pg.display.set_mode((width,height))
screen.fill(cBackground)

pg.display.flip()

clock = pg.time.Clock()
mouseX,mouseY = 0,0
rectStartX,rectStartY = 0,0
initPoint = False

running = True
while running:
	# Fill the background 
	screen.fill(cBackground)

	# Loop through events
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		# When a mouse button is pressed
		elif event.type == pg.MOUSEBUTTONDOWN:
			# If we haven't started drawing a rectangle, get the initial points
			if initPoint == False:
				initPoint = True
				rectStartX = pg.mouse.get_pos()[0]
				rectStartY = pg.mouse.get_pos()[1]
		elif event.type == pg.MOUSEBUTTONUP:
			initPoint = False
	
	mouseX = pg.mouse.get_pos()[0]
	mouseY = pg.mouse.get_pos()[1]

	if initPoint:
		pg.draw.lines(screen,cGreen,True,[(rectStartX,rectStartY),(mouseX,rectStartY),(mouseX,mouseY),(rectStartX,mouseY)])



	clock.tick(60)
	pg.display.update()