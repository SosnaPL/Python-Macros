from hotkey import *
from pynput.keyboard import Key, Controller
import time
spider_exit = 0
back = 0
def move():
	print("move")
	while True:
		time.sleep(0.5)
		is_fighting()
		time.sleep(0.5)
		mouse_move(951, 554)
		time.sleep(0.3)
		click(949, 552)
def is_fighting():
	print("is_fighting")
	x = 50
	y = 330
	entranceX = 1078
	entranceY = 462
	color_is_fighting = pixel_get_color(x, y)
	color_entrance = "#4f4d42"
	while True:
		color_entrance_spider = pixel_get_color(entranceX, entranceY)
		if(color_entrance_spider == color_entrance):
			click(141, 373)
			print("rest")
			time.sleep(60)
			click(926, 504)
			time.sleep(2)
			click(870, 537)
			print("new instance")
			time.sleep(5)
			return True
		elif(color_is_fighting != "#986738"):
			time.sleep(1)
			fight()
		else:
			return
def clock():
	print("clock")
	global back
	global spider_exit
	x = 1303
	y = 395
	endX = 783
	endY = 697
	color_fight_off = "#bf4a1c"
	color_fight_on = "#004a00"
	color_end = "#d4b572"
	color_if_end = pixel_get_color(endX, endY)
	color_clock = pixel_get_color(x, y)
	if(color_clock == color_fight_on):
		while True:
			print("waiting for next round")
			time.sleep(1)
			color_clock = pixel_get_color(x, y)
			time.sleep(0.2)
			color_if_end = pixel_get_color(endX, endY)
			if(color_clock == color_fight_off):
				print("next round")
				return False
			elif(color_if_end == color_end and spider_exit == 1):
				print("back")
				spider_exit = 0
				time.sleep(1)
				click(1250, 733)
				time.sleep(2)
				powrot()
			elif(color_if_end == color_end and back == 1):
				print("back to exit after fight")
				back = 0
				time.sleep(1)
				click(1250, 733)
				time.sleep(2)
				powrot() 
				return True
			elif(color_if_end == color_end):
				print("exit")
				time.sleep(1)
				click(1250, 733)
				time.sleep(2)
				return True
def fight():
	print("fight")
	x = 1393 
	y = 818
	color_boss = pixel_get_color(x, y)
	if(color_boss == "#7d5800"):
		fight_boss()
	elif(color_boss != "#7d5800"):
		fight_spider()
	print("end_fight")
def fight_boss():
	global spider_exit
	spider_exit = 1
	while True:
		print("fight_boss")
		time.sleep(1)
		click(1242, 326)
		time.sleep(1)
		click(1303, 395)
		time.sleep(1)
		if clock(): 
			print("return_fight")
			return
		time.sleep(1)
		click(1242, 358)
		time.sleep(1)
		click(1303, 395)
		time.sleep(1)
		if clock(): 
			print("return_fight")
			return
		while True:
			time.sleep(1)
			click(1242, 419)
			time.sleep(1)
			click(1303, 395)
			time.sleep(1)
			if clock(): 
				print("return_fight")
				return
def fight_spider():
	while True:
		print("fight_spider")
		time.sleep(1)
		click(1242, 419)
		time.sleep(1)
		click(1303, 395)
		time.sleep(1)
		if clock(): 
			print("return_fight")
			return
def powrot():
	global back
	back = 1
	while True:
		print("back to entrance")
		time.sleep(0.5)
		if is_fighting(): return True
		time.sleep(0.5)
		mouse_move(1006, 709)
		time.sleep(0.3)
		click(1004, 707)
		time.sleep(0.3)
add_hotkey("s", move)
add_hotkey("p", exit)
run()