#program that takes a string and returns the number of unique characters in it
text = "I am strong and great"
unique_character = ""
for i in text:
    if i not in unique_character:
        unique_character += i
print("The Given String is:",text)
print("The Length of the string is:",len(text))
print("The Unique Count is: ",len(unique_character))
print("The Unique Character is: ",(unique_character))