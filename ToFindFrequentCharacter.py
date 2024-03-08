# Program that takes a string and returns the most frequent character in it
st1="Python automation"
rep={}
print ("The String is:", st1)
for character in st1:
    if character in rep:
        rep[character] +=1
    else:
       rep[character]=1
rep_str=max(rep,key=rep.get)
print("The frequent or repeated characters are: "+ str(rep_str))