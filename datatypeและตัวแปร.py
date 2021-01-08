# --------Datatype และ Variable--------------

# Data Structures จะแบ่ง datatype เป็น 2 ชนิด คือ
# Primitive datatype ชนิดข้อมูลพื้นฐานที่จะได้เรียนกันในตอนแรก เช่น Integer Float String Boolean
# Non-Primitive datatype เช่น Array Set Tuple Dictionary List File 

#ชื่อตัวแปร = ค่าที่เก็บในตัวแปร

x = 20 #integer
print("ผลลัพธ์ = "+str(x)) # แปลงเป็น String โดยใช้ str


#----การแปลง ชนิดข้อมูล
x = 10 #ชนิด Integer
y = 3.93 #ชนิด Float
z = "26" #ชนิด String

# result =  x + z
# print(result)  ตัว x และ z ไม่สามารถทํางานร่วมกันได้ เพราะตัวแปรคนละชนิดกัน 
#ถ้าจะให้รวมกันได้ต้องแปลง z จาก String ให้เป็น เสียก่อน Integer
int(z)

result = x+int(z)
print(result)