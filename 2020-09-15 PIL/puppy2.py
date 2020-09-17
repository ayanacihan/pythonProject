from PIL import Image

#Load the image

img = Image.open('puppies/puppies.png').convert('L') #makes it gray color

newImage = img.resize((450,500))

newImage.save('puppies/puppiesresized.jpg')

img.rotate(45).show() #rotate picture 45 degree

#Get basic details about the image
#print(img.format)
#print(img.mode)
#print(img.size)

#Show Image
img.show()

#save Image
img.save('puppies/puppies_gs.jpg')

