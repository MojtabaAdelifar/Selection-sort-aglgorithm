

def selectionSort(array):

    for step in range(0, len(array)):
        min_index = step

        for i in range(step + 1, len(array)):
            if array[i] < array[min_index]:
                min_index = i

        key = array[step]
        array[step] = array[min_index]
        array[min_index] = key

    return array

array = [-10, 0, -2, 4, 10]

sortedArray = selectionSort(array)
print(sortedArray)
