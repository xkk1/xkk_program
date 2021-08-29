import urllib.request
import json
import tkinter as tk
import tkinter.messagebox
import time
import threading
import os
import os.path
import copy
import traceback

uid = '82589937'
uid = '314076440'
uid = '513689605'
# 所用api：
# https://api.bilibili.com/x/space/acc/info?mid=513689605&jsonp=jsonp  名称
# https://api.bilibili.com/x/relation/stat?vmid=513689605&jsonp=jsonp  粉丝
# https://api.bilibili.com/x/space/arc/search?mid={uid}&ps=30&tid=0&pn={page_number}&jsonp=jsonp
# https://api.bilibili.com/x/web-interface/view?aid=629032969 视频数据 没用到
# https://api.bilibili.com/x/web-interface/view?bvid=BV1et4y1B7Yp 视频数据

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'

# 初始化数据
data = {
    "version": "0.0.8",  # 版本
    "program": 'B站up主信息显示',  # 程序名称
    "author": "小喾苦",  #制作者
    "uid": '513689605',  # 用户的uid
    "font": ('黑体', 20),  # 字体 字号
    "foreground": 'white',  # 字体颜色
    "background": 'black',  # 背景色
    "toolwindow": True ,  # 是否使用工具窗口
    "alpha": "0.7",  # 窗口透明度(0.0~1.0)  数值越小窗口透明度越高
    "transparentcolor": (False, 'white'),  # 是否使用及设定透明色
    "topmost": True,  # 是否把窗口置顶
    "overrideredirect": True,  # 是否隐藏掉窗口边框和标题栏
    # "interval": 20,  # 每次获取的时间间隔，单位秒(s)
    "update_time": 30.0,  # 每次获取的时间间隔，单位秒(s)
    "title_length": 15,  # 显示视频标题的最大长度
    "form": """up主：{名字}(LV{等级})	粉 丝 数：{粉丝数}{粉丝数变化}
最新视频：{标题}
播放次数：{播放数}{播放数变化}		弹 幕 数：{弹幕数}{弹幕数变化}
点 赞 数：{点赞数}{点赞数变化}		投 币 数：{投币枚数}{投币枚数变化}
收 藏 数：{收藏人数}{收藏人数变化}		分享次数：{分享次数}{分享次数变化}
评 论 数：{评论数}{评论数变化}	({更新时间})"""
}
default_data = copy.deepcopy(data)  # 默认数据（深拷贝）
if not os.path.isdir(f".{os.sep}data"):
    os.mkdir(f".{os.sep}data")
json_data_file = f".{os.sep}data{os.sep}{data['program']}v{data['version']}.json"
error_information = {
    'name': '获取失败',
    'level': -1,
    'coins': -1,
    'birthday': '',
    'sex': '',
    'top_photo': '',
    'follower': -1,
    'following': -1,
    'author': '获取失败',
    'title': '获取失败，请确保uid正确和网络良好！',
    'bvid': '',
    'aid': -1,
    'pic': '',
    'description': '获取失败，请确保uid正确和网络良好！',
    'created': 0,
    'length': '00:00',
    'coin': -1,
    'favorite': -1,
    'like': -1,
    'share': -1,
    'view': -1,
    'danmaku': -1,
    'reply': -1,
    'videos': -1,
    'tname': '',
    'duration': -1,
    'face': 'http://i0.hdslb.com/bfs/face/member/noface.jpg',
    'dislike': -1,
    'width': -1,
    'height': -1}
old_information = copy.deepcopy(error_information)


def show_information_window(title, content):
    window = tk.Tk()
    window.title(title)
    try:
        window.iconbitmap(f'.{os.sep}data{os.sep}icon.ico')
    except:
        pass
    # windows.geometry('100x100')
    t = tk.Text(window,
            width=55,
            height=30,
            )
    t.pack()
    t.insert(tk.INSERT,content)
    window.attributes('-topmost', data["topmost"])  # 处于顶层
    window.mainloop()

def show_error(content):
    show_information_window("出错了！", content)

def save_data(data, json_data_file):
    """保存数据到文件
    data - 要保存的数据
    json_data_file - 保存json文件名"""
    # 写入 JSON 数据
    with open(json_data_file, 'w') as f:
        try:
            json.dump(data, f, indent=4)
        except:
            print('数据写入失败！')
    return data

