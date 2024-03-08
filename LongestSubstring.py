# program that takes two strings and returns the longest common substring between them
in1="I am Shor"
in2="I am Long"
#for i in len(in1):
print("To Find the longest of two strings")
print("The First input is:",in1)
print("The Second input is:",in2)
if len(in1)== len(in2):
    print("Both the inputs have equal length")
elif len(in1)>= len(in2):
    print("The First Input",'"',in1,'"',"is Long")
elif len(in2)>=len(in1):
    print("The Second Input",'"',in2,'"', "is Long")
else:
    print("Inputs are not Equal")