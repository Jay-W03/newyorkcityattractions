def askname():
    name = input("What is your name?")
    print(name)
    return name

def main():
    yourname = askname()
    print("Hey,",yourname,",nice to meet you")

main()
