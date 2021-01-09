#แบบฝึกหัดค้นหาตัวเลขมากสุด & น้อยสุด

#ค้นหาตัวเลข มากสุด / น้อยสุด

max,min = 0,999999

while True :
    number=int(input("ป้อนตัวเลขของคุณ : "))
    
    if number<0 : #คําสั่งกระโดดออกจากloop เมื่อป้อนค่าติดลบ 
        break
        print("จบการทํางาน !!!")
    
    if number>max :
        max = number
    
    if number<min :   
        min = number

print("ค่า max = ",max)
print("ค่า min = ",min)    