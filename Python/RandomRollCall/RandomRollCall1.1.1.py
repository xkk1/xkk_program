from tkinter import *# 图形界面

bbh = "1.1.0Alpha"

def main():
    window=Tk()
    window.title("随机点名V%s"%bbh)
    #window.resizable(0,0)# 禁止调节窗口大小
    
    win = Frame(window,
                # bg = "#7FFF00"# 背景色
                # title = "eee"
                )
    pset_up = PhotoImage(file="set_up.png")
    bset_up = Button(win,
                     text="设置",
                     image=pset_up,#加入图片
                     #compound = CENTER,#关键:设置为背景图片
                     font=('宋体', 12),# 字体和字体大小
                     #command=set_up
                     bd=0# 按钮边框的大小，默认为2个像素
                     ).pack(side=LEFT)
    phelp = PhotoImage(file=".\\help.png")
    bhelp = Button(win,
                     text="帮助",
                     image=phelp,#加入图片
                     font=('宋体', 12),# 字体和字体大小
                     bd=0# 按钮边框的大小，默认为2个像素
                     #command=help
                     ).pack(side=RIGHT)
    win.pack(fill=X)
    window.mainloop()           #循环消息，让窗口活起来

def set_up():
    pass

if __name__ == "__main__":
    main()

if __name__ != "__main__":
    window=Tk()
    window.title("随机点名V%s"%bbh)
    window.resizable(0,0)# 禁止调节窗口大小

    # 创建一个Label
    # 指定字体名称、大小、样式
    # ft = tkFont.Font(root=window, family='Fixdsys', size=zh, weight=tkFont.BOLD)


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

    # begin()
    # print("??????????")

    win = Frame(window)

    f1 = Frame(win)
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    e1 = Entry(f1,# 姓名文件名输入框
               textvariable=v1,
               width=55# 宽度
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
    
    f41 = Frame(f4)
    bsjdm = Button(f41,
               text="随机\n点名",
               font=('宋体', 20),         # 字体和字体大小
               command=sjdm
               )
    bsjdm.pack()# side=LEFT
    bkszt = Button(f41,# 开始暂停
               text="开始",
               font=('宋体', 20),         # 字体和字体大小
               command=kszt
               )
    bkszt.pack()# side=LEFT
    f41.pack(side=LEFT)
    
    l4 = Label(f4, 
        text="被  \n点→\n人→\n名  ",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 22),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    lname = Label(f4, 
        textvariable=v5,
        #text="王小明",    # 标签的文字
        #bg='green',                 # 背景颜色
        #font=ft,
        font=('黑体', 90),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lname.pack(side=LEFT)    # 固定窗口位置
    f4.pack(fill=X)

    f5 = Frame(win)
    bql = Button(f5,
               text="清零",
               font=('宋体', 12),         # 字体和字体大小
               command=ql
               ).pack(side=LEFT)
    l5 = Label(f5, 
        textvariable=v6,
        #text="累计抽取人数：0",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        ).pack(side=LEFT)    # 固定窗口位置
    
    bjian = Button(f5,
               text="-",
               font=('宋体', 12),         # 字体和字体大小
               command=jian
               ).pack(side=RIGHT)
    bjia = Button(f5,
               text="+",
               font=('宋体', 12),         # 字体和字体大小
               command=jia
               ).pack(side=RIGHT)
    lzh = Label(f5, 
        text="字号：",    # 标签的文字
        #bg='green',                 # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
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
    begin()
    window.protocol("WM_DELETE_WINDOW", save_exit)
    window.mainloop()           #循环消息，让窗口活起来
