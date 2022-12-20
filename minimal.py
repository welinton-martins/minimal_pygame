# import the pygame module, so you can use it
import pygame

# define a main function
def main():
	# initialize the pygame module
	pygame.init()
	# load and set the logo
	# logo = pygame.image.load("logo32x32.png")
	# pygame.display.set_icon(logo)
	pygame.display.set_caption("minimal program")
	pygame.display.flip()

	#create a surface on screen that has the size of 240 x 100
	screen = pygame.display.set_mode((240,180))

	# image = pygame.image.load("")
	screen.blit(image, (50, 50))

	# define a variable to control the mai loop
	running = True
	# define the position of the smiley
	xpos = 50
	ypos = 50
	# how many pixels we move your smiley each frame
	step_x = 10
	step_y = 10 

	# main loop
	while running:
		# check if the smiley is still on screen, if not change direction
		if xpos>screen_width-64 or xpos<0:
			step_x = -step_x
		if ypos>screen_height-64 or ypos<0:
			step_y = -step_y
		# update the position of the smiley
		xpos += step_x # move it to the right
		ypos += step_y # move it down

		# event handling, gets all event from the event queue
		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
	# call the main function
	main()