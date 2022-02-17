
#Assignment 3
#Code for searching Psalms chapter and verse
#i will first call for the bible.txt file which i have named biblePsalms


biblePsalms = open('bible-psalms.txt', 'r')
#the i will ask for input for the chapter that the user wants and the verse the user wants
c = input('What Book of Psalms chapter? ')
v = input('What Book of Psalms verse within the chapter? ')
#
cvConcatination = c + ':' + v 

#this i variable is a column counter
foundVerse = False

#in my for loop, the idea was to parse the strings and to display the 
#verse if the reference matched with the right verse with the incriment increase of 1
#as far as how many times the loop will continue.
#also the idea was to make sure that the verse in the line variable matched the 
for line in biblePsalms:
    splitList1 = line.split('\t')
    splitList2 = splitList1[0].split(' ')
    psalmsVerse = splitList1[1]
    psalmsRef = splitList2[1]
   
    if cvConcatination == psalmsRef:
        foundVerse = True
        break

if foundVerse == True:
    print(psalmsVerse)
else:
    print("Not found")
    
#then i close the file and exit the program
biblePsalms.close()
exit()