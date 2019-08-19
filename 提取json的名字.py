#@190818CHENSHUZAO
import shutil
import os
def ChangeInfo(before,after):
    with open(before,'r',encoding='utf-8')as f1:
        with open(after,'a+',encoding='utf-8')as f2:
            lines_a=f1.readlines()
            for line_a in lines_a:
                if line_a.replace('\n', '').find("名称:")>=0:
                    print(line_a)
                    f2.write(line_a.replace("		名称:",""))


before=input("请输入需要提取名称的json文件:\n（名称将保存在111.txt中）\n")
after="C:\\Users\\Administrator\\Desktop\\111.txt"
ChangeInfo(before.replace("\n","").replace("\r",""),after)

