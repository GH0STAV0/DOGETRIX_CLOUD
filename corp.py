# from selenium import webdriver
from PIL import Image

# SpoonFeeder = webdriver.Chrome()
# SpoonFeeder.get('http://pingler.com/')
# element = SpoonFeeder.find_element_by_id('adcopy-puzzle-image')
# SpoonFeeder.execute_script("return arguments[0].scrollIntoView();", element)
# SpoonFeeder.save_screenshot('screenshot.png')
# SpoonFeeder.quit()
Spoon = Image.open('screenshot.png')
left = 530
top = 375
right = 820
bottom = 505
Spoon = Spoon.crop((left, top, right, bottom))
Spoon.save('screenshotnew.png')