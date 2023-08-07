def hashtak_dobodi():
    n=int(input("Enter a number for satr:"))
    m=int(input("Enter a number for soton:"))
    for i in range(n):
        for j in range(m):
            if i%2==0:
                print("#",end="*")
            else:
                print("",end="*#")
        print()
hashtak_dobodi()