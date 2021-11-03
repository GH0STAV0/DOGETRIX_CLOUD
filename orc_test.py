
import pandas as pd
import numpy as np
import cv2
import glob ,time
import easyy
import os
import os.path
import pytesseract
from pytesseract import Output
from PIL import Image, ImageEnhance, ImageFilter



local_pwd = os.path.dirname(os.path.realpath( __file__ ))
image_path = local_pwd+'/IMG/'
# os.listdir(p_vpn_g)
modified_image_path=local_pwd+'/IMG_MOD/'
files = os.listdir(image_path)
files_mod = os.listdir(modified_image_path)



def convert_to_gray(img_name):
	captcha_image_full_path = image_path+img_name
	filename = os.path.basename(captcha_image_full_path)
	captcha_text = os.path.splitext(filename)[0]
	print(captcha_image_full_path)


	# Load the image and convert it to grayscale
	image = cv2.imread(captcha_image_full_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
	ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
	ret, thresh2 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)
	ret, thresh3 = cv2.threshold(image, 120, 255, cv2.THRESH_TRUNC)
	ret, thresh4 = cv2.threshold(image, 120, 255, cv2.THRESH_TOZERO)
	ret, thresh5 = cv2.threshold(image, 120, 255, cv2.THRESH_TOZERO_INV)
	th, dst = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
	
	blur_2 = cv2.GaussianBlur(gray, (3,3), 0)
	thresh6 = cv2.threshold(blur_2, 20, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

	# Morph open to remove noise and invert image
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
	opening = cv2.morphologyEx(thresh6, cv2.MORPH_OPEN, kernel, iterations=1)
	invert = 255 - opening

	# data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
	# print(data)



	# grab the base filename as the text



	gray_name=modified_image_path+"gray_"+captcha_text+".png"
	thresh1_name=modified_image_path+"thresh_1_"+captcha_text+".png"
	thresh2_name=modified_image_path+"thresh_2_"+captcha_text+".png"
	thresh3_name=modified_image_path+"thresh_3_"+captcha_text+".png"
	thresh4_name=modified_image_path+"thresh_4_"+captcha_text+".png"
	thresh5_name=modified_image_path+"thresh_5_"+captcha_text+".png"
	dst_name=modified_image_path+"dst"+captcha_text+".png"

	blur2_name=modified_image_path+"blur_2_"+captcha_text+".png"
	thresh6_name=modified_image_path+"thresh_6_"+captcha_text+".png"

	print(gray_name)


	# cv2.imwrite(gray_name,gray)
	# cv2.imwrite(blur2_name,blur_2)
	cv2.imwrite(thresh6_name,thresh6)
	time.sleep(3)




	# cv2.imwrite(thresh1_name,thresh1)
	# cv2.imwrite(thresh2_name,thresh2)
	# cv2.imwrite(thresh3_name,thresh3)
	# cv2.imwrite(thresh4_name,thresh4)
	# cv2.imwrite(thresh5_name,thresh5)
	# cv2.imwrite(dst_name,dst)

# def read_loop(image_path):
# 	easyy.py.easy_ocr_read(path)
# # print(files)
# files
# os.system("rm IMG_MOD/*")
for f in files_mod:
# for f in files:
	print(f)
	# convert_to_gray(f)
	path=modified_image_path+f
	# print(path)
	easyy.easy_ocr_read(path)







