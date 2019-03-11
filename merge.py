def mergeSort(a):
    if(len(a) > 1):
        mid = len(a) // 2
        
        #print(mid)
        L = a[:mid]
        R = a[mid:]
        mergeSort(L)
        mergeSort(R)
        #First mergeSort(L) will get called till the end of base condition then
		#mergeSort(R) will get called till end of base condition then the code below will be executed
		
        i = j = k = 0
        
        while i< len(L) and j< len(R):
            if(L[i] < R[j]):
                a[k] = L[i]
                i = i + 1
            elif(L[i] > R[j]):
                a[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            a[k] = L[i]
            i = i + 1
            k = k +1
        while j < len(R):
            a[k] = R[j]
            j = j + 1
            k = k +1
    return a
            
        
x = [1,5,3]

print(mergeSort(x))
            
            
        