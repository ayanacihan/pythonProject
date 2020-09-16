#if __name__=="main" allows you to run Python files as reusable

print("Hello")
print("bla bla")

if __name__ == "__main__":
    print("file1 is being run directly")
else:
    print("file1 is being imported")