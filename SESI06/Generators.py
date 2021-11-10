##Using Generators
print("\n> Using Generators")

def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'

print(my_generator())
for char in my_generator():
  print(char)

#Using Generators Function
print("\n> Using Generators Funtion")
def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
  print(i)

#Using Generators Object
print("\n> Using Generators Object")
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

x = simpleGeneratorFun()
print(next(x))
print(next(x))
print(next(x))