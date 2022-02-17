"""
Program: textanalysis.py
Author: Ken
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.


***MODIFIED BY CHRISTIAN FULLER***


"""

#Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, "r")
text = inputFile.read()

#Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') +\
            text.count('!')

#Count the words
words = len(text.split())
'''
when counting the syllables, i needed to to somehow connect the strings aeiouAEIOU to a count or an integer.
this was very hard to do and im still not sure if i did this right but that remains to be seen.
in my modification, i added variables vowelCount and vowelLimit.
since we know that consecutive vowels consist of 2 or more vowels together, i needed to set that value as a variable.
from there, i used the following if statements:

if vowelLimit <= 1:
            syllables -= 1
            if vowelLimit >= 2:
                syllables = 1
                
the idea was if the vowel limit is 1 then the syllable counter would change.
then, if the vowl limit was greater than 2 (above the limit) then the syllable counter would stay at count 1.
i did much better on the first problem but let me know what i can do better.

for context:

    original syllable count: 57807
    after my modification: 57641
'''

#Count the syllables
syllables = 0 
vowels = "aeiouAEIOU"
vowelCount = 10
vowelLimit = 1
for word in text.split():
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
        if vowelLimit == 1:
            syllables -= 1
            if vowelLimit >= 2:
                syllables -= 1

#Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
    84.6 * (syllables / words)
level = round(0.39 * (words / sentences) + 11.8 * \
    (syllables / words) - 15.59)

#Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")