# Given two integer arrays of same size, “arr[]” and “index[]”, 
# reorder elements in “arr[]” according to given index array. 
# It is not allowed to given array arr’s length.

def positive_negative(list_val, list_index):
    if len(list_val) != len(list_index):
        print("Incorrect number of elements")
        return False, False
    
    list_val_ordered = []
    list_index_ordered = []

    for idx in list_index:
        list_val_ordered.append(list_val[idx])
        list_index_ordered.append(list_index.index(idx))

    return list_val_ordered, list_index_ordered

if __name__ == '__main__':
    input_1 = [50, 40, 70, 60, 90]
    input_2 = [3,  0,  4,  1,  2]

    output_1, output_2 = positive_negative(input_1, input_2)
    print(output_1)
    print(output_2)