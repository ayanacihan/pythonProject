from PIL import Image

#Load the image

img = Image.open('puppies/puppies.png')

#Get basic details about the image

print(img.format)
print(img.mode)
print(img.size)

#Show Image

img.show()