from mainFunc import *

txtPath, htmlString  = argParse()
print(htmlString)

stackPDA = []
arrTag = tagParse(htmlString=htmlString)

print(arrTag)

