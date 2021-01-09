#แบบฝึกหัด เขียนโปรแกรมแม่สูตรคูณ

'''
#ใช้loop ซ้อน loop หาผลคูณสูตรคูณ แม่ 2,3

for i in range(2,4) : #ก็คือคือให้เริ่มที่ แม่2 จบที่ ก่อนแม่ 4(ก็คือแม่ 3 นั่นแหละ)
    print("สูตรคูณแม่ : ",i)
    for j in range(1,13) :
        print(i,"X",j,"=",i*j)
    print("--------------")    

'''



'''
num = float(input("ป้อนตัวเลขที่ต้องการหาผลคูณ : "))

for i in range(1,13) :
    print(num,"X",i," = ",num*i)

print("---------------- while------------------------ ")

i=1
while i<=12 :
    print(num,"X",i,"=",num*i)
    i+=1

'''

print("---------------------------------------------")
#ทําแบบช่อง KongRuksiam Official

start = int(input("ป้อนแม่สูตรคูณเริ่มต้น :"))
end = int(input("ป้อนแม่สูตรคูณสุดท้าย :"))


for i in range(start,end+1) :
    for j in range(1,13):
        print(i,"X",j,"=",i*j)