def change_data(new_data, old_data):
    '改变数据'
    # 浅拷贝
    data = new_data.copy()
    # 获取旧数据的所有键
    old_keys = list(old_data.keys())
    
    # 如果没有则加上
    for key in old_keys:
        if key not in data:
            data[key] = old_data[key]
    
    return data

def read_data(json_data_file, default_data=default_data):
    '读数据'
    # 判断数据文件是否存在
    if os.path.isfile(json_data_file):
        with open(json_data_file, 'r') as f:
            try: # 尝试把json转换成Python的数据类型
                new_data = json.load(f)
                new_data = change_data(new_data, default_data)
                return new_data
            except:
                print('数据损坏，无法读取！已恢复默认数据')
                # print(new_data)
                return default_data
    else:
        # print("文件")
        save_data(data, json_data_file)
        return default_data

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
    pic = py_data['data']['list']['vlist'][0]['pic']  # 封面地址
    description = py_data['data']['list']['vlist'][0]['description']  # 简介
    created = py_data['data']['list']['vlist'][0]['created']  # 上传时的时间戳
    length = py_data['data']['list']['vlist'][0]['length']  # 视频时长
    information = {
        'author': author,
        'title': title,
        'view': play,
        'bvid': bvid,
        'aid':aid,
        "pic": pic,
        "description": description,
        "created": created,
        "length": length,
        }
    # print(information)
    # return (bvid, author)
    # return bvid
    return information

def get_video_information(uid):
    """得到视频的信息"""
    # bvid, author = get_video_bvid(uid)  # 未解决联合投稿时up主出错的bug
    information1 = get_video_bvid(uid)
    bvid = information1["bvid"]
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
    pic = py_data['data']['pic']  # 封面地址
    videos = py_data['data']['videos']  # 视频数量
    tname = py_data['data']['tname']  # 分区2
    duration = py_data['data']['duration']  # 持续时间(单位s)
    face = py_data['data']['owner']['face']  # 作者头像地址
    dislike = py_data['data']['stat']['dislike']  # 不喜欢数、踩
    width = py_data['data']["dimension"]["width"]  # 宽度
    height = py_data['data']["dimension"]["height"]  # 高度
    information = {
        'author': name,  # author,  # 作者（bug？？？）
        'title': title,  # 标题
        'coin': coin,  # 投币
        'favorite': favorite,  # 收藏
        'like': like,  # 点赞
        'share': share,  # 分享
        'view': view,  # 播放次数
        'danmaku': danmaku,  # 弹幕
        'reply': reply,  # 评论
        "pic": pic,
        "videos": videos,
        "tname": tname,
        "duration" : duration,
        "face": face,
        "dislike": dislike,
        "width": width,
        "height": height,
        }
    # print(information)
    information = change_data(information1, information)
    return information

def get_author_follower_and_following(uid):
    """得到up主的粉丝数"""
    url = 'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % uid
    print('get_author_follower_and_following:', url)
    request = urllib.request.Request(url)
    request.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(request)
    json_data = response.read().decode('utf-8')
    py_data = json.loads(json_data)
    # print(json_data)
    # print(py_data)
    follower = py_data['data']['follower']  # 粉丝数
    following = py_data['data']['following']  # 关注数
    information = {
        "follower": follower,  # 粉丝数
        "following": following,  # 关注数
        }
    return information

def get_up_name(uid):
    """得到up主的名字，为了解决联合投稿up主出错的bug"""
    url = 'https://api.bilibili.com/x/space/acc/info?mid=%s&jsonp=jsonp' % uid
    print('get_up_name:', url)
    request = urllib.request.Request(url)
    request.add_header('User-Agent', user_agent)
    response = urllib.request.urlopen(request)
    json_data = response.read().decode('utf-8')
    # print(json_data)
    py_data = json.loads(json_data)
    # print('get_up_name')
    name = py_data['data']['name']  # 名字
    level = py_data['data']['level']  # 等级
    # coins = py_data['data']['coins']  # 硬币数
    # birthday = py_data['data']['birthday']  # 生日
    sex = py_data['data']['sex']  # 性别
    top_photo = py_data['data']['top_photo']  # 空间背景链接
    information = {
        "name": name,
        "level": level,
        # "coins": coins,
        # "birthday": birthday,
        "sex": sex,
        "top_photo": top_photo,
        }
    return information
    

