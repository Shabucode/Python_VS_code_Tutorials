#string functions
print('Hello Shabnam\'') #'\ to escape qoutes or # ...or use double quotes instead
name = 'Owaiz'
print(name[::-1]) #reverse a string
#The syntax for slicing is s[start:stop:step]
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print(name.islower())
print(name.lower().islower())
print(len(name))
print(name.index('i'))
print(name.replace('O', 'o'))
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")#'\' - new initial line is not included, '''...''' or """...""" for multiple lines
print(3 * 'rrr' + 'scretch') #Strings can be concatenated (glued together) with the + operator, and repeated with *
print('Shab' 'nam') #strings in '' when placed next in '' automatically concatenates
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
#s[:i] + s[i:] = s as string, length of word[1:3] is 2

Sentence = input(' Enter your sentence: ') 
word1 = input(' Enter the word you want to replace: ')
word2 = input(' Enter the word you want to replace it with: ')
print(Sentence.replace(word1, word2)) # Replace the word in the sentence

#numbers
print(3+7)
print(78/22.934)
print(20//6)
print(20%6)
#convert number to string
number = 55
numberstr = str(number)
print('the number is' + numberstr)
#get absolute value of the number
print(-5)
print(abs(-5))
print(max(6,8,7))
print(min(7,3,0))
print(min(3.5,3.6,3.2))
print(max(3.5,3.6,3.2))
print(round(4.8))
print(bin(334)) #print binary string for that number
print(7**2)
print(7**3)
from math import * #import math functions
print(round(sqrt(41)))
#name = input('Input your name')
#print(name)
#age = input('Input you age: ')
#print('your name is ' + name + ' and your are ' + age + ' years old' )
