# -*- coding: utf8 -*-
from Tkinter import *   #引入Tkinter工具包
import random
import copy

lst = [u'石晓敏', u'刘明莹', u'赵俊阳', u'杨文金', u'张银鑫', u'费正美', u'石彦霞', u'唐俊勇', u'杨苏润', u'杨向婷', u'胡思凡', u'赵俊伟', u'龚梦蝶', u'陈鹏宇', u'刘振颖', u'唐铠露', u'陈玲秀', u'何宇婷', u'高丽仙', u'张梦娇', u'杨宇', u'高开美', u'杨宗远', u'赵欣垚', u'杨灿', u'杨陈维', u'陈晓凤', u'吕艳兵', u'赵树楠', u'李鑫源', u'廖志龙', u'董雪融', u'赵娇蓉', u'陈雅燃', u'罗尚慈', u'邓金羊', u'王亚艳', u'刘明广', u'娄宏杰']
temp = copy.deepcopy(lst)

def show_name():
	if len(temp) != 0:
		name = random.choice(temp)
		label.config(text=name)
		temp.remove(name)
		label2.config(text=str(len(temp)))
	else:
		reset()

def reset():
	global temp
	temp = copy.deepcopy(lst)
	label.config(text='点名')
	label2.config(text=str(len(temp)))


win = Tk()  #定义一个窗体
win.title('自动点名机')    #定义窗体标题
win.geometry('900x350')     #定义窗体的大小，是400X200像素

label = Label(win, text="点名", font=('systemfixed',200,'bold'))
label.pack()

label2 = Label(win, text=str(len(temp)))
label2.pack()

btn = Button(win, text='点名', command=show_name)
btn.pack() #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)

btn2 = Button(win, text='重置', command=reset)
btn2.pack() 

mainloop() #进入主循环，程序运行