def get_information(uid):
    try:
        information = {}
        information = change_data(get_video_information(uid), information)
        information = change_data(get_author_follower_and_following(uid), information)
        information = change_data(get_up_name(uid), information)
        print("information:\n", information)
    except:
        print("出错信息：\n" + traceback.format_exc())
        information = error_information
    return information

def change_information():
    global label
    global information
    global old_information
    # while True:
    information = get_information(data["uid"])
    
    # print('\n\n\n\n', information)
    """
    datas = ''
    datas += '  up主  ：' + information['name'] + '\n'
    datas += '粉 丝 数：' + str(information['follower']) + '\n'
    if len(information['title']) > data["title_length"]:
        datas += '最新视频：' + information['title'][:data["title_length"]] + '…\n'
    else:
        datas += '最新视频：' + information['title'] + '\n'
    datas += '播放次数：' + str(information['view']) + '\n'
    datas += '弹 幕 数：' + str(information['danmaku']) + '\n'
    datas += '点 赞 数：' + str(information['like']) + '\n'
    datas += '投 币 数：' + str(information['coin']) + '\n'
    datas += '收 藏 数：' + str(information['favorite']) + '\n'
    datas += '分享次数：' + str(information['share']) + '\n'
    datas += '评 论 数：' + str(information['reply'])  # + '\n'
    """
    def get_change(key, information=information, old_information=old_information):
        change_str = "%+d" % (information[key] - old_information[key])
        if change_str == "+0":
            return ""
        else:
            return change_str
    
    name = 名字 = information['name']
    follower = 粉丝数 = information['follower']
    follower_change = 粉丝数变化 = get_change("follower")
    following = 关注数 = information['following']
    following_change = 关注数变化 =  get_change("following")
    level = 等级 = information['level']
    sex = 性别 = information['sex']
    face = 头像链接 = information['face']
    top_photo = information['top_photo']
    
    if len(information['title']) > data["title_length"]:
        title = 标题 = information['title'][:data["title_length"]]
    else:
        title = 标题 = information['title']
    author = 作者 = information['author']
    view = 播放数 = information['view']
    view_change = 播放数变化 =  get_change("view")
    danmaku = 弹幕数 = information['danmaku']
    danmaku_change = 弹幕数变化 =  get_change("danmaku")
    like = 点赞数 = information['like']
    like_change = 点赞数变化 =  get_change("like")
    coin = 投币枚数 = information['coin']
    coin_change = 投币枚数变化 =  get_change("coin")
    favorite = 收藏人数 = information['favorite']
    favorite_change = 收藏人数变化 =  get_change("favorite")
    share = 分享次数 = information['share']
    share_change = 分享次数变化 =  get_change("share")
    reply = 评论数 = information['reply']
    reply_change = 评论数变化 =  get_change("reply")
    BV = bvid = information['bvid']
    AV = aid = information['aid']
    description = 简介 = information['description']
    created = 上传时的时间戳 = information['created']
    上传时间 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(information['created']))
    length = 视频时长 = information['length']
    videos = 视频数 = information['videos']
    tname = 分区2 = information['tname']
    duration = 持续时间 = information['duration']
    dislike = 不喜欢数 = 踩 = information['dislike']
    dislike_change = 不喜欢数变化 = 踩变化 =  get_change("dislike")
    width = 宽度 = information['width']
    height = 高度 = information['height']
    pic = 封面链接 = information['pic']
    change_time = 更新时间 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(data)
    
    # label['text'] = datas
    informations = eval("f" + repr(data["form"]))
    print("信息：\n", informations)
    label['text'] = informations
    old_information = information  # 暂时这样没有问题
    # time.sleep(interval)
    # exit()

def change_information_threading():
    while True:
        change_information()
        time.sleep(data["update_time"])

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

def save_exit():
    global data
    data["version"] = default_data["version"]
    data["program"] = default_data["program"]
    data["author"] = default_data["author"]
    save_data(data, json_data_file)
    print("have saved")
    exit()

