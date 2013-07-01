# -*- coding: utf-8-*-
#	Author：	Wenchao Hu		
#	Email：		zjuhwc@gmail.com

import win32com
from win32com.client import Dispatch, constants

#模板文件保存路径
template_path = 'C:\Users\yely\Desktop\easy_exam2\yanjiang.doc'
#另存文件路径
store_path = 'C:\Users\yely\Desktop\easy_exam2\out\\'
#模板中需要被替换的文本。	u''中的u表示unicode字符，用于中文支持
NewStr = u'徐家运'

#启动word
w = win32com.client.Dispatch('Word.Application')
# 或者使用下面的方法，使用启动独立的进程：
# w = win32com.client.DispatchEx('Word.Application')

# 后台运行，不显示，不警告
w.Visible = 0
w.DisplayAlerts = 0
# 打开新的文件
doc = w.Documents.Open( FileName = template_path )
# worddoc = w.Documents.Add() # 创建新的文档

# 正文文字替换
w.Selection.Find.ClearFormatting()
w.Selection.Find.Replacement.ClearFormatting()

#名单
lst = [u'张莉', u'张海娟', u'杨丽娇']

#迭代替换名字，并以名字为名另存文件
for i in lst:
    OldStr, NewStr = NewStr, i
    w.Selection.Find.Execute(OldStr, False, False, False, False, False, True, 1, True, NewStr, 2)
    doc.SaveAs(store_path + i +'.doc')
	#doc.PrintOut()		打印API，未测试

doc.Close()
w.Documents.Close()
w.Quit()
