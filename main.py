from captcha.image import ImageCaptcha


import matplotlib.pyplot as plt
import random

#create a list of numbers and alphabets to create capcha text
number_list = ['0', '1', '2', '3','4', '5','6','7','8','9']
alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_list_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def create_capcha(capcha_text_size = 5):
    capcha_string_list = []

    base_char = alphabet_list + alphabet_list_uppercase + number_list
    print(base_char)
    for i in range(capcha_text_size):
        char = random.choice(base_char)

        capcha_string_list.append(char)
    capcha_string = ''
    for i in capcha_string_list:
        capcha_string += str(i)
    return capcha_string




#create an image capcha with text
def create_image_capcha(capcha_text):
    image_capcha = ImageCaptcha()
    #create the image capcha
    image = image_capcha.generate_image(capcha_text)
    # Save the image to a png file.
    image_file = "./captcha_" + capcha_text + ".png"
    image_capcha.write ( capcha_text , image_file )

    # Display the image in a matplotlib viewer.
    plt.imshow ( image )
    plt.show ( )

    print ( image_file + " has been created." )

if __name__ == '__main__':
    captcha_text = create_capcha()

    #create an image captcha
    create_image_capcha(captcha_text)