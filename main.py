from PIL import Image

from PIL import Image, ImageEnhance

def edit_image():
    filename = 'mountain.jpg'
    image = Image.open(filename)

    image.show()

    print("What would you like to edit?")
    print("1 - Crop")
    print("2 - Change Colour")
    print("3 - Rotate")
    print("4 - Enhance")
    choice = input("Choice: ")


    choice_num = int(choice)

    if choice_num == 1:
        print("What dimensions for cropping?")
        left = int(input("Left: "))
        upper = int(input("Upper: "))
        right = int(input("right: "))
        lower = int(input("lower: "))
        box = (left, upper, right, lower)
        cropped_image = image.crop(box)
        cropped_image.show()

    if choice_num == 2:
        print("How would you like to change the image")
        new_red = input("Red: ")
        new_green = input("Green: ")
        new_blue = input("Blue: ")

        red, green, blue = image.split()
        swap_red = red
        swap_green = green
        swap_blue = blue

        if new_red == "red":
            swap_red = red
        elif new_red == "green":
            swap_red = green
        elif new_red == "blue":
            swap_red = blue

        if new_green == "red":
            swap_green = red
        elif new_green == "green":
            swap_green = green
        elif new_green == "blue":
            swap_green = blue

        if new_blue == "red":
            swap_blue = red
        elif new_blue == "green":
            swap_blue = green
        elif new_blue == "blue":
            swap_blue = blue

        new_image = Image.merge("RGB", (swap_red, swap_green, swap_blue))
        new_image.show()

    if choice_num == 3:
        print("How many degrees would you like to rotate the image?")
        rot_deg = int(input("Degrees: "))
        new_image = image.rotate(rot_deg)
        new_image.show()

    if choice_num == 4:
        print("how would you like to change the image?")

        contrast_factor = float(input("Contrast: "))
        contrast = ImageEnhance.Contrast(image)
        contrast_image = contrast.enhance(contrast_factor)
        contrast_image.show()


edit = 1
while edit:
    edit_image()
    another = input("Do you want to edit again? (Y/N): ")
    if another == "Y" or "y":
        edit = 1
    else:
        edit = 0

