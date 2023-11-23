import os
import argparse
from typing import List


def argParse() -> tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("txt", type=str, help="txt file path")
    parser.add_argument("html", type=str, help="html file path")
    txtArg = parser.parse_args().txt
    htmlArg = parser.parse_args().html.replace("\"", "")

    if (txtArg == None or htmlArg == None):
        print("Argument kurang lengkap! Silahkan jalankan dengan format `python main.py file.txt \"html.txt\"`")
        exit()
    
    if not os.path.isfile(htmlArg):
        print("tidak ditemukan file html yang dimaksud")
        exit()
    
    return (txtArg, open(htmlArg, "r").read())


# fungsinya buat html (bentuk string) jadi array of tag and argument
def tagParse(htmlString:str) -> List[any]:
    isTag = False
    arrTag = []
    line = 1
    stringTemp = ""
    for i in htmlString:
        if i == "<":
            if (stringTemp != ""):
                arrTag.append((line, stringTemp))
            stringTemp = ""
            stringTemp += i
            isTag = True
        elif i == ">":
            stringTemp += i
            arrTag.append((line, stringTemp))
            stringTemp = ""
            isTag = False
        elif isTag:
            stringTemp += i
        elif (i != " ") and (i != "\n"):
            stringTemp += i
        if i == "\n":
            line += 1
    return arrTag


# fungsinya kurleb bikin <a href=""> jadi ["a", "href=\"\""]
def TagClassSeparator(stringArg : str) -> List[str]:
    strTemp = ""
    ArrRes = []
    for i in stringArg:
        if (i == ">" or i == " ") and strTemp != "":
            ArrRes.append(strTemp)
            strTemp = ""
        else:
            if (i != "<") and (i != "\n") and (i != " "):
                strTemp += i
    return ArrRes

