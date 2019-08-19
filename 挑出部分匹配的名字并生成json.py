#@190819CHENSHUZAO
import os
def cycle(TXT):
    with open(TXT,'w',encoding='utf-8')as TXT:
        for i in range(1,101):
            before=input("请输入num前的汉字")
            TXT.write(before)
            #TXT.write(str(i)+"\n")
            TXT.write("%03d"%(i))
            after=input("请输入num后的汉字")
            TXT.write(after+"\n")

def find(TXT,Before):
    with open(TXT,'w',encoding='utf-8')as TXT:
        with open(Before,'r',encoding='utf-8')as Before:
            same=input("（覆盖）请输入需要匹配的汉字：\n")
            lines=Before.readlines()
            for line in lines:
                if line.find(same)>=0:
                    print(line)
                    TXT.write(line.replace(",",""))
    print("findOK")
    
def ReadTXT(JSON,MODEL,TXT):
    with open(TXT,'r',encoding='utf-8')as TXT:
        lines=TXT.readlines()
        with open (JSON,'a',encoding='utf-8')as iJSON:
            iJSON.write("[")
        Discribe=input("(未覆盖）请输入描述：\n")
        for line in lines:
            ModelJson(JSON,MODEL,line,Discribe.replace("\n","").replace("\r",""))
        with open (JSON,'a',encoding='utf-8')as iJSON:
            iJSON.write("\n]")
def ModelJson(JSON,MODEL,NAME,Discribe):
    with open (JSON,'a',encoding='utf-8')as JSON:
        with open(MODEL, 'r')as MODEL:
            iMODELs=MODEL.readlines()
            for iMODEL in iMODELs:
                if iMODEL.find("名称:")>0:
                    JSON.write(iMODEL.replace(",",NAME.replace("\n","")+","))
                elif iMODEL.find("关键描述:")>0:
                    JSON.write(iMODEL.replace(",",Discribe.replace("\n","")+","))
                else:
                    JSON.write(iMODEL)
def main(TXT,Before,JSONroot,MODEL):
    find(TXT,Before)
    JSONname=input("请输入生成json名称：\n")
    JSON=os.path.join(JSONroot,JSONname+".json")
    ReadTXT(JSON,MODEL,TXT)
#cycle(TXT)
#TXT="C:\\Users\\Wu\\Desktop\\333.txt"
#Before="C:\\Users\\Wu\\Desktop\\111.txt"
#MODEL="C:\\Users\\Wu\\Desktop\\moban.json"
JSONroot="C:\\Users\\Administrator\\Documents\\Tencent Files\\1210319205\\FileRecv"
TXT="C:\\Users\\Administrator\\Desktop\\333.txt"
Before="C:\\Users\\Administrator\\Desktop\\111.txt"
MODEL="C:\\Users\\Administrator\\Desktop\\新建文本文档.txt"
while 1:
    main(TXT,Before,JSONroot,MODEL)