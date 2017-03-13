for nums in range(1,2001):
    if nums % 2 == 0:
        str(nums)
        v = "This is an even number"
        # print "Number is",nums, v
    else:
        str(nums)
        t = "This is an odd number"
        # print "Number is" ,nums, t

def multiply(f,num):
    new_arr = []
    for element in f:
        i = element * num
        new_arr.append(i)
    return new_arr

c = [2,2,3,4,5,6]
d = 8
# print multiply(c, d)

def layered_multiples(arr):
    count = 0
    for element in arr:
        final_arr = []
        while element > count:
            final_arr.append(1)
            count += 1
        print final_arr

x = layered_multiples(multiply([2,4,5],3))
print x
