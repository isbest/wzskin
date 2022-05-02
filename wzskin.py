# encoding: UTF-8
import requests
import json
from tkinter import *
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import threading
from tkinter import messagebox
#from PIL import Image,ImageTk

global control
control = 1

#从官网下载json文件到目录下
urlJson = 'http://pvp.qq.com/web201605/js/herolist.json'#这个是网址
JsonFile = requests.get(urlJson).content#这个就是从网上获取文件的意思
JsonFile = JsonFile.decode('utf-8-sig')#把文件转换一下编码，转成我们可以直接读取的格式
with open('herolist.json','wb') as f:#保存文件
    f.write(JsonFile.encode())
    #f.write(JsonFile)


# 读取json文件
with open('herolist.json', 'r', encoding='utf-8') as ff:  # 读取json文件
    jsonFile = json.load(ff)

def download():#下载皮肤
    heroname=ent.get()#获取输入框里面的英雄名字
    skiname=numberChosen.get()#获取下拉列表里面的皮肤名字
    for m in range(len(jsonFile)):
        ename = jsonFile[m]['ename']#英雄代码
        cname = jsonFile[m]['cname']#英雄中文名
        print(cname)
        skinName = jsonFile[m]['skin_name'].split('|')#皮肤名字
        skinNumber = len(skinName)#获取皮肤数量
        if cname == heroname:#查找英雄
            for bigskin in range(1, skinNumber + 1):
                if skiname == skinName[bigskin - 1]:#查找皮肤
                    #生成皮肤的地址
                    urlPicture = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(bigskin) + '.jpg'
                    #    获取图片信息  图片都是二进制  content就是获取二级制信息
                    picture = requests.get(urlPicture).content
                    # 保存信息 保存图片
                    filename = tkinter.filedialog.asksaveasfilename(filetypes = [('','.jpg')],initialfile = skiname)#打开一个保存图片地址的框框
                    if filename:
                        with open(filename + '.jpg', 'wb') as f:
                            f.write(picture)
                        messagebox.showinfo(title='提示', message='下载成功！')
                    break
            break

def downloadskin():#下载隐藏皮肤
    heroname=ent.get()#获取输入框里面的英雄名字
    #skiname=numberChosen.get()
    for m in range(len(jsonFile)):
        ename = jsonFile[m]['ename']#英雄代码
        cname = jsonFile[m]['cname']#英雄中文名
        print(cname)
        skinName = jsonFile[m]['skin_name'].split('|')#皮肤名字
        skinNumber = len(skinName)#获取皮肤数量
        if cname == heroname:#查找英雄
            bigskin =skinNumber + 1
            urlPicture = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(bigskin) + '.jpg'#生成图片地址
            #    获取图片信息  图片都是二进制  content就是获取二级制信息
            getpicture = requests.get(urlPicture)
            picture = getpicture.content
            picturer = getpicture.status_code
            if picturer == 404:
                messagebox.showinfo(title='提示', message='没有找到隐藏皮肤！')
                break
            else :
                # 保存信息 保存图片
                hideskin=str(cname)+'隐藏皮肤'
                filename = tkinter.filedialog.asksaveasfilename(filetypes=[('', '.jpg')], initialfile=hideskin)
                if filename:
                    with open(filename + '.jpg', 'wb') as f:
                        f.write(picture)
                    messagebox.showinfo(title='提示', message='下载成功！')
                    break

def picturesee():
    heroname=ent.get()#获取输入框里面的英雄名字
    skiname=numberChosen.get()#获取下拉列表里面的皮肤名字
    for m in range(len(jsonFile)):
        ename = jsonFile[m]['ename']#英雄代码
        cname = jsonFile[m]['cname']#英雄中文名
        print(cname)
        skinName = jsonFile[m]['skin_name'].split('|')#皮肤名字
        skinNumber = len(skinName)#获取皮肤数量
        if cname == heroname:#查找英雄
            for bigskin in range(1, skinNumber + 1):
                if skiname == skinName[bigskin - 1]:#查找皮肤
                    #生成皮肤的地址
                    urlPicture = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(ename) + '/' + str(ename) + '-bigskin-' + str(bigskin) + '.jpg'
                    #    获取图片信息  图片都是二进制  content就是获取二级制信息
                    picture = requests.get(urlPicture).content
                    # 保存信息 保存图片
                    im=picture
                    (x,y)=im.size
                    x_s = 180
                    y_s = y*x_s // x
                    imag = im.resize((x_s,y_s),Image.ANTIALIAS)
                    img=ImageTk.PhotoImage(imag)
                    imLabel=tk.Label(root,image=img).grid(column = 1,row = 0,rowspan = 3)
                    break
            break
   


def fun_timer():#刷新下拉列表用的
    #picturesee()
    global timer#定义全局变量timer
    print('Hello Timer!')#这一行是用来测试下拉列表是否正常运行的
    k=len(jsonFile)#获取英雄数量
    for m in range(0,k):
        s=0
        cname = jsonFile[m]['cname']#获取英雄的中文名字
        skinName = jsonFile[m]['skin_name'].split('|')#皮肤名字
        skinNumber = len(skinName)
        if cname ==ent.get():#在json文件里面查找你在gui界面里面输入的英雄名字相匹配的皮肤
            s=1
            numberChosen['values'] = skinName#更新下拉列表
            for bigskin in range(1, skinNumber + 1):
                skiname=numberChosen.get()
                if skiname == skinName[bigskin - 1]:#查找皮肤
                    print(skiname)
            break
    if s==0:
        numberChosen['values'] = ('英雄不存在！')#如果查找完了还没找到，那么就在下拉列表里显示英雄不存在
    if control:
        timer = threading.Timer(0.5, fun_timer)#新建一个进程，让刷新下拉列表的进程和主函数分开走
        timer.start()

#创建一个窗口
root = Tk()
root.title('英雄皮肤下载')
root.geometry('250x120+1000+500')

#标题
ttk.Label(root, text="输入英雄名字：",width=12).grid()      # 设置其在界面中出现的位置  column代表列   row 代表行
#ttk.Label(root, text="列表中没有？", width=12).grid(column = 2,row = 2)  # 设置其在界面中出现的位置  column代表列   row 代表行

#输入框
ent = Entry(root,width=14)
ent.grid()
ent.delete(0,END)

#下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(root, width=12, textvariable=number)
#numberChosen['values'] = (0,1,2,3)  # 设置下拉列表的值
numberChosen.grid()  # 设置其在界面中出现的位置  column代表列   row 代表行

#按钮
btn_download = Button(root,text=' 下 载 ',command=download)
btn_download.grid(column = 0,row = 4)

btn_download = Button(root,text=' 下载隐藏皮肤 ',command=downloadskin)
btn_download.grid(column = 1,row = 4)

timer = threading.Timer(0.5, fun_timer)
timer.start()

root.mainloop()

control = 0
timer.cancel()
print("关闭")
