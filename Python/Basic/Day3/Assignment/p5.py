print("Out of 300 marks")
m1=int(input("Enteryourmarks1:"))
m2=int(input("Enteryourmarks2:"))
m3=int(input("Enteryourmarks3:"))

avg = m1+m2+m3/3

if avg>=250:
    print("Firstclass")
elif avg<=150:
    print("Secondclass") 
elif avg<=70:
    print("thirdclass") 