from PIL import Image

FIXED_WIDTH = 1024
def asciify(image, output):
	# specify the name of the image.
	image = Image.open(image)
	image = image.convert('RGB')
	width, height = image.size
	width, height = FIXED_WIDTH, FIXED_WIDTH * height / width
	image = image.resize((width, height))

	# list of chars to be used. (in order).
	chars = list("@%#*+=-:. ")

	output = open(output, 'w')

	for y in range(0, height - 10, 10):
		for x in range(0, width - 5, 5):
			colorSum = 0
			for px in range(5):
				for py in range(10):
					colorSum += max(image.getpixel((x + px, y + py)))

			output.write(chars[colorSum / 50 * len(chars) / 256])
		output.write("\n")
	output.close()

print "working..."
asciify("image.jpg", "output.txt")