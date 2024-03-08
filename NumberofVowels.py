# program to calculate the total numbers of vowels and count 
# of each individual vowel AEIOU in the string Guvi Geeks Network private limited
def find_vowel(inputext, vowels):
    count = {}.fromkeys(vowels,0)

        # To count the vowels
    for character in inputext:
            if character in count:
                count[character] += 1
    return count
vowels = 'aeiouAEIOU'
inputext = "Guvi Geeks Network private limited"
print(find_vowel(inputext, vowels))