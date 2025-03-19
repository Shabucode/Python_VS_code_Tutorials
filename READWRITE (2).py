Family = open("E:/text.txt", 'r' ) # r - read only, w - write only, r+ = read and write, a - append to the end of this file
print(Family.readable()) #in the above line path should always have / in python, not \
#print(Family.readline()) #prints first line
#print(Family.readline()) # prints second line
#print(Family.readlines()) #print all lines
for lines in Family.readlines():
    print(lines)
Family.close

newfile = open("E:/newfileforwriting.txt", 'w')
newfile.write("This file is created using python")
newfile.close
newfile = open("E:/newfileforwriting.txt ", 'a')
newfile.write(" \n This is a new line using append function")
newfile.close
#A new python file created using python
newfile = open("E:/filecreatedusingpython.py", 'w')
newfile.write('print(\" This is comment line \")')
newfile.close              