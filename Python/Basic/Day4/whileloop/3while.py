# write a program to print positive numbers
i=1
while i<5:
    no = int(input("Enter numbers"))
    if no<=0 and no<=-1:
        print("try again")
        break
    i+=1
else:
 print("loop performed all its iterations")

print("end!")     