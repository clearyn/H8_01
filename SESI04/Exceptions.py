import sys

##Raise an Exception
# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

##The AssertionError Exception: Handling Exception
print("\n\n> The AssertionError Exception: Handling Exception")
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('The os_interaction() function was not executed')

##With Else Clause
print("\n\n> With Else Clause")
try:
    with open('test.txt') as file:
        read_data = file.read()
    with open('file.log') as file:
        read_data = file.read()
    print('semua read berhasil')
except FileNotFoundError as error:    
    print(error)
else:    
    print('Executing the else clause.')


## Cleaning Up After Using finally
print("\n\n> Cleaning Up After Using finally")
try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')