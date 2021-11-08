#If statement
print("\nIf statement")
x = 0
y = 5
if x < y:                            # Truthy
    print('yes')
if y < x:                            # Falsy
    print('yes')
if x:                                # Falsy
    print('yes')
if y:                                # Truthy
    print('yes')
if 'aul' in 'grault':                # Truthy
    print('yes')
if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')

#Goruping Statement
print("\nGoruping Statement")
weather = 'cloudy'
if weather == 'nice':
    print('Mow the lawn')
    print('Weed the garden')
    print('Take the dog for a walk')
#Another Statement
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

#Else and elif clauses
print("\nGoruping Statement")
weather = 'cloudy'
if weather == 'nice':
    print('Mow the lawn')
    print('Weed the garden')
    print('Take the dog for a walk')
else:
    print('Read a book')
    print('Watch movies')

x = 20
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

hargaBuku = 20000
hargaMajalah = 5000
uang = 7000
if uang > hargaBuku:
    print('Beli buku')
elif uang > hargaMajalah:
    print('Beli majalah')
else:
    print('Tidak beli buku')

# One line if
print("\nOne line if")
x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

#Ternary Operator
nomor_undian = 80
if nomor_undian < 100:
    prize = 'box1'
else:
    prize = 'box2'
prize = 'box1' if nomor_undian < 100 else 'box2'
print(prize)