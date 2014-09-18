## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

fruit = {
"apples":3,
"pears":3,
"grapes":1,
"tomatoes":2
}

fruit_array = []
for key, value in fruit.items():
    fruit_array.extend([key] * value) # ['apple'] * 3

from random import random

### sample with replacement
cnt_fruit = len(fruit_array)
for i in range(100):
    index = int(random() * cnt_fruit)
    print fruit_array[index] # [0, 1) , [0, cnt_fruit)


### sample without replacement
fruit_array = []
for key, value in fruit.items():
    fruit_array.extend([key] * value) # ['apple'] * 3

index_array = range(len(fruit_array))
for i in range(100):
    cnt_fruit = len(index_array)
    try:
        index = index_array.pop(int(random() * cnt_fruit))
        print fruit_array[index]
    except:
        pass


## 4 fruits
total_cnt = sum(fruit.values())
fruit_boundary = {}
previous_bound = 0
for key, value in fruit.items():
    upper_bound = value * 1. / total_cnt + previous_bound
    fruit_boundary[upper_bound] = key
    previous_bound = upper_bound

fruit_boundary = sorted(fruit_boundary.items())

for i in range(100): # binary search
    random_number = random()
    start = 0
    end = len(fruit_boundary) - 1
    while start < end:
        mid = (start + end) / 2
        if random_number < fruit_boundary[mid][0]:
            end = mid - 1
        else:
            if start == end:
                print fruit_boundary[mid][1]
                break
            else:
                start = mid + 1
    
