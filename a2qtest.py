
import easyy
import os 

# import pandas as pd
# from Levenshtein import distance
# from tqdm.notebook import tqdm

pwd = os.path.dirname(os.path.realpath( __file__ ))
p_vpn_g = pwd+'/IMG/'
# os.listdir(p_vpn_g)
files = easyy.files
# print(files)
# reader = easyocr.Reader(['en'], gpu = False)
#textract = boto3.client('textract')


# def easy_ocr_read(path):

# 	reader = easyocr.Reader(['en'], gpu = False)
# 	text = reader.readtext(path, detail = 0)
# 	if len(text) > 0:
# 		print(text)
# 		s= ' # '.join(text)
# 		print(s)
# 		return s #text[0]
# 	else:
# 		return ""
	# print(s)

for f in files:
	full_path=p_vpn_g+f
	print(full_path)
	# easyy.img_process(full_path)
	easyy.easy_solve(f)


