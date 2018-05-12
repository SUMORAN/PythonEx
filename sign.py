from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import re
	
#写爬虫
def download():
	#获取用户输入的名称
	name = input.get()
	#去空格
	name = name.strip()
	if name == "":
		messagebox.showinfo('提示',"请输入有效的名字")
	else:
		#模拟网页发送请求
		data = {
			'word':name,
			'sizes':'60',
			'fonts':'jfcs.ttf',
			'fontcolor':'#000000'
		}
		startUrl = 'http://www.uustv.com/'
		result = requests.post(startUrl,data = data)
		result.encoding = 'utf-8'
		html = result.text
		print(html)


		#<div class="tu"><img src="tmp/152561514141256.gif"></div>
		#.*?匹配所有
		reg = '<div class="tu">.*?<img src="(.*?)"/></div>'
		imagePath = re.findall(reg,html)
		#print(imagePath)
		imageUrl = startUrl + imagePath[0]   #下标溢出？？？

		#获取图片内容
		response = requests.get(imageUrl).content

		with open('{}.gif'.format(name),'wb') as f:
			f.write(response)

		bm = ImageTk.PhotoImage(file = '{}.gif'.format(name))
		label_2 = Label(root,image = bm)
		label_2.bm = bm
		label_2.grid(row = 2, columnspan = 2)




#create a window
root = Tk()

#set title
root.title("签名设计")

#set window size  中间那个符号是小写的x字母
#root.geometry("600x300")
#set window's position on the desk
#下面是写死的绝对位置
#root.geometry("+400+200")

root.geometry("600x300+400+200")

#set label
label_1 = Label(root,text = "请输入名字",font = ('华文行楷',20),fg = 'red')
#布局，可以用grid， pack，place
#grid是网格式布局
label_1.grid(row = 0,column = 0)

#create input area
input = Entry(root,font = ("宋体",22),fg = 'black')
input.grid(row = 0,column = 1)

#create button
button = Button(root,text = "马上设计",font = ("华文行楷",20),command = download)
button['width'] = 15
button.grid(row = 1, column = 1,sticky = "E")   #E 和W分别是east和west

#print window//message loop
root.mainloop()


#从http://www.uustv.com/爬数据