
#your user : worachote
#your password : 232903

user = input("ป้อน User :")
Password = input("ป้อน Password :")

while (user =="worachote" and Password =="232903" ) :

    age = int(input("ป้อนอายุของคุณ : "))

    if age>=30 :
        print("วัยทํางาน")
    elif age>=20 :
        print("วัยผู้ใหญ่")
    elif age>=15 :
        print("วัยเด็ก")
    else :
        print("วัยเด็ก")       
print("คุณป้อน User หรือ Password ผิด")             
    