def GUI():
    root = tk.Tk()
    root.title(f'{data["program"]}v{data["version"]}')
    try:
        root.iconbitmap(f'.{os.sep}data{os.sep}icon.ico')
    except:
        pass
    
    global label
    label = tk.Label(
        root,
        text='正在加载. . .',
        font=data["font"],
        fg=data["foreground"],
        bg=data["background"],
        justify=tk.LEFT
        )
    label.pack()
    
    set_up_frame_outside = tk.Frame(
        root,
        # fg=foreground,
        bg=data["background"],
        )
    # set_up_frame_outside.pack(fill=tk.X)
    
    set_up_frame = tk.Frame(
        set_up_frame_outside,
        # fg=foreground,
        bg=data["background"],
        )
    set_up_frame.pack(side=tk.RIGHT)
    
    def change():
        global change_window
        try:
            change_window.deiconify()
        except:
            global text
            change_window = tk.Toplevel(root)
            change_window.title(f'更改信息 - {data["program"]}v{data["version"]}')
            change_window.resizable(0, 0)  # 锁定窗口大小不能变化
            try:
                change_window.iconbitmap(f'.{os.sep}data{os.sep}icon.ico')
            except:
                pass
            
            change_frame = tk.Frame(change_window)
            change_frame.pack(padx=5, pady=5)

            
            paste_uid_button = tk.Button(
                change_frame,
                text='粘贴',
                font=('宋体', 15),
                command=lambda : uid_entry.insert(tk.INSERT, root.clipboard_get()),
                )
            paste_uid_button.grid(row=0, column=0)
            
            change_up_label = tk.Label(
                change_frame,
                text='    up主uid：',
                font=('宋体', 15),
                )
            change_up_label.grid(row=0, column=1)
            
            uid_entry = tk.Entry(change_frame)
            uid_entry.grid(row=0, column=2)
            uid_entry.insert(tk.END, data["uid"])
            

            
            change_title_length_label = tk.Label(
                change_frame,
                text='显示视频标题的最大长度：',
                font=('宋体', 15),
                )
            change_title_length_label.grid(row=1, column=0, columnspan=2)
            
            title_length_entry = tk.Entry(change_frame)
            title_length_entry.grid(row=1, column=2)
            title_length_entry.insert(tk.END, str(data["title_length"]))
            

            
            change_update_time_label = tk.Label(
                change_frame,
                text=' 数据的刷新时间间隔(s)：',
                font=('宋体', 15),
                )
            change_update_time_label.grid(row=2, column=0, columnspan=2)
            
            update_time_entry = tk.Entry(change_frame)
            update_time_entry.grid(row=2, column=2)
            update_time_entry.insert(tk.END, str(data["update_time"]))

            form_label = tk.Label(
                change_frame,
                text="显示格式↓",
                font=('宋体', 15))
            form_label.grid(row=3, column=0)

            def show_help():
                show_information_window(
                    f"帮助 - {data['program']}V{data['version']}",
                    """帮助信息：
Ctrl+C复制，Ctrl+V粘贴
uid可以在空间里找到
"显示格式"帮助
在{}中填写的数据名称将会替换成制定数据
（想要显示“{”或“}”的用“{{”或“}}”代替）
在{}里可以填写的有（同一行的等效）：
change_time、更新时间
1)与up主相关
    name、名字
    follower、粉丝数
    follower_change 、粉丝数变化
    following、关注数
    following_change、关注数变化
    level、等级
    sex、性别
    face、头像链接
    top_photo (这个是封面背景链接)
2)与视频相关
    title、标题
    author、作者
    view、播放数
    view_change、播放数变化
    danmaku、弹幕数
    danmaku_change、弹幕数变化
    like、点赞数
    like_change、点赞数变化
    coin、投币枚数
    coin_change、投币枚数变化
    favorite、收藏人数
    favorite_change、收藏人数变化
    share、分享次数
    share_change、分享次数变化
    reply、评论数
    reply_change、评论数变化
    BV、bvid
    AV、aid
    description、简介
    created、上传时的时间戳
    上传时间
    length、视频时长
    videos、视频数
    tname、分区2
    duration、持续时间
    dislike、不喜欢数、踩
    dislike_change、不喜欢数变化、踩变化
    width、宽度
    height、高度
    pic、封面链接

推荐示例：
up主：{名字}(LV{等级})	粉 丝 数：{粉丝数}{粉丝数变化}
最新视频：{标题}
播放次数：{播放数}{播放数变化}		弹 幕 数：{弹幕数}{弹幕数变化}
点 赞 数：{点赞数}{点赞数变化}		投 币 数：{投币枚数}{投币枚数变化}
收 藏 数：{收藏人数}{收藏人数变化}		分享次数：{分享次数}{分享次数变化}
评 论 数：{评论数}{评论数变化}	({更新时间})

短信息示例：
更新时间：{更新时间}
up主  ：{名字}
粉丝数：{粉丝数}
粉丝数变化：{粉丝数变化}
关注数：{关注数}
关注数变化：{关注数变化}
等级：{等级}
性别：{性别}
最新视频：{标题}
作者：{作者}
播放次数：{播放数}
播放次数变化：{播放数变化}
弹 幕 数：{弹幕数}
弹 幕 数变化：{弹幕数变化}
点 赞 数：{点赞数}
点 赞 数变化：{点赞数变化}
投 币 数：{投币枚数}
投 币 数变化：{投币枚数变化}
收 藏 数：{收藏人数}
收 藏 数变化：{收藏人数变化}
分享次数：{分享次数}
分享次数变化：{分享次数变化}
评 论 数：{评论数}
评 论 数变化：{评论数变化}
BV：{BV}
AV：{AV}
上传时的时间戳：{上传时的时间戳}
上传时间：{上传时间}
视频时长：{视频时长}
视频数：{视频数}
分区2：{分区2}
持续时间：{持续时间}
踩：{踩}
踩变化：{踩变化}
宽度：{宽度}
高度：{高度}

全部示例：
更新时间：{更新时间}
up主  ：{名字}
粉丝数：{粉丝数}
粉丝数变化：{粉丝数变化}
关注数：{关注数}
关注数变化：{关注数变化}
等级：{等级}
性别：{性别}
头像链接：{头像链接}
top_photo：{top_photo}
最新视频：{标题}
作者：{作者}
播放次数：{播放数}
播放次数变化：{播放数变化}
弹 幕 数：{弹幕数}
弹 幕 数变化：{弹幕数变化}
点 赞 数：{点赞数}
点 赞 数变化：{点赞数变化}
投 币 数：{投币枚数}
投 币 数变化：{投币枚数变化}
收 藏 数：{收藏人数}
收 藏 数变化：{收藏人数变化}
分享次数：{分享次数}
分享次数变化：{分享次数变化}
评 论 数：{评论数}
评 论 数变化：{评论数变化}
BV：{BV}
AV：{AV}
简介：{简介}
上传时的时间戳：{上传时的时间戳}
上传时间：{上传时间}
视频时长：{视频时长}
视频数：{视频数}
分区2：{分区2}
持续时间：{持续时间}
踩：{踩}
踩变化：{踩变化}
宽度：{宽度}
高度：{高度}
封面链接：{封面链接}""")
            
            show_help_button = tk.Button(
                change_frame,
                text='帮助',
                font=('宋体', 15),
                command=show_help)
            show_help_button.grid(row=3, column=2)
            
            form_text = tk.Text(change_frame,
                width=55,
                height=20,)
            form_text.grid(row=4, column=0, columnspan=3)
            form_text.insert(tk.END, data["form"])
            
            
            def change_data():
                global data
                # global uid
                # global title_length
                # global update_time
                try:
                    temp_title_length = int(title_length_entry.get())
                    if  temp_title_length> 0:
                        data["title_length"] = temp_title_length
                    else:
                        raise TypeError
                    temp_update_time = float(update_time_entry.get())
                    if temp_update_time > 0:
                        data["update_time"] = temp_update_time
                    else:
                        raise TypeError
                    data["uid"] = uid_entry.get()
                    print(data["uid"])
                    data["form"] = form_text.get(1.0, "end")[:-1]
                    change_information()
                    change_window.destroy()
                except:
                    tkinter.messagebox.showerror(
                        '出错了-_-！', 
                        '出现数据错误！\n请检查您输入的数据是否正确')
            
            ok_button = tk.Button(
                change_frame,
                text='确定',
                font=('宋体', 15),
                command=change_data,
                )
            ok_button.grid(row=5, column=1)
            
            cancel_button = tk.Button(
                change_frame,
                text='取消',
                font=('宋体', 15),
                command=lambda :change_window.destroy(),
                )
            cancel_button.grid(row=5, column=2)
            
            change_window.attributes('-topmost', data["topmost"])  # 处于顶层
            change_window.mainloop()
    
    try:
        change_PhotoImage = tk.PhotoImage(file=f'.{os.sep}data{os.sep}change.png')
    except:
        change_PhotoImage = None
    change_button = tk.Button(
        set_up_frame,
        text='更改',
        image=change_PhotoImage,
        # compound = tk.CENTER,  # 关键:设置为背景图片
        fg=data["foreground"],
        bg=data["background"],
        # width=20,
        # height=20,
        command=change,
        )
    change_button.grid(row=0, column=0)
    createToolTip(change_button, '更改')
    
    def change_topmost():
        # global topmost_true_PhotoImage
        # global topmost_false_PhotoImage
        # global topmost_button
        # global topmost
        global data
        if topmost_button['text'] == '置顶':
            data["topmost"] = True
            topmost_button['text'] = '取消置顶'
            topmost_button['image'] = topmost_true_PhotoImage
        else:
            data["topmost"] = False
            topmost_button['text'] = '置顶'
            topmost_button['image'] = topmost_false_PhotoImage
        root.attributes('-topmost', data["topmost"])  # 处于顶层(更新状态)
    
    # global topmost_true_PhotoImage
    # global topmost_false_PhotoImage
    # global topmost_button
    try:
        topmost_true_PhotoImage = tk.PhotoImage(file=f'.{os.sep}data{os.sep}topmost_true.png')
    except:
        topmost_true_PhotoImage = None
    try:
        topmost_false_PhotoImage = tk.PhotoImage(file=f'.{os.sep}data{os.sep}topmost_false.png')
    except:
        topmost_false_PhotoImage = None
    topmost_button = tk.Button(
        set_up_frame,
        text='取消置顶' if data["topmost"] else '置顶',
        image=topmost_true_PhotoImage if data["topmost"] else topmost_false_PhotoImage,
        fg=data["foreground"],
        bg=data["background"],
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

    try:
        fix_true_PhotoImage = tk.PhotoImage(file=f'.{os.sep}data{os.sep}fix_true.png')
    except:
        fix_true_PhotoImage = None
    try:
        fix_false_PhotoImage = tk.PhotoImage(file=f'.{os.sep}data{os.sep}fix_false.png')
    except:
        fix_false_PhotoImage = None
    fix_button = tk.Button(
        set_up_frame,
        text='固定',
        image=fix_false_PhotoImage,
        fg=data["foreground"],
        bg=data["background"],
        command=change_fix,
        )
    fix_button.grid(row=0, column=2)
    createToolTip(fix_button, '固定')
    
    try:
        exit_PhotoImage = tk.PhotoImage(file=f'.{os.sep}data{os.sep}exit.png')
    except:
        exit_PhotoImage = None
    exit_button = tk.Button(set_up_frame, text='退出', image=exit_PhotoImage,
        fg=data["foreground"],
        bg=data["background"],
        command=save_exit,
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
    
    root.overrideredirect(data["overrideredirect"])  # 隐藏掉窗口边框和标题栏
    root.attributes('-toolwindow', data["toolwindow"])  # 置为工具窗口(没有最大最小按钮)
    root.attributes('-alpha', data["alpha"])  # 透明度(0.0~1.0)
    root.attributes('-topmost', data["topmost"])  # 处于顶层
    if data["transparentcolor"][0]:
        # 这一行可以将所有的白色透明掉
        root.attributes("-transparentcolor", data["transparentcolor"][1])
    
    t =  threading.Thread(target=change_information_threading) # , args=(old_verson, ))
    t.setDaemon(True)  # 设置线程为守护线程
    t.start()
    
    root.mainloop()

def main():
    try:
        global data
        data = read_data(json_data_file, default_data)
        GUI()
    except:
        show_error(traceback.format_exc())

if __name__ == '__main__':
    main()
