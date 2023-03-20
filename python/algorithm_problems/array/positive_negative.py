# You have been given an array and you have to make a program to convert that 
# array such that positive elements occur at even numbered places in the array 
# and negative elements occur at odd numbered places in the array. 
# We have to do it in place.
# There can be unequal number of positive and negative values and the extra 
# values have to left as it is.

def positive_negative(list_unordered):
    num_pos = []
    num_neg = []

    for num in list_unordered:
        if num >= 0:
            num_pos.append(num)
        else:
            num_neg.append(num)
    
    num_pos.reverse()
    num_neg.reverse()

    list_ordered = []

    if len(num_pos) == len(num_neg):
        for i in range(len(list_unordered)):
            if i % 2 == 0:
                list_ordered.append(num_pos.pop())
            else:
                list_ordered.append(num_neg.pop())
    elif len(num_pos) > len(num_neg):
        for i in range(2*len(num_neg)):
            if i % 2 == 0:
                list_ordered.append(num_pos.pop())
            else:
                list_ordered.append(num_neg.pop())
        for i in range(len(num_pos)):
            list_ordered.append(num_pos.pop())
    elif len(num_pos) < len(num_neg):
        for i in range(2*len(num_pos)):
            if i % 2 == 0:
                list_ordered.append(num_pos.pop())
            else:
                list_ordered.append(num_neg.pop())
        for i in range(len(num_neg)):
            list_ordered.append(num_neg.pop())
 
    return list_ordered

if __name__ == "__main__":
    input = [-1, 3, -5, 6, 3, 6, -7, -4, -9, 10]
    output = positive_negative(input)
    answer = [3, -1, 6, -5, 3, -7, 6, -4, 10, -9]
    if output == answer:
        test = True
    else:
        test = False
    
    print(output)   
    print(test)