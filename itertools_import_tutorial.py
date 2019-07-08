from itertools import count, accumulate, takewhile

# counts from 3 till 20
for i in count(3):
    print(i)
    if i >= 20:
        break

# adds up all the prev numbers in the list each time
a = list(accumulate(range(8)))
print(a)

# takes stuff from a list while TRUE
# eg. goes until < 6
print(list(takewhile(lambda x: x <= 6, a)))