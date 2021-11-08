
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
import easyocr
from PIL import Image
# import boto3
import os , cv2
import calendar , time

# import pandas as pd
# from Levenshtein import distance
# from tqdm.notebook import tqdm



pwd = os.path.dirname(os.path.realpath( __file__ ))
p_vpn_g = pwd+'/IMG/'
os.listdir(p_vpn_g)
files = os.listdir(p_vpn_g)
# print(files)
# reader = easyocr.Reader(['en'], gpu = False)
#textract = boto3.client('textract')

def img_process(file_path):
    img = cv2.imread(file_path)
    # img = cv2.medianBlur(img, 9)
    # img = cv2.Canny(img, 100, 200)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gre_path=file_path.split(".")[0]+"grey.png"
    cv2.imwrite(gre_path,gray)
    print("grey ")
    #max_filter = maximumBoxFilter(2,gray)  #custom function 
    median_filter = cv2.medianBlur(gray,5)
    ada_mean_thresh = cv2.adaptiveThreshold(median_filter,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    thresh = cv2.threshold(ada_mean_thresh, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    thre_path=file_path.split(".")[0]+"ther.png"
    
    cv2.imwrite(thre_path,thresh)
#     invert_img = cv2.bitwise_not(thresh)
    return gray,thresh


def easy_ocr_read(path):

	reader = easyocr.Reader(['en'], gpu = False)
	text = reader.readtext(path, detail = 0)#, text_threshold= 0.95)
	if len(text) > 0:
		print(text)
		s= ' '.join(text)
		print(s)
		return s #text[0]
	else:
		return ""
	# print(s)


# for f in files:
# 	print(p_vpn_g+f)
def easy_solve(filee):
	texttt=easy_ocr_read(p_vpn_g+filee)
	return texttt


def resolve_image():

	ts = str(calendar.timegm(time.gmtime()))

	try:
		# os.system("rm *.png")
		pass
	except Exception as e:
		print(e)

	# image_puzzel_button=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'adcopy-puzzle-image-image')))
	# location = image_puzzel_button.location
	# size = image_puzzel_button.size
	# w, h = size['width'], size['height']
	# hh=h-15
	
	left = 0
	right = 0

	top = -1
	bottom = -1

	print(" Corp ok")
	colored_image="1636172029screenshot.png"
	screen_colored_image=ts+'captchanew.png'

	imj=cv2.imread(colored_image)
	print(imj.shape)
	cropped_image=imj[325:470,529:824]
	cv2.imwrite("1s636172029screenshot.png",cropped_image)

	# driver.save_screenshot(colored_image)
	Spoon = Image.open(colored_image)

	# Spoon = Spoon.crop((left, top, right, bottom))
	Spoon.save("IMG/"+screen_colored_image)

	print('Puzzel')
	global text_final0
	# text_final=easyy.easy_solve(screen_colored_image)
	# text_final0=text_final
	# print(text_final0)
	# input('yy')
	time.sleep(3)
	# os.system("rm "+colored_image)
	# submit_result_text(driver)
	# read_message(driver,captcha_retries)

resolve_image()