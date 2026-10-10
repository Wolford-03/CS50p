def main():
    name = input("What is your name? ")
    first, last = name.split()
    hello(name)

def hello(to = "world"):
    print("Hello",to)

main()