def solution(A):
    # write your code in Python 3.6
    
    #BASE CASE: max O(3) = O(1)
    if(len(A) < 3):
        result = 1
        for i in range(len(A)):
            result = result * A[i]
        
        return result
    
    # O(nlogN)
    A.sort()
    #print(A)
    max_trip = A[0] ** 3
    
    #we have 2 negatives
    if(A[1] < 0):
        trip = A[0] * A[1]  * A[-1]
        if(trip > max_trip): 
            max_trip = trip
            
    # we have 3 values greater than 0
    # or we have all 0 or negative values
    # or we have all positive values
    if(A[-3] > 0 or A[-1] <= 0 or A[0] > 0):
        trip = A[-3] * A[-2] * A[-1]
        print("trip", trip)
        if(trip > max_trip): 
            max_trip = trip

    return max_trip