# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    pic=Image.open(filename)
    return pic



# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(pic):
    pic.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(pic,filename):
    pic.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(pic):
    #find the RGB for the product
    pixels = pic.getdata()
    new_pixels=[] #creates list for new image pixels
    #intensity = r+g+b
    #if intensity < 182 set pixel color to (0,51,76)
    for p in pixels:
        intensity = p[0]+p[1]+p[2]
        if intensity < 182:
            new_pixels.append((0,51,76))
        elif 182 <= intensity < 364:
            new_pixels.append((217,26,33))
        elif 364 <= intensity < 546:
            new_pixels.append((112,150,158))
        elif intensity >= 546:
            new_pixels.append((252,227,166))
    #if intensity is between 182 and 364 set pixel color to (217,26,33)
    #if intensity is between 364 and 546 set pixel color to (112,150,158)
    #if intensity > 546 set pixel color to (252,227,166)
    #save the filtered pixels as a new image

    newpic = Image.new("RGB", pic.size)
    newpic.putdata(new_pixels)
    return newpic

def main():
        filename = input("Enter the name of the image to edit.")
        img = load_img(filename)
        newing = obamicon (img)
        save_img(newing, "recolored.jpg")

main()
