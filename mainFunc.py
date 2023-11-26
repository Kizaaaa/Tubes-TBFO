import os
import argparse
from typing import List

class Stack:
    def __init__(self, buffer:List[any], idxTop:int) -> None:
        self.buffer = buffer
        self.idxTop = idxTop
        
    def Top(self) -> any:
        if (self.idxTop == -1):
            return None
        else:
            return (self.buffer[self.idxTop])

    def push(self, toBePushed:any):
        self.buffer.append(toBePushed)
        self.idxTop += 1

    def pop(self) -> any:
        toBeRet = self.buffer.pop()
        self.idxTop -= 1
        return toBeRet
    
    def length(self) -> int:
        return (len(self.buffer))
    
    def isEmpty(self) -> bool:
        return (self.idxTop == -1)
    
    def DisplayStack(self):
        print(self.buffer)
        

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
    
    return (open(txtArg, "r").read(), open(htmlArg, "r").read())


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


def txtParse(txtString:str) -> List[any]:
    line = 1
    stopCopy = False
    states = []
    inputs = []
    stacks = []
    initial_state = []
    initial_stack = []
    accept_state = []
    accept_condition = []
    transition = []
    txtTemp = ""
    for i in txtString:
        if i == "\n":
            stopCopy = False
            if line == 1:
                states = list(txtTemp.split())
            elif line == 2:
                inputs = list(txtTemp.split())
            elif line == 3:
                stacks = list(txtTemp.split())
            elif line == 4:
                initial_state = txtTemp.replace(" ", "")
            elif line == 5:
                initial_stack = txtTemp.replace(" ", "")
            elif line == 6:
                accept_state = txtTemp.replace(" ", "")
            elif line == 7:
                accept_condition = txtTemp.replace(" ", "")
            else:
                transition.append(list(txtTemp.split()))
            txtTemp = ""
            line += 1
        elif i == "#":
            stopCopy = True
        elif not stopCopy:
            txtTemp += i
    
    return states, inputs, stacks, initial_state, initial_stack, accept_state, accept_condition, transition

