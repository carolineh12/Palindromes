##########################################
#Program 9
#Caroline Holland
#November 19, 2022
##########################################
#Subroutine
def iterate(word):
    #if length of the list is 0, then it's a palindrome
    if len(word)==0: #basecase
        return True
    #if two end letters are equal, remove from list and put the new list through the subroutine
    elif word[0] == word[-1]:
        return iterate(word[1:-1]) #Sofia Whelchel
    #if character is a non letter, remove from list and put new list through subroutine
    elif word[0] != word[-1]:
        if word[0].isalpha()==False:
            return iterate(word[1:])
        if word[-1].isalpha()==False:
            return iterate(word[0:-1])
    else:
        return False
            
#MAIN PROGRAM
from sys import stdin, stdout
file= open("palindrome.txt")
datalist= []
for i in file:
    #get rid of beginning new line and add each word/phrase to an array
    strip= i.rstrip("\n")
    datalist.append(strip)
#empty list for palindromes
newlist = []
for line in datalist:
    lowLine=line.lower()
    #put each character in the line in an array
    character=[]
    for char in lowLine:
        character.append(char)
    #put the character array through the subroutine
    test= iterate(character)
    #if the word/phrase is a palindrome, add to newlist
    if test == True:
        newlist.append(line)
newlist.sort()
print("There are {} palindromes out of {} phrases: ".format(len(newlist),len(datalist)))
#print all palindromes
for x in newlist:
    print(x)
    

    



