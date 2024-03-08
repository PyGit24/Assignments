#Program to find Anagram or not
def anag(str1,str2):
    return sorted(str1)==sorted(str2)
st1=input("Enter the First String: ")
st2=input("Enter the Second String: ")
if anag(st1,st2):
    print("True")
else:
    print("False")
