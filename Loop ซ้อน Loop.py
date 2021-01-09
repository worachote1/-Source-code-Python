#Loop ซ้อน Loop

#จะทํางานจาก loop นอก แล้วมาที่ loopใน ตามจํานวนรอบที่ได้ระบุไว้ แล้วกลับไปทําที่ loop นอก ต่อ แล้วเข้ามาทํา loopใน อีก

#while ซ้อน while

print("while ซ้อน while ")

i = 1
while i<=3 :
    j=1
    while j<=5 :
        print("รอบที่ ",i,"ตําแหน่งที่ ",j)
        j+=1     
    i+=1
print("จบโปรแกรม")
print("--------------------------------------------")

print("for ซ้อน for ")

for i in range(1,4) :
    for j in range(1,6) :
        print("รอบที่ ",i,"ตําแหน่งที่ ",j)

print("จบโปรแกรม")        