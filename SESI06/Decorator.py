# Python Decorator
print("\n> Python Decorator")

#First Class Object
print("\n> First Class Object")
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))

#Inner Functions
print("\n> Inner Functions")
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    first_child()
    second_child()

print(parent())

#Returning Function From Functions
print("\n\n> Returning Funtion From Function")
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
print(first())


##Simle Decorator
print("\n\n> Simle Decorator")
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

##Before
# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)

##After
print("\n\n> Simle Decorator")
@my_decorator
def say_whee():
    print("Whee!")

say_whee()

##More Exampe
# print("\n\n> More Exampe")
# import functools
# import time

# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()    # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()      # 2
#         run_time = end_time - start_time    # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#     return wrapper_timer

# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])

# waste_some_time(1)

def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)

@greet
def shout(text):
    return text.upper()

@greet
def whisper(text):
    return text.lower()
 

shout
greet