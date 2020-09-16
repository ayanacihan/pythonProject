import file1 as f1 #we imported file1.py

print("Hello from file 2")

if __name__ == "__main__": #if this is __main__, then the first part of the if sentence will run
    print("file1 is being run directly")
else:
    print("file1 is being imported")