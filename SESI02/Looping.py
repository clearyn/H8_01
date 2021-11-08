print("\nLooping")
n = 5

## While Loop
print("While Loop")
while n > 0:
    n -= 1
    print(n)


## Python break and continue Statements
print("Python break and continue Statements")
#Break
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

# Continue
while n > 0:    
    n -= 1    
    if n == 2:       
         continue    
    print(n)
print('Loop ended.')


## The else Clause in loop
print("\nThe else Clause in loop")
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

## Nested while loop
print("\nNested loop break")
i = 0
while i <= 10:
    if i == 3: break
    j = 0
    while j <= 5:
        print(i, j)
        j += 1
        if(j == 3): continue
        print('---')
    i += 1

a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))

##One line while loop
print("\nOne line while loop")
n = 5
while n > 0: n -= 1; print(n)


## For Loop
print("\nFor loop")
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)
    
#Range
print("\nRange")
x = range(0, 100, 20)
for n in x:
    print(n)

#Using dictionary and build in function items() and values() for dictionary
print("\nUsing dictionary and build in function items() and values() for dictionary")
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d.values():
    print(k)
for k, v in d.items():
    print(k, ':', v)