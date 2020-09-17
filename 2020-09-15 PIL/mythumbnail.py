#This will create 3 new
from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob("puppies/*jpg"): #search any png files
    file, ext = os.path.splitext(infile) #infile means for any file object
    img = Image.open(infile)
    img.thumbnail(size,Image.ANTIALIAS) #ANTIALIAS method is to minimize the distortion when you compress the image
    img.save(file + ".thumbnail", "JPEG")