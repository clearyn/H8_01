## Assignment Instructions
# Buatlah sebuah list dengan value berupa:

# numbers = [ 951, 402, 984, ....]
# Loop dan print semua angka genap dari list angka diatas dengan urutan yang sama. Jangan mencetak angka apa pun yang muncul setelah angka 918.
# Tampilkan pesan 'Done' setelah looping berakhir.

## Non-Graded Assignment ini dibuat guna mengevaluasi konsep looping sebagai berikut:

# Mampu membuat looping dengan menggunakan for / while
# Mampu mengimplementasikan if statement didalam looping
# Mampu mengimplementasikan break dan continue statement didalam looping
# Mampu mengimplementasikan else statement didalam looping

## Keterangan Assignment
# Nama: Ryan Cleary
# Kode: FSDO001ONL003

numbers = [
    951, 402, 984, 651, 360,
    69, 408, 319, 601, 485,
    980, 507, 725, 547, 544,
    615, 83, 165, 141, 501,
    263, 617, 865, 575, 219,
    390, 984, 592, 236, 105,
    942, 941, 386, 462, 47, 
    418, 907, 344, 236, 375,
    823, 566, 597, 978, 328,
    615, 953, 345, 399, 162,
    758, 219, 918, 237, 412,
    566, 826, 248, 866, 950, 
    626, 949
]

# Function to check odd / even number
def isEven(number):
    if(int(number / 2) * 2 == number):
        return True
    else:
        return False

## For Type
print("\n> For Type")
# Loop to print lower than 918 & even number 
for i, number in enumerate(numbers):
    if(number <= 918 and isEven(number)):
        print(number)
    # Below code is not necessary but needed for assignment objective number 4 "Implements continue and break"
        continue 
    elif i + 1 == len(numbers):
        print('Done')
        break
    # End: Below code is not necessary but needed for assignment objective number 4 "Implements continue and break"
# print('Done')

## While Type
# Loop to print lower than 918 & even number 
print("\n> While Type")
while numbers:
    if(numbers[0] <= 918 and isEven(numbers[0])):
        print(numbers.pop(0))
    # Below code is not necessary but needed for assignment objective number 4 "Implements continue and break"
        continue
    else:
        del numbers[0]
    # End: Below code is not necessary but needed for assignment objective number 4 "Implements continue and break"
else:
    print('Done')