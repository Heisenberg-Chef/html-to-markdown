# -*- coding:utf-8 -*-
import re
'''
python3.8.2
html中的table表格转换成markdown模式
此举还是方便我们后期整理笔记
'''

# C 语言封装
SRC = r"./src.txt"
TAR = r"./tar.txt"


def analyze(html,fout):
    #   html = html.replace("\n","")
    # html = html.replace(" ","")
    html = html.replace("<br>","")
    res = re.findall(r"(?:[\s\S]*?)<tbody(?:.*)>([\s\S]*?)</tbody>(?:[\s\S]*?)",html)
    for lists in res:
        tmp_tr = re.findall(r"(?:[\s\S]*?)<tr(?:[\s\S]*?)>([\s\S]*?)</tr>(?:[\s\S]*?)",lists)
        # tmp_tr is linear list
        count = 0
        for part in tmp_tr:         # one loop equal one column
            count += 1
            tmp_td = re.findall(r"(?:[\s\S]*?)<td(?:[\s\S]*?)>([\s\S]*?)</td>(?:[\s\S]*?)",part)
            print("|",file=fout,end="")           
            for i in tmp_td:
                i = i.replace("\n","")
                print(" {} |".format(i),file=fout,end="")
            if count == 1:
                print("\n",file=fout,end="")
                print("|" + " --- |"*len(tmp_td),file=fout,end="")
            print("\n",file=fout,end="")
        print("\n"*2)
            
    
if __name__ == '__main__':
    #   打开文件
    print("") 
    print("+"*30)
    try:
        fin = open(SRC,"r")
    except FileNotFoundError:
        print("*"*15)
        print("File <src.txt> no found...\
              \nI create a new empty file for you.\
              \nCopy your html code into it then try run me again.\n")
        fin = open(SRC,"r+")
        exit(1)
        
    try:
        fout = open(TAR,"w+")
    except Exception:
        print("Could not create a <tar.core> file.\n")
#   数据缓存
    html = fin.read()
    analyze(html,fout)  #   linear list
    del(html)
    fout.seek(0)
    print(fout.read())
    fout.close()
    fin.close()


