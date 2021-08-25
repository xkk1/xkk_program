from tkinter import *
from random import sample
from os.path import exists
from tkinter import messagebox

file = 'Students.txt'
names = []
name = ""
havenames = []
lj = 0


def OK():
    global names
    global havenames
    file = v1.get()
    if not exists(file):
        print(exists(file))
        messagebox.showerror(title = '未找到文件',
                            message='文件“%s”不存在！'%file)
    else:
        """if exists(wjj+"/"+wjj):# 如果数据文件夹在
            return True# 返回真
        elif exists(wjj+".dat"):# 如果数据文件存在
            decdat(wjj)# 直接解压数据文件
            return True
        elif exists(wjj):# 如果数据文件夹存在
            f = open(wjj+"/"+wjj, "w")
            f.write(firststr)
            f.close()
            return False# 返回假
        else:
            mkdir(wjj)
            f = open(wjj+"/"+wjj, "w")
            f.write(firststr)
            f.close()
            return False"""
        """
        f = open(NamesFile,"w")
        f.write("mdzz")
        f.close()"""
        f = open(file,"r")
        names = f.readlines()
        f.close()
        for i in range(len(names)):# 删掉每行多余的回车
            if i != len(names) - 1:
                names[i] = names[i][:-1]
            else:
                if names[i][-1] == "\n":
                    names[i] = names[i][:-1]
        for i in range(len(names)):# 删掉多余的空行（改良版）
            while i < len(names) and names[i] == "":
                del names[i]
        """
        def del_():# 删掉多余的空行
            for i in range(len(names)):
                if names[i] == "":
                    del names[i]
                    del_()
                    break
        del_()
        """
        print(names)
        for j in names:
            print(j)
            
        v2.set("当前姓名总数："+str(len(names)))
        v3.set("剩余姓名数："+str(len(names)))
        havenames = []

def help():
    #showinto （信息提示）
    # 弹出对话框
    messagebox.showinfo(title = '帮助',message="QQ:3434623263")
    # 返回值为：ok

def FW():# 复位
    global havenames
    v3.set("剩余姓名数："+str(len(names)))
    havenames = []

def sjdm():
    global name
    global havenames
    global lj
    if len(names) == 0:
        messagebox.showerror(title = '没有指定姓名文件',
                            message='没有指定姓名文件！\n请先指明姓名文件！')
    else:
        if not v4.get():# 判断是否选上不重复点名
            # print(v4.get(),"F")
            name = sample(names,1)[0]# 随机抽取一个名字
            v5.set(name)
            lj += 1
            v6.set("累计抽取人数："+str(lj))
        else:
            #print(v4.get(),"???")
            name = sample(names,1)[0]# 随机抽取一个名字
            while name in havenames:
                name = sample(names,1)[0]# 随机抽取一个名字
            v5.set(name)
            lj += 1
            v6.set("累计抽取人数："+str(lj))
            havenames += [name]
            if len(names)-len(havenames) == 0:
                havenames = []
            v3.set("剩余姓名数："+str(len(names)-len(havenames)))
            print(havenames)

def ql():
    global lj
    lj = 0
    v6.set("累计抽取人数："+str(lj))


if __name__ == "__main__":
    window=Tk()
    window.title("随机点名V1.0.0")
    # window.resizable(0,0)# 禁止调节窗口大小
    
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = IntVar()
    v5 = StringVar()
    v6 = StringVar()

    v1.set("Students.txt")
    v2.set("当前姓名总数：0")
    v3.set("剩余姓名数：0")
    v5.set("")
    v6.set("累计抽取人数：0")

    win = Frame(window)

    f1 = Frame(win)
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    e1 = Entry(f1,textvariable=v1,width=25
               ).pack(side=LEFT)
    bOK = Button(f1,
               text="确定",
               font=('宋体', 12),         # 字体和字体大小
               command=OK
               ).pack(side=RIGHT)

    f1.pack(fill=X)

    f2 = Frame(win)
    l2 = Label(f2, 
        textvariable=v2,
        # text="当前姓名总数：0",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    bhelp = Button(f2,
               text="帮助",
               font=('宋体', 12),         # 字体和字体大小
               command=help
               ).pack(side=LEFT)
    bFW = Button(f2,
               text="↓复位↓",
               font=('宋体', 12),         # 字体和字体大小
               command=FW
               ).pack(side=RIGHT)
    f2.pack(fill=X)

    f3 = Frame(win)
    ccf = Checkbutton(f3, 
                       text='不重复点名', 
                       variable=v4, 
                       onvalue=1, 
                       offvalue=0
                       #command=print_selection
                       ).pack(side=LEFT)
    l3 = Label(f3, 
        textvariable=v3,
        text="剩余姓名数：0",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=RIGHT)    # 固定窗口位置
    f3.pack(fill=X)

    f4 = Frame(win)
    bsjdm = Button(f4,
               text="随机\n点名",
               font=('宋体', 20),         # 字体和字体大小
               command=sjdm
               ).pack(side=LEFT)
    l4 = Label(f4, 
        text="被  \n点→\n人→\n名  ",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    lname = Label(f4, 
        textvariable=v5,
        #text="王小明",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('黑体', 40),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    f4.pack(fill=X)

    f5 = Frame(win)
    bql = Button(f5,
               text="清零→",
               font=('宋体', 8),         # 字体和字体大小
               command=ql
               ).pack(side=LEFT)
    l5 = Label(f5, 
        textvariable=v6,
        #text="累计抽取人数：0",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 8),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    bjia = Button(f5,
               text="-",
               font=('宋体', 8)         # 字体和字体大小
               #command=cupy
               ).pack(side=RIGHT)
    bjian = Button(f5,
               text="+",
               font=('宋体', 8)         # 字体和字体大小
               #command=cupy
               ).pack(side=RIGHT)
    lzh = Label(f5, 
        text="字号：",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 8),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=RIGHT)    # 固定窗口位置
    f5.pack(fill=X)

    win.pack()
    """

    f = Frame(window)

    t = Text(f,
             width=33,
             height=12
               )
    t.pack()

    f.pack(side=LEFT)
    """
    window.mainloop()           #循环消息，让窗口活起来
