ha = int(input('geef getal op'))

def binarysearch(lst, target):
    min_i = 0
    max_i = len(lst)-1

    while max_i >= min_i:
        index = int((min_i + max_i)/2)

        if lst[index] == target:
            return True
        elif lst[index] < target:
            min_i = index + 1

        elif lst[index] > target:
            max_i = index - 1
    
    return False

lst = [1,3,6,9,12,21,25,27]


print(binarysearch(lst, ha))
    
