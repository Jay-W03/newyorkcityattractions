postit = {
"Ester" : "Yellow",
"Myrai" : "Green",
"Evelyn" : "Blue",
"Jayda" : "Blue",
"Jinming" : "Purple",
"Ariella" : "Yellow",
"Jacquie" : "Blue",
"Reggie" : "Yellow",
"Bridget" : "Green",
"Jennifer" : "Green",
"Michela" : "Yellow",
"Lina" : "Green",
"Kelsey" : "Green",
"Syeda" : "Orange",
"Naoroz" : "Blue",
"Taylor" : "Yellow",
"Gabby" : "Green",
"Fiorella" : "Purple"
}

#Goal 1: Make a list of all the colors
colors = []
#Make a for loop to loop through the names and colors in the dictionary
for name in postit:
    color = postit[name]
    colors.append(color)
#print(colors) - test the colors list

#Goal 2: Create a dictionary with colors = key and frequency = value
color_frequency = {}
for color in colors:
    if color in color_frequency:
        currentVal = color_frequency[color]
        newVal = currentVal + 1
        color_frequency[color] = newVal
    else:
        color_frequency[color] = 1
