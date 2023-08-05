import requests
import zipfile
import tempfile
import re
import os
import shutil
import tkinter as tk
from tkinter import messagebox

R_PATH = "Update_repository_with_python-main"
DOWNLOAD_URL= "https://codeload.github.com/jx06T/Update_repository_with_python/zip/refs/heads/main"
CHECK_URL= "https://github.com/jx06T/Update_repository_with_python/blob/main/README.md"
VERSION_FILE_NAME = "_version.text"
TEMP_FILE_NAME = "_temp"
current_path = os.path.dirname(os.path.abspath(__file__)) 
NewVersion = None
LastVersion = None

def get_data():
    payload = {}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    response = requests.request("GET", DOWNLOAD_URL, headers=headers, data=payload)
    return DOWNLOAD_URL, response.content

def CheckUpdata():
    global NewVersion
    global LastVersion
    payload = {}
    headers = {}
    response = requests.request("GET", CHECK_URL, headers=headers, data=payload)
    rule = r"version-(V[\d|'.']*)"
    V =  re.findall(rule,response.text)
    if len(V)>0:
        NewVersion = V[0]
    else:
        return False,False
    
    if os.path.isfile(VERSION_FILE_NAME):
        with open(VERSION_FILE_NAME, "rt",encoding='UTF-8') as f:
            record = f.read()
            lastV = re.findall(rule,record) 
            LastVersion = lastV[1]
            lastV.append(None)
            if  lastV[0]==NewVersion:
                return False,record

    return True,record

def UpDataSuccess(record,version):
    with open(VERSION_FILE_NAME, "w",encoding='UTF-8') as f:
        f.write("version-"+version+'\n'+record)

def SaveNewData():
    url, data = get_data()  # data为byte字节
    _tmp_file = tempfile.TemporaryFile()  # 创建临时文件
    print(_tmp_file)
    _tmp_file.write(data)  # byte字节数据写入临时文件
    zf = zipfile.ZipFile(_tmp_file, mode='r')
    for names in zf.namelist():
        f = zf.extract(names, './')  # 解压到zip目录文件下
        print("add =>", f)
    zf.close()

def MoveDataBack(_from):
    for name in os.listdir(os.path.join(current_path,_from)):
        NewName = name
        name = os.path.join(_from,name)
        print("move => ",name)
        os.rename(name, NewName)
    shutil.rmtree(_from)

def MoveData(_to):
    if os.path.exists(_to):
        shutil.rmtree(_to)
        os.mkdir(_to)
    else:
        os.mkdir(_to)
    for file_name in os.listdir(current_path):
        destination = os.path.join(_to, file_name)
        if file_name==TEMP_FILE_NAME or file_name==VERSION_FILE_NAME:
            continue  
        print("move => ",file_name)
        shutil.move(file_name, destination)

def DeleteData(name):
    for file_name in os.listdir(os.path.join(current_path,name)):
        if file_name==TEMP_FILE_NAME or file_name==VERSION_FILE_NAME:
            continue  
        print("delete => ",file_name)
        if os.path.isdir(file_name):
            shutil.rmtree(file_name)
        else:
            os.remove(file_name)

if __name__ == '__main__':
    CanUpdata,record = CheckUpdata()
    if CanUpdata:
        result = messagebox.askokcancel('Update Tools', "有可用更新("+NewVersion+")\n\n是否下載更新？")
        if result:
            MoveData(TEMP_FILE_NAME)
            SaveNewData()
            MoveDataBack(R_PATH)
            messagebox.showinfo('Update Tools', '已更新至最新版('+NewVersion+')')
            UpDataSuccess(record,NewVersion)
        else:
            print("Not Now UpData")
    else:
        if record == False:
            messagebox.showwarning('Update Tools', '無法確認是否有更新版本')
        else:
            result = messagebox.askokcancel('Update Tools', "已經是最新版("+NewVersion+")\n\n是否要還原更新？(to "+LastVersion+")")
            if result:
                DeleteData(current_path)
                MoveDataBack(TEMP_FILE_NAME)
                messagebox.showinfo('Update Tools', '已還原至舊版('+LastVersion+')')
                UpDataSuccess(record,LastVersion)
            else:
                print("Nothing")
