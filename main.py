 
size = 0
 
""" Here I made a bunch of temp variables to use for the while loop. """ 
 
tempVariable1 = 1 
tempVariable2 = 2
tempVariable3 = 3
while True:
    try:
       size = int(input("Input the amount of characters you want to move: "))
       if (size == tempVariable1) or tempVariable2 or tempVariable3:
           break
       else:
          print("Number must be between 1 and 3")
    except:
       print("Please try again")
       
sentence = input("Please enter a word, phrase or sentence: ")
print(str.split(sentence," "))
 
consonants = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
 
print("your phrase is: ", sentence)
 
sentenceChoppa = sentence.split()
 
for word in sentenceChoppa:
  if (word[0] in vowels):
    print (word + 'way')
  elif (word[0:3] in consonants):
    print (word[3:] + word[0:3] + 'ay')
  elif (word[0:2] in consonants):
    print(word[2:] + word[0:2] + 'ay')
  else:
    print(word[1:] + word[0:1] + 'ay')
