# ตัวเลขขั้นบันได

'''
input = 4
1
12
123
1234

'''

# row แนวนอน
# colum แนวตั้ง

last = int(input("ป้อนตัวเลข : "))

for row in range(1,last+1) :
    for colum in range (1,row+1) :
        print(colum,end="") # end = " " เอาไว้เพื่อแสดงผลในแนวนอน
    print(" ")    # print(" ") แบบนี้คือไม่ใส่ argument ใดๆลงใน print() ทําให้เว้นบรรทัด