import requests
import zipfile
import tempfile
import re
import os
    # f = os.open('demo/demo.txt', os.O_RDWR|os.O_CREAT)   # 建立一個可讀寫的 demo.txt



def get_data():
    url = "https://codeload.github.com/jx06T/FindBook3/zip/refs/heads/main"
    payload = {}
    headers = {
    'authority': 'codeload.github.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': '_octo=GH1.1.909076288.1685718751; tz=Asia%2FTaipei; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=jx06T; preferred_color_mode=dark',
    'dnt': '1',
    'if-none-match': 'W/"88eb8acf462dfcd24d1eeacc1f20025c3bb1a22a473b170b8beb025a6a1914af"',
    'referer': 'https://github.com/jx06T/FindBook3',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return url, response.content
 


def CheckUpdata():
    url = "https://github.com/jx06T/Update_repository_with_python/blob/main/README.md"

    payload = {}
    headers = {
    'Cookie': '_gh_sess=yrhsh%2FQQ7yZCSPGnCn3ao8dMBnxcWC3hwuUi%2F79CN8Xxk3KNXphs%2FEMUpRUwHUdDWW8Z%2BBkc1MKnDRGt7%2Bx1OafPzUHdaRtKjIH5Qaz0F54xRqu2ER3vNqfeNrF0Emkpq2wHI0DySfQ3VvawP9mhVXLYzZCXnMQHgNIXiivtgK3NnjxmWaQPy4KEGgGev3PIWEvvdQqsOY4rkRREmidY6iI4kQ5SF801JKsRo5vt8EAGc6VFd3b5Mpbww9ZfR%2B8v0tUCHsj%2BpKF5724OPAv37w%3D%3D--H55d0j9%2FM3Ktix1z--VBcsToN38iwKRPOoTrTMMA%3D%3D; _octo=GH1.1.1270137357.1691156003; logged_in=no'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    rule = r"version-(V[\d|'.']*)"
    V =  re.findall(rule,response.text)
    if len(V)>0:
        V = V[0]
    print(V)
    with open("version_record", "r") as f:
        lastV =  re.findall(rule,f.read()) 
        if len(lastV)>0 and not lastV[0]==V:
            print(lastV[0])
            print("!!")
        if len(lastV)==0:
            f.write("version-"+V)
            print("!!!")

        f.close()


if __name__ == '__main__':


    CheckUpdata()

    # url, data = get_data()  # data为byte字节
 
    # _tmp_file = tempfile.TemporaryFile()  # 创建临时文件
    # print(_tmp_file)
 
    # _tmp_file.write(data)  # byte字节数据写入临时文件
 
    # zf = zipfile.ZipFile(_tmp_file, mode='r')
    # for names in zf.namelist():
    #     f = zf.extract(names, './')  # 解压到zip目录文件下
    #     print(f)
 
    # zf.close()
