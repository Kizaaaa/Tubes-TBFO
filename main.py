from mainFunc import *
from PDA import *

txtString, htmlString  = argParse()

stackPDA = []
arrTag = tagParse(htmlString=htmlString)
states, inputs, stacks, initial_state, initial_stack, accept_state, accept_condition, transition = txtParse(txtString)
print(txtParse(txtString=txtString))
# print(arrTag)
# print(TagClassSeparator(arrTag[7][1]))

