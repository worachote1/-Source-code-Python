# การใช้ if ซ้อน if 
age=int(input("ป้อนอายุของคุณ : "))

if age <= 15 :
    if age==15:
        print("เด็กม.3")
    elif age ==14 :
        print("เด็กม.2")
    elif age ==13 :
        print("เด็กม.1")
    else :
        print("เด็กประถม")    
else :
    print("เด็กม.ปลาย")