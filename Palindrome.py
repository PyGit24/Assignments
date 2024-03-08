# program that takes a string and returns True if it is a palindrome, False otherwise
x="malayalam"
w = ""
for i in x:
    w = i + w
print("The Given Input is: ",x)
if (x == w):
    print("True. The Given input",'"',x,'"',"is a Palindrome")
else:
    print("False. The Given input",x, "is not a Palindrome")