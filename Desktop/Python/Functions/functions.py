# --- Define your functions below! ---
# --- Put your main program below! ---
greetings = ["hi","hello","hey","nice to meet you too"]
farewells = ["goodbye","bye","later"]
gratitude = ["thanks", "thank you","yes","yes thank you","yes thanks", "thank you so much"]

def intro():
    print("""Hi my name is Ryan Smith. I will be your chatbot today.""")

def askname():
    name = input("What is your name?")
    return name

def name():
    yourname = askname()
    print("Hey,",yourname,",nice to meet you")

def process_input(answer):
    if answer in greetings:
        say_greeting()
    elif answer in farewells:
        say_farewell()
    elif answer in gratitude:
        say_gratitude()
    else:
        say_default()

def say_greeting():
    print("How may I be of service to you today?")

def say_default():
    print("How may I be of service to you today?")

def say_gratitude():
    print("No problem!")

def say_farewell():
    print("Goodbye. Have a good day!")

def membership():
    print("Your gym membership expires in 10 days. Hope that helped.")

def coach():
    print("Got it! I'll connect you to a representative. Hope I was of good service to you!")

def extra():
    print("No problem. I will now connect you to a representative. Hope I was able to fulfill your needs.")

def say_middle(user_input):
    if user_input == "a":
        membership()
    elif user_input == "b":
        coach()
    else:
        if user_input == "c":
            extra()


def main():
    intro()
    name()
    while True:
        answer = input("(What will you say?)")
        process_input(answer)
        answer = answer.lower()
        user_input = input("(Type 'a' for help with gym membership, 'b' to contact a coach and 'c' for other.)")
        say_middle(user_input)
        user_input = user_input.lower()
        answer = input("(What will you say?)")
        process_input(answer)
        break




# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
