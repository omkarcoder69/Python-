age = int(input("Enter your age:"))
gen = input("Enter your gender(m / f)")

if age>=18 and gen=="m":
    print("major")
elif age<=18 and gen=="":
    print("minor")

if age>=18 and gen=="f":
    print("major")
elif age<=18 and gen=="":
    print("minor")


  