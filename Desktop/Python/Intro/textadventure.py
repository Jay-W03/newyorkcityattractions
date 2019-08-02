    # Update this text to match your story.
start = '''
    You wake up in the middle of the night and hear a strange noise in your house.
    You grow curious and decide to find out where the noise is coming from.
    The kitchen is to your right and the living room is to to your left.
    Where will you check first?
    '''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()

if user_input == "left":

    start = '''
        You walk into the living room and trip on something. You check to see what it was
        and see your little sister's doll staring straight at you. You then hear the strange
        noise again.It sounds like it's coming from the backyard. Are you gonna go see?
        '''

print(start)

print("Type yes or no")
user_input = input()
if user_input == "yes":
    start = '''
    You walk towards the backyard. The wind is very strong. Suddenly, you get stuck in a sink hole in the grass.
    You then hear footsteps approaching. They come closer and closer. Are you gonna grab a stick or a rock
    as your defense weapon?
    '''
    print(start)

    print("Type rock or stick")
    if user_input == "rock":
        start = '''
        You grab a rock and wait for the person to come closer. The footsteps unexpectedly stop. Suddenly,
        a man in a mask finds you in the sink hole. He is holding a chainsaw. Oh no! He turns on the chainsaw
        and is coming towards you. Are you going to try to knock him out or give in?
        '''
        print(start)
        print("Type '1' to knock him out or '2' to give in")

    elif user_input == "stick":
        start = '''

        '''

elif user_input == "no":
    start = '''
        You stay inside the house. As soon as you turn around you see the shadow of a strange figure upstairs.
        You know no one else is home since your sister is at a sleepover and your parents are at the hospitala
        with your grandmother.
        Will you call the police or grab a weapon and sneak upstairs?
        '''
print(start)

print("Type 'A' for police or 'B' for weapon.")

if user_input == "right":
    print("You choose to go right into the kitchen.") # Update to match your story.


        # Continue code to finish story.
