from utils import greet

def main():
    name = input("What is your name? ")
    message = greet(name)
    print(message)
#better way to run the main code
if __name__ == "__main__":
    main()