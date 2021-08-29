import urllib.request
import json
import tkinter as tk
import time
import threading

uid = '82589937'
uid = '314076440'
# 所用api：
# https://api.bilibili.com/x/space/acc/info?mid=513689605&jsonp=jsonp  名称 没用到
# https://api.bilibili.com/x/relation/stat?vmid=513689605&jsonp=jsonp  粉丝
# https://api.bilibili.com/x/space/arc/search?mid={uid}&ps=30&tid=0&pn={page_number}&jsonp=jsonp
# https://api.bilibili.com/x/web-interface/view?aid=629032969 视频数据 没用到
# https://api.bilibili.com/x/web-interface/view?bvid=BV1et4y1B7Yp 视频数据

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

# font = ('黑体', 20)  # 字体 字号
foreground = 'white'  # 字体颜色
background = 'black'  # 背景色
toolwindow = False  # 是否使用工具窗口
alpha = 0.7  # 窗口透明度(0.0~1.0)  数值越小窗口透明度越高
transparentcolor = (False, 'white') # 是否使用及设定透明色
topmost = True  # 是否把窗口置顶
overrideredirect = True  # 是否隐藏掉窗口边框和标题栏
interval = 20  # 每次获取的时间间隔，单位秒(s)


def get_video_bvid(uid):
    """从UID得到up主最新视频的BV号"""
    url = 'https://api.bilibili.com/x/space/arc/search?mid={uid}&ps={ps}&tid=0&pn={page_number}&jsonp=jsonp'
    url = url.format(uid=uid, ps='1', page_number='1')
    print('get_video_bvid:', url)
    request = urllib.request.Request(url)
    request.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(request)
    json_data = response.read().decode('utf-8')
    py_data = json.loads(json_data)
    # print(json_data)
    # print(py_data)
    author = py_data['data']['list']['vlist'][0]['author']  # 作者
    title = py_data['data']['list']['vlist'][0]['title']  # 标题
    play = py_data['data']['list']['vlist'][0]['play']  # 播放次数
    bvid = py_data['data']['list']['vlist'][0]['bvid']  # 最新视频的BV号
    aid = py_data['data']['list']['vlist'][0]['aid']  # 最新视频aid
    information = {
        'author': author,
        'title': title,
        'play': play,
        'bvid': bvid,
        'aid':aid,
        }
    print(information)
    return bvid

def get_video_information(uid):
    """得到视频的信息"""
    bvid = get_video_bvid(uid)
    url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + bvid
    print('get_video_information:', url)
    request = urllib.request.Request(url)
    request.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(request)
    json_data = response.read().decode('utf-8')
    py_data = json.loads(json_data)
    # print(json_data)
    # print(py_data)
    name = py_data['data']['owner']['name']  # 作者
    title = py_data['data']['title']  # 标题
    coin = py_data['data']['stat']['coin']  # 投币
    favorite = py_data['data']['stat']['favorite']  # 收藏
    like = py_data['data']['stat']['like']  # 点赞
    share = py_data['data']['stat']['share']  # 分享
    view = py_data['data']['stat']['view']  # 播放次数
    danmaku = py_data['data']['stat']['danmaku']  # 弹幕
    reply = py_data['data']['stat']['reply']  # 评论
    information = {
        'name': name,  # 作者
        'title': title,  # 标题
        'coin': coin,  # 投币
        'favorite': favorite,  # 收藏
        'like': like,  # 点赞
        'share': share,  # 分享
        'view': view,  # 播放次数
        'danmaku': danmaku,  # 弹幕
        'reply': reply,  # 评论
        }
    print(information)
    return information

def get_author_follower(uid):
    """得到up主的粉丝数"""
    url = 'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % uid
    print('get_author_following:', url)
    request = urllib.request.Request(url)
    request.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(request)
    json_data = response.read().decode('utf-8')
    py_data = json.loads(json_data)
    # print(json_data)
    # print(py_data)
    follower = py_data['data']['follower']
    return follower

def get_information(uid):
    try:
        follower = get_author_follower(uid)
        information = get_video_information(uid)
        information['follower'] = follower
    except:
        information = {
            'name': '获取失败',  # 作者
            'title': '获取失败，请确保uid正确和网络良好！',  # 标题
            'coin': 0,  # 投币
            'favorite': 0,  # 收藏
            'like': 0,  # 点赞
            'share': 0,  # 分享
            'view': 0,  # 播放次数
            'danmaku': 0,  # 弹幕
            'reply': 0,  # 评论
            'follower': 0,  # 粉丝
            }
    return information

