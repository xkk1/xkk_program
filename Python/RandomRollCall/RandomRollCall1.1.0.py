from tkinter import *# 图形界面

file = 'Students.txt'
names = []# 读取的姓名
name = ""# 当前抽取的姓名
havenames = []
lj = 0
data = "data.txt"
zh = 90
donghua = False

bbh = "1.1.0.1"# 版本号
background = "#66ff66"# 背景色
buttonbg = "#99ff99"# 按钮背景色


def set_up():
    global window
    window.destroy()# 销毁主窗口
    
    wset_up=Tk()# 设置窗口
    wset_up.title("随机点名——设置")
    # wset_up.resizable(0,0)# 禁止调节窗口大小
    try:# 尝试打开设置图标
        wset_up.iconbitmap('.\\RandomRollCall.ico')
    except:
        pass
    
    vname_file = StringVar()
    vbackground = StringVar()
    
    vname_file.set(file)
    vbackground.set(background)
    
    
    win = Frame(wset_up,
                bg = background,# 背景色
                )
    win.pack()
    
    f1 = Frame(win,
               bg = background,# 背景色
               )
    f1.pack(fill=X)
    
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        bg=background,          # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l1.pack(side=LEFT)    # 固定窗口位置
    ename_file = Entry(f1,# 姓名文件名输入框
               textvariable=vname_file,
               bg=background,          # 背景颜色
               width=30,# 宽度
               )
    ename_file.pack(side=LEFT)
    
    
    """
    obj['state'] = DISABLED   ###禁用
    obj['state'] = NORMAL     ###重新激活
    """
    f2 = Frame(win,
               bg = background,# 背景色
               )
    f2.pack(fill=X)
    
    l2 = Label(f2, 
        text="背景颜色：",    # 标签的文字
        bg=background,          # 背景颜色
        #fg="red",
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack(side=LEFT)    # 固定窗口位置
    l2['state'] = DISABLED   ###禁用
    
    ebackground = Entry(f2,# 姓名文件名输入框
               textvariable=vbackground,#可变本文
               bg=background,          # 背景颜色
               width=30,# 宽度
               )
    ebackground.pack(side=LEFT)
    ebackground['state'] = DISABLED   ###禁用
    
    
        
    bOK = Button(win,
               # text="确定",
               text="保存",
               font=('宋体', 14),        # 字体和字体大小
               bg=buttonbg,
               # command=OK,
               )
    bOK.pack()
    
    

    
    wset_up.mainloop()           #循环消息，让窗口活起来
    main()

def main():
    global window
    window=Tk()
    window.title("随机点名V%s"%bbh)
    window.resizable(0,0)# 禁止调节窗口大小
    try:# 尝试打开设置图标
        window.iconbitmap('.\\RandomRollCall.ico')
    except:
        pass
    
    
    
    win = Frame(window,
                bg = background,# 背景色
                )
    win.pack(fill=X)
    
    f1 = Frame(win,
               bg = background,# 背景色
               )
    f1.pack(fill=X)
    
    try:# 尝试打开设置图片
        ppset_up = PhotoImage(file=".\\set_up.png")
    except:# 打开失败
        bset_up = Button(f1,
                         text="设置",
                         # bd=0,# 按钮边框的大小，默认为2个像素
                         bg = buttonbg,# 按钮背景色
                         # image=pset_up,#加入图片
                         # compound = CENTER,#关键:设置为背景图片
                         font=('宋体', 12)         # 字体和字体大小
                         # command=set_up# 命令
                         )
    else:# 否则正常显示
        bset_up = Button(f1,
                     text="设置",
                     bd=0,# 按钮边框的大小，默认为2个像素
                     bg = background,# 按钮背景色
                     image=ppset_up,#加入图片
                     # compound = CENTER,#关键:设置为背景图片
                     font=('宋体', 12),         # 字体和字体大小
                     command=set_up# 命令
                     )
    finally:# 最后
        bset_up.pack(side=LEFT)
    
    c1 = Checkbutton(f1, 
                     bg = background,# 背景色
                     text='不重复点名', 
                     # variable=v4, 
                     onvalue=1, 
                     offvalue=0,
                     font=('宋体', 12)         # 字体和字体大小
                     #command=print_selection
                     )
    c1.pack(side=LEFT)
    
    l1 = Label(f1, 
               text="                             ",    # 标签的文字
               bg = background,# 背景色
               font=('宋体', 12),         # 字体和字体大小
               #width=15, height=2          # 标签长宽
               )
    l1.pack(side=LEFT)    # 固定窗口位置
    
    
    try:# 尝试打开设置图片
        phelp = PhotoImage(file=".\\help.png")
    except:# 打开失败
        bhelp = Button(f1,
                         text="帮助",
                         #image=phelp,#加入图片
                         bg = buttonbg,# 按钮背景色
                         #bd=0,# 按钮边框的大小，默认为2个像素
                         font=('宋体', 12)         # 字体和字体大小
                         #command=help
                         )
    else:# 否则正常显示
        bhelp = Button(f1,
                         text="帮助",
                         image=phelp,#加入图片
                         bg = background,# 按钮背景色
                         bd=0,# 按钮边框的大小，默认为2个像素
                         font=('宋体', 12)         # 字体和字体大小
                         #command=help
                         )
    finally:# 最后
        bhelp.pack(side=RIGHT)
    
    
    
    
    f2 = Frame(win,
               bg = background,# 背景色
               )
    f2.pack()
    
    l2 = Label(f2, 
        text="\n\n\n",    # 标签的文字
        bg = background,# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack()    # 固定窗口位置
    
    lname = Label(f2, 
        text="这里显示名字",    # 标签的文字
        bg = background,# 背景色
        font=('宋体', 30),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lname.pack()    # 固定窗口位置
    
    bsjdm = Button(f2,
               text="随机点名",
               bg = buttonbg,# 按钮背景色
               font=('宋体', 20),         # 字体和字体大小
               #command=sjdm
               )
    bsjdm.pack()# side=LEFT
    
    bkszt = Button(f2,# 开始暂停
               text="滚动点名",
               bg = buttonbg,# 按钮背景色
               font=('宋体', 20),         # 字体和字体大小
               #command=kszt
               )
    bkszt.pack()# side=LEFT
    
    l21 = Label(f2, 
        text="\n\n\n",    # 标签的文字
        bg = background,# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l21.pack()    # 固定窗口位置
    
    
    
    
    
    f3 = Frame(win,
               bg = background,# 背景色
               )
    f3.pack(fill=X)    # 固定窗口位置
    
    bql = Button(f3,
               text="清零",
               bg = buttonbg,# 按钮背景色
               font=('宋体', 12)         # 字体和字体大小
               # command=ql
               )
    bql.pack(side=LEFT)
    
    l3 = Label(f3, 
        # textvariable=v6,
        text="累计抽取人数：0",    # 标签的文字
        bg = background,# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l3.pack(side=LEFT)    # 固定窗口位置
    
    bjian = Button(f3,
               text="-",
               bg = buttonbg,# 按钮背景色
               font=('宋体', 12)         # 字体和字体大小
               #command=jian
               )
    bjian.pack(side=RIGHT)
    
    bjia = Button(f3,
               text="+",
               bg = buttonbg,# 按钮背景色
               font=('宋体', 12)         # 字体和字体大小
               #command=jia
               )
    bjia.pack(side=RIGHT)
    
    lzh = Label(f3, 
        text="字号：",    # 标签的文字
        bg = background,# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lzh.pack(side=RIGHT)    # 固定窗口位置
    
    
    
    
    
    
    
    # window.protocol("WM_DELETE_WINDOW", save_exit)
    # window.wm_attributes("-alpha", 0.4)        # 透明度(0.0~1.0)
    # window.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
    # window.wm_attributes("-topmost", True)     # 永远处于顶层
    window.mainloop()           #循环消息，让窗口活起来


if __name__ == "__main__":
    main()
