##Function Creation 
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)

def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)


##Call a Function
print("\n\n> Call a Function")
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

printme("I'm first call to user defined function!")
printme("Again second call to the same function")


##Pass by reference vs value
print("\n\n> Pass before using function with reference & after")
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("Values inside the function : ", mylist)
   return mylist

mylist = [10,20,30]
print("Values outside the function - before : ", mylist)
mylist = changeme( mylist )
print("Values outside the function - after  : ", mylist)

#Overwritten by function
print("\n> Overwriten by function")
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = [1, 2, 3, 4] # This would assign new reference in mylist
   print("Values inside the function  : ", mylist)

mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)


##Required Argments
print("\n\n> Required Arguments, keyword argument, default arguments, variable-length arguments")
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

printme("Hello")

print("\n> Another example function to calculate rect that required parameter calculate_rect(length, width)")
def calculate_rect(length, width = 50):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)

calculate_rect(100, 20)

#Keyword Arguments
print("\n> Example with keyword arguments with same function reversed order parameter calculate_rect(width = 20, length = 200)")
calculate_rect(width = 20, length = 200)

#Default Arguments
print("\n> Example function with default arguments width = 50 calculate_rect(width = 50, length)")
calculate_rect(length = 100)

#Variable-length Arguments
def buy(customer_name, *items):
    for i, item in enumerate(items):
        print('customer: {customer} item number {index}: {itemname}'.format(customer = customer_name, index = i, itemname = item))

buy('roy', 'chocolate bar')
buy('tia', 'eggs', 'wheat', 'flour', 'chololate bar')


##Anonymous Functions
print("\n\n> Anonymous function")
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))


##Return Statement
print("\n\n> Return Statement")
# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total

# Now you can call sum function
total = sum(10, 20)
print("Result function : ", total)


##Global variable vs Local variable
print("\n\n> Global variable vs Local variable")
# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total

# Call a function
print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)


##Docstring
print("\n\n> Docstring")

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3

print(sum_number.__doc__)