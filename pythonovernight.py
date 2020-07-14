import pyautogui
import time
pos = list(pyautogui.position())

while True:
	pyautogui.click(pos[0], pos[1])
	time.sleep(120)
	pyautogui.click(pos[0], pos[1])
	time.sleep(3600)
	x += 1
	print(x)
