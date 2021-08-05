from PIL import Image, ImageFilter
import requests
import sys

try:

    im = Image.open("turtle.jpg")
    im.show()

    #Image details
    print("Format: {0}\nSize: {1}\nMode: {2}".format(im.format, im.size, im.mode))
    print("Width: {0}\nHeight: {1}\nInformation: {2}".format(im.width, im.height, im.info))

    #Rotate an image
    im2=im.rotate(45)
    im2.show()
    im3=im.rotate(90)
    im3.show()
    im4=im.rotate(180)
    im4.show()

    #blurring an image
    blurred = im.filter(ImageFilter.BLUR)

    blurred.save("blurred.png")
    im1 = Image.open("blurred.png")
    im1.show()

    #Converting to grayscale
    grayscale = im.convert('L')
    grayscale.show()

    #Fetching image from an URL

    url = 'https://lh3.googleusercontent.com/proxy/lchlGQKgrICAbmKjR6KsatMPqv_0FOcMF9PjtZ3kwudBQZp60AyGd55zNau2_BKpmlT4LW5PELd8gOvuRQdel90ljtmFOKSGe-qYZLGEq6lnAejDQQ7PB5KaBA'


    resp = requests.get(url, stream=True).raw
    img = Image.open(resp)
    img.save('turtle2.jpg', 'jpeg')  
    img.show()

except requests.exceptions.RequestException as e:  
    sys.exit(1)


  
    





    print("Format: {0}\nSize: {1}\nMode: {2}".format(im.format, im.size, im.mode))
    print("Width: {0}\nHeight: {1}\nInformation: {2}".format(im.width, im.height, im.info))

    #blurred = im.filter(ImageFilter.BLUR)

    #blurred.save("blurred.png")
    #im1 = Image.open("blurred.png")
    #im1.show()

    #grayscale = im.convert('L')
   # grayscale.show()

#except IOError:
    #print("Unable to load image")
    #sys.exit(1)
    
