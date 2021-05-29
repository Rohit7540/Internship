def my_function():
    print("Hello Rohit")
my_function()

#example with argument
def my_function(name):
    print("name is :",name)
my_function("Rohit")

#example with return statement
def my_function(name):
    return name
name = my_function("Rohit")
print(name)

#example with multiple statement
def my_function():
    name="Rohit"
    contact=7016054978
    return name,contact
name,contact=my_function()
print("Name:",name)
print("Contact :",contact)