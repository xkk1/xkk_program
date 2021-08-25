from tkinter import *# 图形界面
from tkinter import messagebox# 对话框
import jsondata
'''
bbh = ""# 版本号


jsondata.data = {
    'lj': 0, # 累计人数
    'zh': 90, # 字号
    'file': 'Students.txt',# 姓名文件
    'background': "#99ff66",# 背景色
    'buttonbg': "#99ff99",# 按钮背景色
}
'''

def help():
    #showinto （信息提示）
    # 弹出对话框
    messagebox.showinfo(title = '帮助',message="""有事加QQ群:：681032320
使用方法：
1、默认姓名文件为本目录下的“%s”
2、一个人名占一行，不要有空白行
3、点击“随机点名”即可随机点名
4、勾选“不重复点名”后同一个人只会抽到一次
所有人全被抽到后重新开始抽
点“↓复位↓”后重置
(使用Alt + Tab切换窗口)
更新日志：
已修复文件打开闪退bug
已修复当数据文件为隐藏时程序无法关闭的bug
但是要确保数据文件的属性不为只读
增加抽取动画
增加新的抽取方式""")

def set_up():
    global window
    #global jsondata.data
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
    
    vname_file.set(jsondata.data['file'])
    vbackground.set(jsondata.data['background'])
    
    
    win = Frame(wset_up,
                bg = jsondata.data['background'],# 背景色
                )
    win.pack()
    
    f1 = Frame(win,
               bg = jsondata.data['background'],# 背景色
               )
    f1.pack(fill=X)
    
    l1 = Label(f1, 
        text="姓名文件：",    # 标签的文字
        bg=jsondata.data['background'],          # 背景颜色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l1.pack(side=LEFT)    # 固定窗口位置
    ename_file = Entry(f1,# 姓名文件名输入框
               textvariable=vname_file,
               bg=jsondata.data['background'],          # 背景颜色
               width=30,# 宽度
               )
    ename_file.pack(side=LEFT)
    
    
    """
    obj['state'] = DISABLED   ###禁用
    obj['state'] = NORMAL     ###重新激活
    """
    f2 = Frame(win,
               bg = jsondata.data['background'],# 背景色
               )
    f2.pack(fill=X)
    
    l2 = Label(f2, 
        text="背景颜色：",    # 标签的文字
        bg=jsondata.data['background'],          # 背景颜色
        #fg="red",
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack(side=LEFT)    # 固定窗口位置
    l2['state'] = DISABLED   ###禁用
    
    ebackground = Entry(f2,# 姓名文件名输入框
               textvariable=vbackground,#可变本文
               bg=jsondata.data['background'],          # 背景颜色
               width=30,# 宽度
               )
    ebackground.pack(side=LEFT)
    ebackground['state'] = DISABLED   ###禁用
    
    
        
    bOK = Button(win,
               # text="确定",
               text="保存",
               font=('宋体', 14),        # 字体和字体大小
               bg=jsondata.data['buttonbg'],
               # command=OK,
               )
    bOK.pack()
    
    

    
    wset_up.mainloop()           #循环消息，让窗口活起来
    main()

def main():
    global window
    #global jsondata.data
    #print(jsondata.data)
    window=Tk()
    window.title("随机点名V%i.%i.%i.%i"%tuple([jsondata.data['verson'][i] for i in range(4)]))
    window.resizable(0,0)# 禁止调节窗口大小
    try:# 尝试打开设置图标
        window.iconbitmap('.\\RandomRollCall.ico')
    except:
        pass
    
    
    
    win = Frame(window,
                bg = jsondata.data['background'],# 背景色
                )
    win.pack(fill=X)
    
    f1 = Frame(win,
               bg = jsondata.data['background'],# 背景色
               )
    f1.pack(fill=X)
    
    try:# 尝试打开设置图片
        ppset_up = PhotoImage(file=".\\set_up.png")
    except:# 打开失败
        bset_up = Button(f1,
                         text="设置",
                         # bd=0,# 按钮边框的大小，默认为2个像素
                         bg = jsondata.data['buttonbg'],# 按钮背景色
                         # image=pset_up,#加入图片
                         # compound = CENTER,#关键:设置为背景图片
                         font=('宋体', 12),         # 字体和字体大小
                         command=set_up# 命令
                         )
    else:# 否则正常显示
        bset_up = Button(f1,
                     text="设置",
                     bd=0,# 按钮边框的大小，默认为2个像素
                     bg = jsondata.data['background'],# 按钮背景色
                     image=ppset_up,#加入图片
                     # compound = CENTER,#关键:设置为背景图片
                     font=('宋体', 12),         # 字体和字体大小
                     command=set_up,# 命令
                     )
    finally:# 最后
        bset_up.pack(side=LEFT)
    
    c1 = Checkbutton(f1, 
                     bg = jsondata.data['background'],# 背景色
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
               bg = jsondata.data['background'],# 背景色
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
                         bg = jsondata.data['buttonbg'],# 按钮背景色
                         #bd=0,# 按钮边框的大小，默认为2个像素
                         font=('宋体', 12),         # 字体和字体大小
                         command=help,
                         )
    else:# 否则正常显示
        bhelp = Button(f1,
                         text="帮助",
                         image=phelp,#加入图片
                         bg = jsondata.data['background'],# 按钮背景色
                         bd=0,# 按钮边框的大小，默认为2个像素
                         font=('宋体', 12),         # 字体和字体大小
                         command=help,
                         )
    finally:# 最后
        bhelp.pack(side=RIGHT)
    
    
    
    
    f2 = Frame(win,
               bg = jsondata.data['background'],# 背景色
               )
    f2.pack()
    
    l2 = Label(f2, 
        text="\n\n\n",    # 标签的文字
        bg = jsondata.data['background'],# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l2.pack()    # 固定窗口位置
    
    lname = Label(f2, 
        text="这里显示名字",    # 标签的文字
        bg = jsondata.data['background'],# 背景色
        font=('宋体', 30),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lname.pack()    # 固定窗口位置
    
    bsjdm = Button(f2,
               text="随机点名",
               bg = jsondata.data['buttonbg'],# 按钮背景色
               font=('宋体', 20),         # 字体和字体大小
               #command=sjdm
               )
    bsjdm.pack()# side=LEFT
    
    bkszt = Button(f2,# 开始暂停
               text="滚动点名",
               bg = jsondata.data['buttonbg'],# 按钮背景色
               font=('宋体', 20),         # 字体和字体大小
               #command=kszt
               )
    bkszt.pack()# side=LEFT
    
    l21 = Label(f2, 
        text="\n\n\n",    # 标签的文字
        bg = jsondata.data['background'],# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l21.pack()    # 固定窗口位置
    
    
    
    
    
    f3 = Frame(win,
               bg = jsondata.data['background'],# 背景色
               )
    f3.pack(fill=X)    # 固定窗口位置
    
    bql = Button(f3,
               text="清零",
               bg = jsondata.data['buttonbg'],# 按钮背景色
               font=('宋体', 12)         # 字体和字体大小
               # command=ql
               )
    bql.pack(side=LEFT)
    
    l3 = Label(f3, 
        # textvariable=v6,
        text="累计抽取人数：0",    # 标签的文字
        bg = jsondata.data['background'],# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    l3.pack(side=LEFT)    # 固定窗口位置
    
    bjian = Button(f3,
               text="-",
               bg = jsondata.data['buttonbg'],# 按钮背景色
               font=('宋体', 12)         # 字体和字体大小
               #command=jian
               )
    bjian.pack(side=RIGHT)
    
    bjia = Button(f3,
               text="+",
               bg = jsondata.data['buttonbg'],# 按钮背景色
               font=('宋体', 12)         # 字体和字体大小
               #command=jia
               )
    bjia.pack(side=RIGHT)
    
    lzh = Label(f3, 
        text="字号：",    # 标签的文字
        bg = jsondata.data['background'],# 背景色
        font=('宋体', 12),         # 字体和字体大小
        #width=15, height=2          # 标签长宽
        )
    lzh.pack(side=RIGHT)    # 固定窗口位置
    
    
    
    # window.protocol("WM_DELETE_WINDOW", save_exit)
    # window.wm_attributes("-alpha", 0.4)        # 透明度(0.0~1.0)
    # window.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
    # window.wm_attributes("-topmost", True)     # 永远处于顶层
    window.mainloop()           #循环消息，让窗口活起来