import sys
import re

with open(sys.argv[1],'r') as file1:
    text = file1.readlines()


text2 = []
check1 = "//"
check2 = "/*"
check3 = "*/"
check4 = "/**"
check5 = "*"
length = len(text)

for i in range(length):
    curr = text[i]
    find1 = curr.find(check1)
    find2 = curr.find(check2)
    find3 = curr.find(check3)
    find4 = curr.find(check4)
    find5 = curr.find(check5)
    
    if find1 != -1:
        text2.append(curr[:find1])
    elif find2 != -1:
        text2.append(curr[:find2])  
    elif find3 != -1:
        text2.append(curr[find3 + 2:]) 
    elif find4 != -1:
        text2.append(curr[find4 + 1:]) 
    elif find5 != -1:
        text2.append(curr[:find5])
    else:
        text2.append(curr)  

new = ''.join(text2)

filename = sys.argv[1]
filename = filename[:-4]
extension = "nocom"
newname = filename + extension

nocom = open(newname,"w+")
nocom.write(new)
nocom.close()
nocom = open(newname,"r+")
nocomtxt = nocom.read()
print (nocomtxt)
nocom.close()


def balanced():
    stack = []
    not_balanced = "File is not balanced"
    for j in range(len(nocomtxt)):
        if nocomtxt[j] == "{" or nocomtxt[j] == "(" or nocomtxt[j] == "[":
            stack.append(nocomtxt[j])
        if nocomtxt[j] == "}":
            if len(stack) == 0:
                return not_balanced
            if stack[len(stack)-1] == "{":
                stack.pop()
            else:
                return not_balanced 
        if nocomtxt[j] == ")":
            if len(stack) == 0:
                return not_balanced
            if stack[len(stack)-1] == "(":
                stack.pop()
            else:
                return not_balanced
        if nocomtxt[j] == "]":
            if len(stack) == 0:
                return not_balanced
            if stack[len(stack)-1] == "[":
                stack.pop()
            else:
                return not_balanced
    if len(stack) == 0:
        return "File is balanced"
    else:
        return not_balanced
result = balanced()
print(result)                        