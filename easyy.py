
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
import easyocr
from PIL import Image
# import boto3
import os , cv2

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
	text = reader.readtext(path, detail = 0)#, text_threshold= 0.85)
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


