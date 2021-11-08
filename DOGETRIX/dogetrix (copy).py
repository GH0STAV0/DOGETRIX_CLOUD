import mod_driver
import mod_vpn
import cnf_bvb
from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import requests
import requests , os
import io
from pydub import AudioSegment
import time , random
import emoji
import speech_recognition as sr
from PIL import Image
import calendar
import easyy
import cv2

from io import BytesIO



captcha_retries=0
local_pwd = os.path.dirname(os.path.realpath( __file__ ))
output_image_folder="/INPUT_IMG/"
modified_image_path=local_pwd+output_image_folder #'/IMG_MOD/'


balance_arry=[]

fresh=['1icdlc0kr@adhoc-yellow.com','ylabr3qv7@adhoc-purple.com','afztg11a8@adhoc-aqua.com','cuxduxhuc@adhoc-purple.com','icx8ao8f7@adhoc-white.com','urpyf7aui@adhoc-aqua.com','zutnjh7iw@adhoc-aqua.com','tvtfsgw70@adhoc-yellow.com','vjcx6ce8g@adhoc-purple.com','kkmx180sy@adhoc-aqua.com','j89pxhd8z@adhoc-yellow.com','sikhbkg6w@adhoc-red.com']


def get_captca(driver):
	number_fra = driver.find_elements_by_tag_name("img")
	print(len(number_fra))
	i=0
	for fr_m in number_fra:
		i=i+1
		png_test="Frame : "+str(i)+".png"
		print("Frame : "+str(i))
		fr_m.screenshot(png_test)

		user = fr_m.get_attribute("src")
		print(user)

def submit_result_text(driver):
	print('TRY OPEN COLLECT ',end=' ')
	reponse_captcha=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'adcopy_response')))
	time.sleep(2)
	print(text_final0)
	reponse_captcha.click()

	time.sleep(2)
	reponse_captcha.send_keys(text_final0)
	time.sleep(2)
	reponse_captcha.send_keys(Keys.ENTER)
	print('OK')
	time.sleep(6)
	# input('hyyyyyy')

#########################################################################################
def captcha_retries_count():
	global captcha_retries
	captcha_retries=1+captcha_retries
	print(str(captcha_retries))
	if captcha_retries > 15:
		captcha_retries=0
		init_fire()
		satrt_now()

def read_the_alert(driver, alert0):
	print('check alert   :  ',end=" ")
	print(alert0)
	if "Captcha" in alert0:
		# driver.refresh()
		print("CAPTCH ERROR ! :( ")
		# captcha_retries=captcha_retries+1
		captcha_retries_count()
		print("retries : "+str(captcha_retries))
		time.sleep(2)
		input("screeen")
		# corresolve_image(driver)



		collect_fun(driver)
		
	if "Staking interest received:" in alert0:
		close_after_succe(driver)
		
	


##################################################################################################

def read_message(driver,captcha_retries):
	#alert alert-success alert-dismissible text-center
	try:
		# alert_tip=driver.find_element_by_css_selector('.alert.alert-success.alert-dismissible.text-center')
		open_login_button=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible.text-center')))
		items = driver.execute_script("return [...document.querySelectorAll('div.alert.alert-success.alert-dismissible.text-center')].map(item => item.innerText)")
		print(items)
		message_alert=items[2].replace('×\n','')
		read_the_alert(driver ,message_alert)
		
	except Exception as e:
		print(str(e))
		pass

	try:
		alert_tip=driver.find_element_by_css_selector('.alert.alert-danger.alert-dismissible.text-center')
		time.sleep(3)
		items = driver.execute_script("return [...document.querySelectorAll('div.alert.alert-danger.alert-dismissible.text-center')].map(item => item.innerText)")
		message_alert=items[2].replace('×\n','')
		read_the_alert(driver ,message_alert)

	except Exception as e:
		print(e)
	
	


def resolve_image(driver):

	ts = str(calendar.timegm(time.gmtime()))

	try:
		os.system("rm *.png")
		pass
	except Exception as e:
		print(e)








