import re
priorities = {"(" : 5, ")" : 0, "!" : 3, "&" : 2, "|" : 1}
#print("Use ! for NOT, & for AND, and | for OR")
exp = input("Enter the expression in infix: ")
wordlist = exp.split()
exp = exp.replace(" and ", " & ")
exp = exp.replace(" or "," | ")
#print (wordlist)
#exp = exp.replace(" ", "")
i = 0
j = 0
a = ""
exparr = []
print (range(len(exp)))
for c in exp:
        while((i < len(exp)) and ((c != "&") or (c != "|") or (c != "!"))):
                a = a + c
                i = i + 1
        #j = j+1
        exparr.append(a)
        #j = j+1
        if i < len(exp):
                exparr.append(exp[i])
                i = i+1
        #j = j+1
print(exparr)
        
stack = []
outputExp = ""
for ch in exp:
	if ch not in priorities: outputExp += ch + " "
	else:
		while stack and stack[-1] != "(" and priorities[stack[-1]] >= priorities[ch]:
			outputExp += stack.pop() + " "
		if ch != ')':	stack.append(ch)
		else:
			while stack and stack[-1] != '(':
				outputExp += stack.pop() + " "
			stack.pop()
while stack:
	outputExp += stack.pop() + " "
print(outputExp)
