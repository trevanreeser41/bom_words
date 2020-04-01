# Parameters in the following functions:
#   data: a list of tuples
#   index: the tuple index to sort by
#
# Consider the following example data:
data = [
    ( 'homer', 'simpson', 50 ),
    ( 'luke', 'skywalker', 87 ),
    ( 'bilbo', 'baggins', 111 ),
    ( 'mike', 'azowskie', 21 )
]
#
#   bubble_sort(data, 0) sorts on first name (a..z)
#   bubble_sort(data, 0, True) sorts on first name (z..a)
#   bubble_sort(data, 2) sorts on age (1..infinity)
#
# The data list is sorted in place (anew list is not created).
# You do NOT need to perform validation on input data
# (null data list, index out of bounds, etc.)
#


def bubble_sort(data, index, descending=False):
    '''Sorts using the bubble sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(len(data)-1,0,-1):
        for i in range(item):
            if descending == False:
                if data[i][index]>data[i+1][index]:
                    temp = data[i]
                    data[i] = data[i+1]
                    data[i+1] = temp
            elif descending == True:
                if data[i][index]<data[i+1][index]:
                    temp = data[i]
                    data[i] = data[i+1]
                    data[i+1] = temp
    # data.sort(key=lambda t: t[index], reverse=descending)


def insertion_sort(data, index, descending=False):
    '''Sorts using the insertion sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(1,len(data)):
        currentValue=data[item]
        position = item
        if descending == False:
            while position>0 and data[position-1][index]>currentValue[index]:
                data[position]=data[position-1]
                position = position-1
        elif descending == True:
            while position>0 and data[position-1][index]<currentValue[index]:
                data[position]=data[position-1]
                position = position-1
        data[position]=currentValue
    # data.sort(key=lambda t: t[index], reverse=descending)

def selection_sort(data, index, descending=False):
    '''Sorts using the selection sort algorithm'''
    # replace this with your own algorithm (do not use Python's sort)
    for item in range(len(data)-1,0,-1):
        maxPosition = 0
        for i in range(1,item+1):
            if descending == False:
                if data[i][index] > data[maxPosition][index]:
                    maxPosition = i
            elif descending == True:
                if data[i][index] < data[maxPosition][index]:
                    maxPosition = i
        temp = data[item]
        data[item] = data[maxPosition]
        data[maxPosition] = temp
    # data.sort(key=lambda t: t[index], reverse=descending)

# bubble_sort(data, 0, True)
# selection_sort(data, 2, True)
# insertion_sort(data, 1, True)