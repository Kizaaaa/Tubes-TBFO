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
while(i < len(arrTag) and isAccept):
    if (arrTag[i][1] != '<!DOCTYPE html>'):
        inputTag = TagClassSeparator(arrTag[i][1])
        for j in inputTag:
            isAccept = mainPDA.run(j)
        if (isAccept == False):
            tagFalse = arrTag[i]
    i+=1


if mainPDA.isAccept():
    print("acc")
else:
    print("ga acc")
    print(tagFalse)
print(arrTag)