from GUI import * # 图形界面
#from jsondata import * # 用于保存数据
import jsondata # 用于保存数据



file = 'Students.txt'
names = []# 读取的姓名
name = ""# 当前抽取的姓名
havenames = []
lj = 0
# data = "data.txt"
zh = 90
donghua = False



# json数据文件名称/地址
json_data_file = 'data.json'
# 初始化数据

jsondata.data = {
    'lj': 0, # 累计人数
    'zh': 90, # 字号
    'file': 'Students.txt',# 姓名文件
    'background': "#66ff66",# 背景色
    'buttonbg': "#99ff99",# 按钮背景色
    'program_name': 'RandomRollCall',#程序名
    'program_path': jsondata.sys.argv[0],# 程序路径
    'verson': [1, 1, 0, 1],# 版本号
    'autor': '小喾苦',# 制作人
    'time': jsondata.time.strftime("%Y-%m-%d %H:%M:%S", jsondata.time.localtime()),# 时间
    'check_code': '',# 校验码
}
bbh = "%i.%i.%i.%i"%tuple([jsondata.data['verson'][i] for i in range(4)])# 版本号



if __name__ == '__main__':
    # 读数据
    jsondata.data = jsondata.read_data(jsondata.data, json_data_file)
    
    main()# 显示主窗口
    
    # 保存数据
    jsondata.save_data(jsondata.data, json_data_file)
