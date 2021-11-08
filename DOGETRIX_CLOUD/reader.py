# import the necessary packages
from PIL import Image
from PIL import ImageEnhance
import PIL.ImageOps
import pytesseract
import argparse
import cv2
import os
import numpy

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image to be OCR'd")
# args = vars(ap.parse_args())

# # load the example image and convert it to RGB, invert it and adjust brightness
# image = Image.open(args["image"]).convert('RGB')
# image = PIL.ImageOps.invert(image)
# image = ImageEnhance.Brightness(image)
# image = image.enhance(10)
# imageArray = numpy.array(image)
# imageArray = imageArray[:, :, ::-1].copy()

# filename = "{}.png".format(os.getpid())
# image.save(filename)

# # load the image as a PIL/Pillow image, apply OCR, and then delete
# # the temporary file
# text = pytesseract.image_to_string(Image.open(filename))
# os.remove(filename)
# print(text)

# show the output images
# cv2.imshow("Image", imageArray)screenshotnew
# cv2.waitKey(0) 1369367 300026-2.png
image2 = cv2.imread('screenshotnew.png')
text2 = pytesseract.image_to_string(image2,lang='eng',config='--psm 13') 
print(text2)