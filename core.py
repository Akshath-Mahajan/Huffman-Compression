from custom_nodes import node
from compress import *
from decompress import *

if __name__ == "__main__":
    print("\n")
    print("Would you like to compress or decompress a file?")
    choice = input().lower()
    print("Enter file to "+choice)
    filename = input()
    if choice == "compress":
        compress(filename)
        print("File compressed!")
    else:
        if choice == "decompress":
            decompress(filename)
            print("File decompressed!")
        else:
            print("Invalid choice")


