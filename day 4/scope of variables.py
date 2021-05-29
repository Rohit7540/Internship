def my_func():
    x=50 #local variable
    print("Value inside function:",x)
x=20   #globel variable
my_func()
print("Value outside function:",x)