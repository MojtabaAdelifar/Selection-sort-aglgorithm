

def selectionSort(array):
    # loops through entier array in order to find the minimum value
    for step in range(0, len(array)):
        min_index = step
        
        # loops for comparing the elements with the minimum element
        for i in range(step + 1, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        
        # swap the elements 
        key = array[step]
        array[step] = array[min_index]
        array[min_index] = key

    return array

# implementaion of the function
array = [-10, 0, -2, 4, 10]

sortedArray = selectionSort(array)
print(sortedArray)