#adcopy-outer modal-content claim
	
	
	# number_fra=driver.find_elements_by_tag_name("iframe")
	# print(str(len(number_fra)))
	# input('tt')
	image_puzzel_button=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'adcopy-puzzle-image')))
	
	location = image_puzzel_button.location
	print(str(location))
	size = image_puzzel_button.size
	w, h = size['width'], size['height']



	# hh=h-15
	print(str(size))
	image_puzzel_button.screenshot('screen_shot_element.png')
	png = driver.get_screenshot_as_png()
	im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']
	# im = im.crop((left, top, right, bottom)) # defines crop points
	im.save('screen_shot_Totale.png')
	input("pilllll")






	y=location['y']
	x=location['x']
	print(int(x))
	ww=int(w)
	hh=int(h)



	
	# left = location['x']
	# top = location['y'] + 80
	# right = location['x'] + size['width']
	# bottom = location['y']+ hh + 80
	print(" Corp ok")
	colored_image=ts+"screenshot.png"
	screen_colored_image=ts+'captchanew.png'

	driver.save_screenshot(colored_image)
	time.sleep(3)
	Spoon = Image.open(colored_image)


	in_hh= y-hh
	in_ww=x-ww
	print(int(in_hh))

	# imj=cv2.imread(colored_image)
	# (x,y,w,h) = cv2.selectROI(imj)
	# input("")
	# left = location['x']
	# right = in_ww

	# top = location['y'] - 180
	# bottom = in_hh


	# left = location['x']
	# top = location['y'] - 50
	# right = location['x'] + size['width'] # in_ww #
	# bottom = location['y']+ hh - 50 #in_hh#
	left = location['x']
	top = location['y'] - 290
	right = location['x'] + size['width']
	bottom = location['y']+ hh - 310


	Spoon = Spoon.crop((left, top, right, bottom))
	# Spoon = Spoon.crop((10, 10, 10, 10))
	Spoon.save("IMG/"+screen_colored_image)
	time.sleep(3)


	
	# cropped_image=imj[y:y+h, x:630]
	# cv2.imwrite("IMG/"+screen_colored_image ,cropped_image)

	print('Puzzel')
	global text_final0
	text_final=easyy.easy_solve(screen_colored_image)
	text_final0=text_final
	# print(text_final0)
	# input('yy')
	time.sleep(3)
	# os.system("rm "+colored_image)
	submit_result_text(driver)
	read_message(driver,captcha_retries)



def get_earned_ready(driver):
	time.sleep(6)
	earned_amount=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'faucet')))
	print(earned_amount.text)
	earned_amount=int (earned_amount.text)
	if earned_amount < 2 :
		until_time= 20 - earned_amount
		time.sleep(until_time*60)




def collect_fun(driver):
	try:
		driver.refresh()
		# faucet
		print('DOGE AMOUNT : ',end=' ')
		get_earned_ready(driver)




		open_login_button=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.enter-btn-wrapper')))
		time.sleep(2)
		open_login_button.click()
		time.sleep(2)
		print('OK ')
		resolve_image(driver)
	except Exception as e:
		print(str(e))


###########################  GET THE BALCE AND ID ###############################
def check_lo_in(driver):
	get_the_id=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'pubkey')))
	#global_balance_treasure
	get_the_balance=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'global_balance_treasure')))

	print("ID PUBLICKEY : "+get_the_id.text)
	print("Balance : "+get_the_balance.text)
####################################################################################################



