from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import re
import os
import multiprocessing 

try:
	driver = webdriver.Firefox()
except:
	driver = webdriver.Chrome(executable_path='chromedriver.exe')
dem = len(os.listdir('Data_Web'))
temp_urls = []
with open('log_url.txt','r') as f:
	temp_urls=f.read().split('\n')
print(temp_urls)
# Take File
def take_file():
	pass


#science.nasa.gov
def download_data_universe(url):
	driver.get(url)
	content = ""
	# Finding content.
	content_infomations = driver.find_elements(By.CLASS_NAME,"BlockWrapper")
	print("Tien hanh in ra thong tin du lieu:")
	for i in content_infomations[:-2]:
		info = i.text
		content += info + '\n'
		if(len(info.split())<10):
			print("-")
		print(info)
	
	# Tien hanh thuc thi doan ma tiep theo
	urls = []
	click_infomations = driver.find_elements(By.CLASS_NAME,"link-external-false")
	for i in click_infomations:
		print("Checking URL")
		url = i.get_attribute('href')
		print(url)
		info_temp = re.search('https://science.nasa.gov/[a-zA-z].*/.*/[a-zA-z].*',url)
		print(info_temp)
		try:
			urls.append(info_temp.string)
		except:
			pass
	print(urls)

	# The Title of Content.
	temp_string = f'{dem}_'+content_infomations[0].text.split('\n')[1]
	blacklist = [':',',','.','\'',',','.','/','?','<','>','}','{','[',']','\\','\/','!','~','`','@','#','$','%','^','&','*','(',')','-','+','=']
	for i in blacklist:
		temp_string=temp_string.replace(i,'')
	title = 'Data_Web/'+temp_string+'.txt'
	title = title.replace(' ','_')
	print(title)
	print("The Title of Content")
	with open(title,'a') as f:
		f.write(content)

	with open('log_url.txt','a') as f:
		f.write(url+'\n')
	return urls



#www.nasa.gov
def download_data_missions(url):
	with open('log_url.txt','a') as f:
		f.write(url+'\n')

	driver.get(url)
	content = ""
	content_infomations = driver.find_elements(By.CLASS_NAME,"display-48")
	#for content_temp in content_infomations:
	#	content += content_temp.text +"\n"
	# Finding content.
	content_infomations += driver.find_elements(By.TAG_NAME,"p")
	print("Tien hanh in ra thong tin du lieu:")
	for i in content_infomations:
		info = i.text
		content += info + '\n'
		if(len(info.split())<10):
			print("-")
		print(info)
	
	# Tien hanh thuc thi doan ma tiep theo
	urls = []
	click_infomations = driver.find_elements(By.CLASS_NAME,"color-carbon-black")
	for i in click_infomations:
		print("Checking URL")
		url = i.get_attribute('href')
		print(url)
		info_temp = re.search('https://science.nasa.gov/[a-zA-z].*/.*/[a-zA-z].*',url)
		print(info_temp)
		try:
			urls.append(info_temp.string)
		except:
			pass
	print(urls)

	# The Title of Content.
	temp_string = f'{dem}_'+content_infomations[0].text.split('\n')[0]
	blacklist = [':',',','.','\'',',','.','/','?','<','>','}','{','[',']','\\','\/','!','~','`','@','#','$','%','^','&','*','(',')','-','+','=']
	for i in blacklist:
		temp_string=temp_string.replace(i,'')
	title = 'Data_Web/'+temp_string+'.txt'
	title = title.replace(' ','_')
	print(title)
	print("The Title of Content")
	with open(title,'a') as f:
		f.write(content)
	return urls


def multidownload(url):
	global dem
	urls = []
	dem+=1
	print(f"Noi dung thu {dem}")
	if ("science.nasa.gov" in url):
		urls=download_data_universe(url)
	elif ("www.nasa.gov" in url):
		urls=download_data_missions(url)
	else:
		pass
	return urls

if __name__ == '__main__':
	dem+=1
	urls = multidownload('https://science.nasa.gov/missions/xrism/nasa-jaxas-xrism-mission-captures-unmatched-data-with-just-36-pixels/')
	print("Thanh Cong")
	os.system("pause")