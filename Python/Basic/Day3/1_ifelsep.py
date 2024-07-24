
s1="goodmorning"
ch = input("Enter a character:") #userinput

flag=False
for i in s1:
    if i==ch:
        flag=True
        break

if flag==True:
    print("character present")
else:
    print("character not present")
