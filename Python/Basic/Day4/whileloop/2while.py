# accept 4 no and takes a sum
i=1
sum=0
while i<=4:
    no=int(input("Enter number:"))
    if no<=0 :
        print("try again")
        break
    sum=sum+no
    i+=1
    print(sum)
    