from mainFunc import *
from PDA import *

txtString, htmlString  = argParse()

stackPDA = []
arrTag = tagParse(htmlString=htmlString)
states, inputs, stacks, initial_state, initial_stack, accept_state, accept_condition, transition = txtParse(txtString)


# kamus variabel
i:int = 0
isAccept:bool = True
inputTag = []
lineFalse:int = -1
tagFalse:any = None

# PDA
mainPDA = PDA(states, inputs, stacks, initial_state, initial_stack, accept_state, accept_condition, transition)

# program main
while(i < len(arrTag) and isAccept):
    if (arrTag[i][1] != '<!DOCTYPE html>'):
        inputTag = TagClassSeparator(arrTag[i][1])
        isAccept = mainPDA.run(inputTag)
        if (isAccept == False):
            tagFalse = arrTag[i]
    i+=1

if isAccept:
    print("acc")
else:
    print("ga acc")

