import requests
import zipfile
import tempfile
import re
import os
import shutil
import win32api
import win32con
import win32file
# win32file.CopyFile ("移動copy.py", "新檔名", 1)
# win32file.DeleteFile ("移動copy.py")

def get_data():
    url = "https://codeload.github.com/jx06T/Update_repository_with_python/zip/refs/heads/main"
    payload = {}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.example.com/', 
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return url, response.content
 


def CheckUpdata():
    url = "https://github.com/jx06T/Update_repository_with_python/blob/main/README.md"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    rule = r"version-(V[\d|'.']*)"
    V =  re.findall(rule,response.text)
    if len(V)>0:
        V = V[0]
    else:
        return False
    with open("version_record.text", "rt",encoding='UTF-8') as f:
        record = f.read()
        lastV = re.findall(rule,record) 
        if len(lastV)>0 and not lastV[0]==V:
            print("!!")
        elif len(lastV)==0:
            print("!!!")
        else :
            return False
        
    with open("version_record.text", "w",encoding='UTF-8') as f:
        # f.write("version-"+V)
        return True

def save():

    current_path = os.path.dirname(os.path.abspath(__file__)) 
    new_folder = '_temp'
    R_PATH = "Update_repository_with_python-main"

    if os.path.exists(new_folder):
        shutil.rmtree(new_folder)
        os.mkdir(new_folder)
    else:
        os.mkdir(new_folder)

    # win32api.MoveFileEx("_UpData.py", new_folder+"/_UpData.py", win32con.MOVEFILE_REPLACE_EXISTING)

    for file_name in os.listdir(current_path):
        destination = os.path.join(new_folder, file_name)
        print(file_name,destination)
        if file_name=="_temp" :
            continue  
        shutil.move(file_name, destination)

    url, data = get_data()  # data为byte字节
 
    _tmp_file = tempfile.TemporaryFile()  # 创建临时文件
    print(_tmp_file)
    _tmp_file.write(data)  # byte字节数据写入临时文件
    zf = zipfile.ZipFile(_tmp_file, mode='r')
    oldNames = []
    for names in zf.namelist():
        oldNames.append(names)
        f = zf.extract(names, './')  # 解压到zip目录文件下
        print(f)
    zf.close()

    for name in oldNames:
        NewName = name.replace(R_PATH+"/","")
        print(NewName,name)
        if os.path.exists(NewName):
            try:
                os.remove(NewName)
            except:
                continue
        try:
            os.rename(name, NewName)
        except:
            pass

    if os.path.exists(R_PATH):
        shutil.rmtree(R_PATH)
        
def UpData():
    if CheckUpdata():
        save()

if __name__ == '__main__':
    UpData()

