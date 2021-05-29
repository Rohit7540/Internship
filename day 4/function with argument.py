def sum(a=6,b=8):
    print(a+b)
sum(10,20)   #calling with argument
sum()        #calling without argument

#keyword argument
def sum(a,b):
    print("sum is :",a+b)
sum(b=10,a=20) #calling with argument

#non keyword argument
def add(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("sum:",sum)
add(10,20)
add(10,20,30)

#keyword argument
def my_function(**arg):
    for i,j in arg.items():
        print(i,j)
my_function(Name="Rohit",lastname="Makwana")
