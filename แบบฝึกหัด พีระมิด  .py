# test พีระมิด *
# ข้อมูล การเว้นบบรทัดใน print() จากเว็บไซต์
# https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
# `\n` will put each word in a new line
print("hello world", "Time", "Worachote", sep="\n")


#
# Patterns can be printed in python using simple for loops.
# First outer loop is used to handle number of rows
# and Inner nested loop is used to handle the number of columns.
# Manipulating the print statements, different number patterns, alphabet patterns
# or star patterns can be printed.
# Some of the Patterns are shown in this article.


# แบบ พีระมิดอย่างง่าย
# ใช้ outter loop เพื่อกําหนด row และ ใช้ nested inner loop เพื่อกําหนด colum


def testpypart(num):
	# outer loop to handle number of rows
	# n in this case
    for i in range(0, num):
        for j in range(0, i+1):
            print("*", end=" ") #end=' ' is used to place a space after the displayed string instead of a new line (ทําให้ข้อความต่อไปมาต่อกันในบรรทัดเดียว แทนที่จะขึ้นบรรทัดใหม่แบบปกติ)
        print("") 	# ending line after each row


num = int(input("Enter number of rows = "))
testpypart(num)

'''
ได้ ถ้าป้อนว่า num = 5 จะได้output คือ
*
**
***
****
*****

'''

print("--------------------------------------------")

# แบบ พีระมิดตัวเลข


def testpypart_number(n):
    #num_pattern = 1
    for i in range(0, n):
            num_pattern=1
            for j in range(0,i+1):
              print(num_pattern,end=" ")
              num_pattern+=1
            print("") 	# ending line after each row
  
n = int(input("Enter number of rows  = "))  
testpypart_number(n)


print("-----------------------------------------")

#พีระมิดแบบ 3 เหลี่ยม

def triangle(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k-1  
        for j in range(0,i+1):
            print("*",end=" ")
        print("")    
     
  
n = int(input("Enter number of row = "))
triangle(n)
           