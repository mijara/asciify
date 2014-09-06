import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200, 200))

# specify the name of the image.
image = pygame.image.load("image.jpg")

# list of chars to be used. (in order).
chars = list("@%#*+=-:. ")		

output = open("output.txt", 'w')

for y in range(0, image.get_height() - 10, 10):
	for x in range(0, image.get_width() - 5, 5):
		colorSum = 0
		for px in range(5):
			for py in range(10):
				colorSum += max(image.get_at((x + px, y + py))[:3])
		output.write(chars[colorSum / 50 * len(chars) / 256])
	output.write("\n")
output.close()