import time
import json
from traceback import format_exc  #用于精准的获取错误异常
import requests


def get_id(book_name):
    url = "https://www.jiumodiary.com/init_hubs.php"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    data = {
        "q": book_name,
        "remote_ip": "",
        "time_int": int(time.time())}
    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    book_id = json.loads(response.text)["id"]
    # print(book_id)
    return book_id

def get_book_data(book_name):
    book_id = get_id(book_name)
    # url = "https://www2.jiumodiary.com/ajax_fetch_hubs.php"
    url = "https://www.jiumodiary.com/ajax_fetch_hubs.php"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
    data = {
        "id": book_id,
        "set": 0}
    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    sources = json.loads(response.text)["sources"]
    datas = []
    for data in sources:
        try:
            for i in data["details"]["data"]:
                datas.append({
                    "title": i["title"],
                    "des": i["des"],
                    "link":i["link"]})
        except:
            # print(format_exc())
            pass
    # print(datas)
    return datas
    
def get_book_information(book_name):
    datas = get_book_data(book_name)
    information = f"共查询到{len(datas)}条结果，共耗时{round(time.time()-now_time, 2)}s\n"
    for data in datas:
        if data['des'] == "":
            information += f"{data['title']}\n{data['link']}\n\n"
        else:
            information += f"{data['title']}\n{data['des']}\n{data['link']}\n\n"
    return information
    

def main():
    global now_time
    book_name = input("请输入你要搜索的电子书：")
    now_time = time.time()
    information = get_book_information(book_name)
    print(information)


if __name__ == "__main__":
    main()
