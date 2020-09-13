f = open("quotes.txt")

#print(f.read(11))
#print(f.readline())

for quote in f: #we can use for loop to read the file content.
    print(quote)
f.close() #it's good to close the file after the integration with it.