def ltc_login(width,height):

	try:
		# mod_vpn.fnc_vpn ()

		serv,ops=mod_driver.build_driver(width,height)
		driver = webdriver.Firefox(service=serv, options=ops)
		extension_path=cnf_bvb.extension_path
		extension_path_ublock=cnf_bvb.extension_path_ublock
		driver.install_addon(extension_path, True)
		driver.install_addon(extension_path_ublock, True)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.get("https://dogetrix.com/")
		print("GO TO WEBSITE")
		#cookie-btn
		coockie_accept_button=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'cookie-btn')))
		coockie_accept_button.click()
		print("ACCEPT COOCKIE")

		
		try:
			print('TRY OPEN LOGIN')
			open_login_button=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.enter-btn-wrapper')))
			time.sleep(2)
			open_login_button.click()
			print("OPEN LOGIN")
			#signin-email
			email_accept_button=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'signin-email')))
			print('INPUT CREDENTIAL')
			time.sleep(2)
			email_accept_button.click()
			time.sleep(2)
			email_accept_button.send_keys("GH0STAV0@protonmail.com")
			time.sleep(2)
			email_accept_button.send_keys(Keys.TAB,"baba123A*")
			# get_captca(driver)
			capatch(driver)
			check_lo_in(driver)
			#pubkey
			# input('Captcha resolved')
			time.sleep(5)
			#enter-btn-wrapper
			####################################
			collect_fun(driver)
			satrt_now()
			
			####################################


			# input('INPUT CREDENTIAL')
			# address_dodge_button.send_keys("D5vKiS3qhtW2zU9Buak1LdKawT7p95jpCx")
			# time.sleep(2)
			# address_dodge_button.send_keys(Keys.ENTER)
			# print("ADDRESS ENTRED ")
			# # input('D5vKiS3qhtW2zU9Buak1LdKawT7p95jpCx')
			# time.sleep(8)
		except Exception as e:
			print(str(e))
			collect_fun(driver)
			pass


		# try:
		# 	#print(old_amount)
		# 	address_dodge_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-success.btn-lg')))
		# 	time.sleep(2)
		# 	print("ADDRESS ENTRED ")
		# 	# address_dodge_button.send_keys("D5vKiS3qhtW2zU9Buak1LdKawT7p95jpCx")
		# 	# time.sleep(2)
		# 	address_dodge_button.send_keys(Keys.ENTER)
		# 	print("ADDRESS ENTRED ")
			
		# except Exception as e:
		# 	print(str(e))
		# 	pass

		try:
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4.2);window.scrollTo(0, document.body.scrollHeight/4.5);")
			time.sleep(5)
			address_dodge_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.g-recaptcha')))
			address_dodge_button.send_keys(Keys.TAB)
			number_fra=driver.find_elements_by_tag_name("iframe")
			print(str(len(number_fra)))#find_elements_by_class_name
			time.sleep(3)
			capatch(driver)
			# driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
			# print("switch")
			# time.sleep(3)
			# recaptcha_ok=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rc-anchor-container"]/div[3]/div[1]/div/div')))
			# print(" |")
			# recaptcha_ok.click()
			time.sleep(2)
			# y=0
			# for link in number_fra:
			# 	download_link = link.get_attribute('title')
			# 	print(download_link+"   "+str(y))
			# 	y=y+1btn btn-success

			#time.sleep(1)
		except Exception as e:
			print(str(e))

		init_fire()
		pass
	except Exception as e:
		print(str(e))
		init_fire()
		satrt_now()


def daily_offer(driver):
	global bonnus_array
	bonnus_array=[]
	print("check daily offers")
	daily_button=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a')))	
	time.sleep(2)
	daily_button.click()
	time.sleep(3)
	number_links = driver.find_elements_by_tag_name("a")
	#print(str(number_links))
	for link in number_links:
		download_link = link.get_attribute('href')
		print(download_link)
		if "bonus/" in download_link:
			bonnus_array.append(download_link)
		else:
			pass
	print(bonnus_array)
	for ik in bonnus_array:
		print(ik)
		driver.get(ik)
		time.sleep(3)
		visit_button=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div[2]/div[3]/div/div[2]/div[3]/a')))
		print('ok')
		visit_button.click()
		time.sleep(3)
		close_func(driver)
		time.sleep(2)


def audio_fonction(download_link):
	#data = open('1.mp3', 'rb').read()
	print("ok download_link")
	request = requests.get(download_link)
	audio_file = io.BytesIO(request.content)
	sound = AudioSegment.from_mp3(audio_file)
	dst = "test1.wav"
	sound.export(dst, format="wav")
	r = sr.Recognizer()
	with sr.WavFile("test1.wav") as source:
		audio = r.record(source)
	
	audio_output=r.recognize_google(audio)
	print("Transcription: " + audio_output)
	return audio_output


def close_func(driver):
	global new_amount
	driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
	print("Length of Driver = ", driver_len)
	if driver_len > 1:
		for i in range(driver_len - 1, 0, -1):
			driver.switch_to.window(driver.window_handles[i])
			time.sleep(5)
			driver.close()
			print("Closed Tab No. ", i)
		driver.switch_to.window(driver.window_handles[0])
	else:
		print("Found only Single tab.")
	time.sleep(5)
	print('check balance ')
	getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usd_balance"]')))
	#global new_amount
	new_amount= getLink_button.text
	print(new_amount)
	driver.delete_all_cookies()

