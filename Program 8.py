##########################################
#Program 8
#Caroline Holland
#November 8, 2022
##########################################
#Subroutine
def iterate(word):
    #change to lowercase
    lowercase=word.lower()
    #location of letter in the word/phrase
    first_position=0
    last_position=len(lowercase)-1
    #https://datagy.io/python-palindrome/
    while first_position<=last_position:
        #the value at the location
        first_value= lowercase[first_position]
        last_value= lowercase[last_position]
        #https://careerkarma.com/blog/python-isalpha-isnumeric-isalnum/#:~:text=In%20other%20words%2C%20isalpha%20%28%29%20checks%20if%20a,contains%20a%20space%2C%20the%20method%20will%20return%20False.
        #if a non alphabet character, skip and change value 
        while first_value.isalpha()== False:
            first_position+=1
            first_value = lowercase[first_position]
        while last_value.isalpha()== False:
            last_position-=1
            last_value = lowercase[last_position]
        #if first and last are equal, move inwards to compare the next two values 
        if first_value==last_value:
           first_position+=1
           last_position-=1
        else:
            return False 
    return True
      
#MAIN PROGRAM
from sys import stdin, stdout
file= open("phrases.txt")
datalist= []
for i in file:
    #get rid of beginning new line and add each word/phrase to an array
    strip= i.rstrip("\n")
    datalist.append(strip)
#empty list for palindromes
newlist = []
#run each word/phrase in the datalist through the subroutine
for line in datalist:
    test= iterate(line)
    #if the word/phrase is a palindrome, add to newlist
    if test == True:
        newlist.append(line)
print("There are {} palindromes out of {} phrases: ".format(len(newlist),len(datalist)))
#print all palindromes
for x in newlist:
    print(x)
    

    


