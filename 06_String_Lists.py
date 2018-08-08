#Get user input
word = input("Give me a word: ")
#Store this as a string
wrd = str(word)

#Reverse the word and store as variable rvs
rvs = wrd[::-1]

#Compare wrd string to rvs string
if wrd == rvs:
    print("The word " + wrd + " is a Palindrome")
else:
    print("This word " + wrd + " is NOT a Palindrome")