def capatch(driver):
	print("\n # STARTING CAPATCHA  ")
	
	global new_amount
	try:
		# without_captcha_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'without_captcha_button')))
		# without_captcha_button.send_keys(Keys.TAB )
		# time.sleep(2)
		# main_button=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'without_captcha_button')))
		# time.sleep(5)
		# number_fra=driver.find_elements_by_tag_name("iframe")
		# print(str(len(number_fra)))#find_elements_by_class_name
		# time.sleep(1)
		# #input('check capatch')
		time.sleep(2)
		driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[1])
		# print("switch")
		time.sleep(2)
		recaptcha_ok=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rc-anchor-container"]/div[3]/div[1]/div/div')))
		# print(" |")
		# recaptcha_ok.perform()
		# webdriver.ActionChains(driver).move_to_element(recaptcha_ok).click(recaptcha_ok).perform()
		time.sleep(2)

		# recaptcha_ok.click()
		webdriver.ActionChains(driver).move_to_element(recaptcha_ok).click(recaptcha_ok).perform()

		time.sleep(2)
	except Exception as d:
		print(str(d))
		satrt_now()

	try:
		donne_ok=WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
		print('lucky captcha')
		driver.switch_to.default_content()
		time.sleep(3)
		success_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-success')))
		time.sleep(2)
		success_button.click()
		print('lucky Cleaim')
		time.sleep(2)

		close_func(driver)
		end_of_task()
		#input('lucky captcha')
		# balance_arry.append(new_amount)	
	except Exception as e:
		print("no captch lucky")
		# satrt_now()

	# print("A")
	try:
		driver.switch_to.default_content()
		time.sleep(5)
		driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[3])
		time.sleep(2)
		recaptcha_ok=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'recaptcha-audio-button')))
		recaptcha_ok.click()
		time.sleep(3)
		eto_firstName=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'audio-source')))
		download_link = eto_firstName.get_attribute('src')
		audio_output= audio_fonction(download_link)
		time.sleep(3)
		text_cap=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'audio-response')))
		text_cap.send_keys(audio_output)
		time.sleep(2)
		text_cap.send_keys(Keys.ENTER)
		time.sleep(2)
		driver.switch_to.default_content()
		success_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'action-signin')))
		time.sleep(2)
		success_button.click()

		print('Captcha resolved')
		#action-signin
		time.sleep(3)
	except Exception as e:
		print(str(e))



def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("rm -rf __pycache__/")
		#print("############################################################")
	except  Exception as e :
		print(" NO  some_Error init_fire")
		print(str(e))

def end_of_task():
	try:
		print(" OK !!!"+old_amount+" -> "+new_amount)
		slack_message.append(old_amount+" -> "+new_amount)
	except Exception as e:
		print(str(e))
	init_fire()

def slack_fonction(s):
	cmdd="curl -X POST -H 'Content-type: application/json' --data "+"'"+'{"text":"'+s+'"}'+"'"+" https://hooks.slack.com/services/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"
	#print (cmdd)
	#os.system(cmdd)


def satrt_now():

	os.system("rm -rf __pycache__/")
	os.system("rm -rf /tmp/*")

	try:
		init_fire()
		mod_vpn.fnc_vpn ()
		width , height =cnf_bvb.resolution_func()
		ltc_login(width,height)

	except Exception as e:
		print(e)
		satrt_now()
#######################################################################
def close_after_succe(driver)	:

	print("SUCCED GO TO SLEEP")
	# print("SUCCED : ) ")
	driver.close()
	init_fire()
	time.sleep(1200)
	satrt_now()


#####################################################################


satrt_now()
################################-----------------------------

# for i in fresh:
# 	init_fire()
# 	print(i)
# 	width , height =cnf_bvb.resolution_func()
# 	# display = Display(visible=1, size=(width,height)).start()
# 	# slack_message.append(i)
# 	global slack_message
# 	slack_message=[]
# 	slack_message.append(i)
# 	ltc_login(i,width,height)
# 	s= ' # '.join(slack_message)
# 	slack_fonction(s)
# 	display.stop()
# 	os.system("rm -rf __pycache__/")
# 2021-11-04 17:57:18 WARNING: Compression for receiving enabled. Compression has been used in the past to break encryption. Sent packets are not compressed unless "allow-compression yes" is also set.
# STARTING VPN [NCVPN-MD-Chisinau-UDP.ovpn]OK !!!!!
#  [ 185.163.46.157 ] [Europe/Chisinau ] [ 47.2556,28.3099 ]
# VPN STATUS = OK || NCVPN-MD-Chisinau-UDP.ovpn||185.163.46.157||Europe/Chisinau
# BUILDING PROFILE DRIVER  ...... [ 53.0.2 ] Ok  ✅ 👽
# Mozilla/5.0 (Linux; U; Android 4.4.2; pl-pl; SM-T210 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30
# GO TO WEBSITE
