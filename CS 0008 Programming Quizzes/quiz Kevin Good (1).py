# Code by Kevin Good
count = 0
word = input("Enter a word: ")
word = word.lower()
count2 = len(word)
if count2 == 1:
    if word == "i" or word == "a":
        print("It's a palindrome!")
    else:
        print("Not a Palindrome")
while word[count] == word[count2-1-count] and count2 > 1:
    count = count + 1
    if count == count2 - 1:
        print("It's a palindrome!")
        break
if word[count] != word[count2-1-count]:
    print("Not a palindrome")
    
    
      
      
    
    
    
    
    
