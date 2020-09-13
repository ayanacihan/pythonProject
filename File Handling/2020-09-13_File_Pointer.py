f = open("quotes.txt")

print(f.read())
print(f.tell()) #default mode 'read' and 'text', the tell method will return '0'
#after we read the file the tell method returned 25. This is the pointer position.

print(f.seek(0)) #we can set the pointer position.
f.close()