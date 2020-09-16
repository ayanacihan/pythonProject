f = open("quotes.txt")

print(f.readable()) #check if the file is readable or not. This will return boolean value.

print(f.read()) #this method prints the content of the file.

f.close() #we closed the readability of the file.
f.readable() #this will throw an error.