def change_information():
    global label
    global information
    # while True:
    information = get_information(uid)
    
    # print('\n\n\n\n', information)
    data = ''
    data += '  up主  ：' + information['name'] + '\n'
    data += '粉 丝 数：' + str(information['follower']) + '\n'
    if len(information['title']) > 15:
        data += '最新视频：' + information['title'][:15] + '…\n'
    else:
        data += '最新视频：' + information['title'] + '\n'
    data += '播放次数：' + str(information['view']) + '\n'
    data += '弹 幕 数：' + str(information['danmaku']) + '\n'
    data += '点 赞 数：' + str(information['like']) + '\n'
    data += '投 币 数：' + str(information['coin']) + '\n'
    data += '收 藏 数：' + str(information['favorite']) + '\n'
    data += '分享次数：' + str(information['share']) + '\n'
    data += '评 论 数：' + str(information['reply'])  # + '\n'
    
    print(data)
    
    label['text'] = data
    
    # time.sleep(interval)
    # exit()

def change_information_threading():
    while True:
        change_information()
        time.sleep(interval)

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() # + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        try:
            # For Mac OS
            tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", tw._w,
                       "help", "noActivates")
        except tk.TclError:
            pass
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffff", relief=tk.SOLID, borderwidth=1,
                      # font=("tahoma", "8", "normal")
                      )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def main():
    root = tk.Tk()
    root.title('B站up主信息显示')
    root.iconbitmap('.\\data\\icon.ico')
    
    global label
    label = tk.Label(
        root,
        text='正在加载. . .',
        font=('宋体', 20),
        fg=foreground,
        bg=background,
        justify=tk.LEFT
        )
    label.pack()
    
    set_up_frame_outside = tk.Frame(
        root,
        # fg=foreground,
        bg=background,
        )
    # set_up_frame_outside.pack(fill=tk.X)
    
    set_up_frame = tk.Frame(
        set_up_frame_outside,
        # fg=foreground,
        bg=background,
        )
    set_up_frame.pack(side=tk.RIGHT)
    
    def change_up():
        global change_up_window
        try:
            change_up_window.deiconify()
        except:
            global text
            change_up_window = tk.Toplevel(root)
            change_up_window.title('更改UP主')
            change_up_window.resizable(0, 0)  # 锁定窗口大小不能改变
            change_up_window.iconbitmap('.\\data\\icon.ico')
            
            change_up_frame = tk.Frame(change_up_window)
            change_up_frame.pack(padx=10, pady=10)
            
            help_label = tk.Label(
                change_up_frame,
                text='请输入你要更改up主的uid',
                font=('宋体', 15),
                )
            help_label.pack(padx=5, pady=5)
            
            uid_entry = tk.Entry(change_up_frame)
            uid_entry.pack(padx=5, pady=5)
            uid_entry.insert(tk.END, uid)
            
            ok_cancel_frame = tk.Frame(change_up_frame)
            ok_cancel_frame.pack()
            
            paste_button = tk.Button(
                ok_cancel_frame,
                text='粘贴',
                font=('宋体', 15),
                command=lambda : uid_entry.insert(tk.INSERT, root.clipboard_get()),
                )
            paste_button.pack(side=tk.LEFT, padx=5, pady=5)
            
            def change_uid():
                global uid
                uid = uid_entry.get()
                change_information()
                change_up_window.destroy()
            
            ok_button = tk.Button(
                ok_cancel_frame,
                text='确定',
                font=('宋体', 15),
                command=change_uid,
                )
            ok_button.pack(side=tk.LEFT, padx=5, pady=5)
            
            cancel_button = tk.Button(
                ok_cancel_frame,
                text='取消',
                font=('宋体', 15),
                command=lambda :change_up_window.destroy(),
                )
            cancel_button.pack(side=tk.LEFT, padx=5, pady=5)
            
            change_up_window.attributes('-topmost', topmost)  # 处于顶层
            change_up_window.mainloop()
    
    change_up_PhotoImage = tk.PhotoImage(file='.\\data\\change_up.png')
    change_up_button = tk.Button(
        set_up_frame,
        text='更改',
        image=change_up_PhotoImage,
        # compound = tk.CENTER,  # 关键:设置为背景图片
        fg=foreground,
        bg=background,
        # width=20,
        # height=20,
        command=change_up,
        )
    change_up_button.grid(row=0, column=0)
    createToolTip(change_up_button, '更改up主')
    
    def change_topmost():
        # global topmost_true_PhotoImage
        # global topmost_false_PhotoImage
        # global topmost_button
        global topmost
        if topmost_button['text'] == '置顶':
            topmost = True
            topmost_button['text'] = '取消置顶'
            topmost_button['image'] = topmost_true_PhotoImage
        else:
            topmost = False
            topmost_button['text'] = '置顶'
            topmost_button['image'] = topmost_false_PhotoImage
        root.attributes('-topmost', topmost)  # 处于顶层(更新状态)
    
    # global topmost_true_PhotoImage
    # global topmost_false_PhotoImage
    # global topmost_button
    topmost_true_PhotoImage = tk.PhotoImage(file='.\\data\\topmost_true.png')
    topmost_false_PhotoImage = tk.PhotoImage(file='.\\data\\topmost_false.png')
    topmost_button = tk.Button(
        set_up_frame,
        text='取消置顶',
        image=topmost_true_PhotoImage,
        fg=foreground,
        bg=background,
        command=change_topmost,
        )
    topmost_button.grid(row=0, column=1)
    createToolTip(topmost_button, '置顶')
    
    def change_fix():
        # global on_motion
        if fix_button['text'] == '固定':
            fix_button['text'] = '取消固定'
            fix_button['image'] = fix_true_PhotoImage
            # print('固定')
            # def on_motion(event):
            #     pass
            root.bind("<B1-Motion>", lambda x : True)
        else:
            fix_button['text'] = '固定'
            fix_button['image'] = fix_false_PhotoImage
            '''
            print('取消固定')
            def on_motion(event):
                global x, y
                deltax = event.x - x
                deltay = event.y - y
                _x = root.winfo_x() + deltax
                _y = root.winfo_y() + deltay
                root.geometry("+%s+%s" % (_x, _y))'''
            root.bind("<B1-Motion>", on_motion)
    
    fix_true_PhotoImage = tk.PhotoImage(file='.\\data\\fix_true.png')
    fix_false_PhotoImage = tk.PhotoImage(file='.\\data\\fix_false.png')
    fix_button = tk.Button(
        set_up_frame,
        text='固定',
        image=fix_false_PhotoImage,
        fg=foreground,
        bg=background,
        command=change_fix,
        )
    fix_button.grid(row=0, column=2)
    createToolTip(fix_button, '固定')
    
    exit_PhotoImage = tk.PhotoImage(file='.\\data\\exit.png')
    exit_button = tk.Button(set_up_frame, text='退出', image=exit_PhotoImage,
        fg=foreground,
        bg=background,
        command=exit,
        )
    exit_button.grid(row=0, column=3)
    createToolTip(exit_button, '退出')
    
    
    def start_move(event):
        global x, y
        x = event.x
        y = event.y
    '''
    def stop_move(event):
        x = None
        y = None
    '''
    # global on_motion
    def on_motion(event):
        global x, y
        deltax = event.x - x
        deltay = event.y - y
        _x = root.winfo_x() + deltax
        _y = root.winfo_y() + deltay
        root.geometry("+%s+%s" % (_x, _y))
    
    def enter(event):
        set_up_frame_outside.pack(fill=tk.X)
    
    def leave(event):
        set_up_frame_outside.pack_forget()
    
    root.bind("<ButtonPress-1>", start_move)
    # root.bind("<ButtonRelease-1>", stop_move)
    root.bind("<B1-Motion>", on_motion)
    root.bind('<Button-3>', lambda event:exit()) # 右键单击事件
    
    root.bind('<Enter>', enter) # 鼠标移动到区域 Enter
    root.bind('<Leave>', leave) # 鼠标离开区域 Leave
    
    root.overrideredirect(overrideredirect)  # 隐藏掉窗口边框和标题栏
    root.attributes('-toolwindow', toolwindow)  # 置为工具窗口(没有最大最小按钮)
    root.attributes('-alpha', alpha)  # 透明度(0.0~1.0)
    root.attributes('-topmost', topmost)  # 处于顶层
    if transparentcolor[0]:
        # 这一行可以将所有的白色透明掉
        root.attributes("-transparentcolor", transparentcolor[1])
    
    t =  threading.Thread(target=change_information_threading) # , args=(old_verson, ))
    t.setDaemon(True)  # 设置线程为守护线程
    t.start()
    
    root.mainloop()


if __name__ == '__main__':
    main()