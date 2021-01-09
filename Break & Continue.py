#Break & Continue


#การใช้Break
i = 1 
while i<=10 :
    print("รอบที่ ",i)
    if i==5 :
        print("ได้ใช้ break จบที่ i = 5 แล้ว")
        break
    i+=1    
print("จบโปรแกรม")    

#การใช้Continue
#เป็นคําสั่งที่ใช้ในการกระโดดข้าม

i = 1 
while i<=10 :
    print("รอบที่ ",i)
    i+=1
    if (i-1)==5 :
        print("ได้ใช้ continue ข้ามที่ i = 5 แล้ว")
        continue

        
print("จบโปรแกรม")    
