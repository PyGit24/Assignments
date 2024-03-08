# Removing vowels from a string
def remove_vowels(text): 
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 
    no_vowel = "" 
    for char in text: 
        if char not in vowels: 
            no_vowel += char 
    return no_vowel 
in_string = "interpreter, computer" 
out_string = remove_vowels(in_string) 
print(out_string)