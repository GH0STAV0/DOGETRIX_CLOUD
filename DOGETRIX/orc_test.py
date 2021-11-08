
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
# os.listdir(p_vpn_g)


########################                              #####################


input_image_folder="/INPUT_IMG/"
output_image_folder="/OUTPUT_IMG/"

image_path = local_pwd+input_image_folder
image_output=local_pwd+output_image_folder
# image_path = local_pwd+'/IMG/'

modified_image_path=local_pwd+output_image_folder #'/IMG_MOD/'
files = os.listdir(image_output)
files_mod = os.listdir(image_path)
# print(modified_image_path)
print(image_path)




###########################################################################""

def convert_to_gray(img_name):
	captcha_image_full_path = image_path+img_name
	filename = os.path.basename(captcha_image_full_path)
	captcha_text = os.path.splitext(filename)[0]
	print(captcha_image_full_path)


	# Load the image and convert it to grayscale
	image = cv2.imread(captcha_image_full_path)
	# image = cv2.medianBlur(image,5)
	

	# ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
	ret, thresh1 = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
	
	ret, thresh2 = cv2.threshold(thresh1, 120, 255, cv2.THRESH_BINARY_INV)
	ret, thresh3 = cv2.threshold(thresh2, 120, 255, cv2.THRESH_TRUNC)
	
	ret, thresh5 = cv2.threshold(thresh3, 120, 255, cv2.THRESH_TOZERO_INV)
	# th, dst = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
	ret, thresh4 = cv2.threshold(thresh5, 120, 255, cv2.THRESH_TOZERO)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	blur_2 = cv2.GaussianBlur(gray, (3,3), 0)
	

	th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
	th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)


	thresh6 = cv2.threshold(blur_2, 130, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

	# Morph open to remove noise and invert image
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
	opening = cv2.morphologyEx(thresh6, cv2.MORPH_OPEN, kernel, iterations=1)
	invert = 255 - opening
# 
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

# for f in files_mod:


def convert_it():
	cmdd="rm "+local_pwd+output_image_folder+"*"
	os.system(cmdd)
	
	for f in files_mod:
		print(f)
		convert_to_gray(f)
		# path=modified_image_path+f
		path=local_pwd+output_image_folder+f

		# print(path)
		# easyy.easy_ocr_read(path)

def read_it():
	for f in files:
		print(f)
		# convert_to_gray(f)
		# path=modified_image_path+f
		path=local_pwd+output_image_folder+f
		# print(path)
		easyy.easy_ocr_read(path)



convert_it()
read_it()



