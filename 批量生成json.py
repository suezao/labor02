#@190818CHENSHUZAO
#逐行读取名称所在TXT，把每个名称生成JSON，（变量所在为主要）
#读取模板写入，
def ReadTXT(JSON,MODEL,TXT):
    with open(TXT,'r',encoding='utf-8')as TXT:
        lines=TXT.readlines()
        with open (JSON,'a',encoding='utf-8')as iJSON:
            iJSON.write("[")
        for line in lines:
            ModelJson(JSON,MODEL,line)
        with open (JSON,'a',encoding='utf-8')as iJSON:
            iJSON.write("\n]")
def ModelJson(JSON,MODEL,NAME):
    with open (JSON,'a',encoding='utf-8')as JSON:
        with open(MODEL, 'r',encoding='utf-8')as MODEL:
            iMODELs=MODEL.readlines()
            for iMODEL in iMODELs:
                if iMODEL.find("名称:")>0:
                    JSON.write(iMODEL.replace(",",NAME.replace("\n","")+","))
                else:
                    JSON.write(iMODEL)
JSON=input("生成文件所在目录")
MODEL="C:\\Users\\Wu\\Desktop\\moban.json"
TXT="C:\\Users\\Wu\\Desktop\\333.txt"
ReadTXT(JSON,MODEL,TXT)
print("OK")
