# You have been given an array and you have to make a program to convert that 
# array such that positive elements occur at even numbered places in the array 
# and negative elements occur at odd numbered places in the array. 
# We have to do it in place.
# There can be unequal number of positive and negative values and the extra 
# values have to left as it is.

def positive_negative(list):
    num_pos = []
    num_neg = []

    for num in list:
        if num >= 0:
            num_pos.append(num)
        else:
            num_neg.append(num)
    
    num_pos.reverse()
    num_neg.reverse()

    new_list = []
    for i in range(len(list)):
        if i % 2 == 0:
            new_list.append(num_pos.pop())
        else:
            new_list.append(num_neg.pop())
    
    return new_list

if __name__ == "__main__":
    input = [1, -3, -6, 5]
    output = positive_negative(input)
    answer = [1, -3, 5, -6]
    if output == answer:
        test = True
    else:
        test = False
    
    print(output)   
    print(test)