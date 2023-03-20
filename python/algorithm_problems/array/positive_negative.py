# Given two integer arrays of same size, “arr[]” and “index[]”, 
# reorder elements in “arr[]” according to given index array. 
# It is not allowed to given array arr’s length.

def positive_negative(list_val, list_index):
    if len(list_val) != len(list_index):
        print("Incorrect number of elements")
        return False, False
    
    return list_val_ordered, list_index_ordered

if __name__ == '__main__':
    input_1 = [10, 11, 12]
    input_2 = [1, 0, 2]

    output_1, output_2 = positive_negative(input_1, input_2)
    print(output_1)
    print(output_2)