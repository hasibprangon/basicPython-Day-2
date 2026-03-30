inp = input()
num = inp.split()
x = int(num[0])
y = int(num[1])
z = int(num[2])

min = x
max = x

# min value
if y < min:
    min = y

if z < min :
    min = z

# max value
if y > max:
   max = y
if z > max:
    max = z

print(min, max)
