import webbrowser
import pyautogui
import time
import os
import subprocess

count_flag = 0

def access_meet(num):
	meet_url = [
	"https://meet.google.com/asdfasdf",
	"https://meet.google.com/qwerqwer"
	]
	print(pyautogui.size())
	os.startfile('chrome.exe')
	time.sleep(3)

	webbrowser.open(meet_url[num])
	time.sleep(5)

	# pyautogui.hotkey('ctrl', 'd')
	# time.sleep(1)
	pyautogui.hotkey('ctrl', 'e')

	button_location = pyautogui.locateOnScreen('access.png')
	time.sleep(1)
	print('[DEBUG] Find Button : ',button_location)
	pyautogui.click(button_location)

def end_process():
	os.system('taskkill /f /im chrome.exe')

def start(start_hour, start_min, index, total_hour):
	global count_flag

	while True:
		lecture_hour = int(time.strftime('%H'))
		lecture_min = int(time.strftime('%M'))
		if lecture_hour == start_hour and lecture_min == start_min and count_flag == index:
			print('Try to Access...')
			access_meet(count_flag)
			count_flag += 1;

		if lecture_hour == start_hour + total_hour:
			end_process()
			break

# start(start_hour, start_min, index, total_hour)
start(9,9,0,3)
start(13,00,1,3)
