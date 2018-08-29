#Question.1- Write a Python program to read n lines of a file
#Answer
f=open('file1.txt','r')
new=f.read()
print(new)
f.close()
print()


#Question.2- Write a Python program to count the frequency of words in a file.
#Answer
f=open("file1.txt",'r')
data=f.read()
word=data.split()
dict={}
for x in word:
    dict[x]=word.count(x)
print(dict)
print()


#Question.3- Write a Python program to copy the contents of a file to another file
#Answer
with open('file1.txt', 'r') as f1:
    with open('file2.txt', 'w') as f2:
        f2.write(f1.read())


#Question.4- Write a Python program to combine each line from first file with the corresponding line in second file.
#Answer
str1=[]
str2=[]
s=str()
with open('file1.txt','r') as f1:
    with open('file2.txt','r') as f2:
       str1+=f1.readlines()
       str2+=f2.readlines()
       for x,y in zip(str1,str2):
           print(x)
           print(y)
           s+=x+y
with open('file3.txt','w') as f3:
      f3.write(s)



'''
Question.5- Write a Python program to write 10 random numbers into a file.
Read the file and then sort the numbers and then store it to another file.
'''
#Answer
with open('file4.txt','w') as f:
   for i in range(10):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('file4.txt','r') as f:
   data=f.readlines()
   for no in data:
       a=no.split()
   a.sort()

with open('file5.txt','w') as f:
   for i in a:         
      f.write("%s "%(i))
