x=0
y=1
till_no=int(input("Enter the number till which you want fibonacci series: "))
if till_no ==0:
    print(0)
else:
    print(x,end=" ")
    sum1=y
    while sum1<=till_no:
        print(sum1,end=" ")
        sum1=x+y
        x=y
        y=sum1
