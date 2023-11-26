from mainFunc import *
from PDA import *

txtString, htmlString  = argParse()

stackPDA = []
arrTag = tagParse(htmlString=htmlString)
states_input, inputs_input, stacks_input, initial_state_input, initial_stack_input, accept_state_input, accept_condition_input, transitionLists = txtParse(txtString)


# kamus variabel
i:int = 0
isAccept:bool = True
inputTag:any = []
lineFalse:int = -1
tagFalse:any = None

# PDA
mainPDA = PDA(states_input, inputs_input, stacks_input, initial_state_input, initial_stack_input, accept_state_input, accept_condition_input, transitionLists)

# program main
while((i < len(arrTag)) and (isAccept == True)):
    if (arrTag[i][1] != '<!DOCTYPE html>'):
        inputTag = TagClassSeparator(arrTag[i][1])
        for j in inputTag:
            isAccept = mainPDA.run(j)
            if not isAccept:
                break
        if (isAccept == False):
            tagFalse = [arrTag[i], i]
    i+=1

if isAccept:
    print("verdict : Accepted")
else:
    print("verdict : Not Accepted")
    print(f"error at line {tagFalse[0][0]} : \"", end="")
    for i in range(len(arrTag)):
        if arrTag[i][0] == tagFalse[0][0]:
            if i == tagFalse[1]:
                print('\033[91m' + arrTag[i][1] + '\033[0m', end="")
            else:
                print(arrTag[i][1], end="")
    print("\"")

print(TagClassSeparator(arrTag[15][1]))