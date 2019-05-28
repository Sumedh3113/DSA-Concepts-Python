"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists 
		#after 1st iteration [] + 1 is returned and greater([4,6,9,2]) is called 
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
		
test = [1,4,6,9,2]
#test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(sort(test))
