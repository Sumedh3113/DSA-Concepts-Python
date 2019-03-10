import math
def binary_search(input_array, value):
    high = len(input_array)-1
    low = 0
    while(low <= high):
        m = math.floor((high+low)/2)
        if(input_array[m] == value):
            return value
        elif(input_array[m] > value):
            high = m -1
        else:
            low = m + 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))