from mainFunc import *

txtPath, htmlString  = argParse()
print(htmlString)

stackPDA = []
arrTag = tagParse(htmlString=htmlString)

print(arrTag)

print(TagClassSeparator(arrTag[7][1]))

