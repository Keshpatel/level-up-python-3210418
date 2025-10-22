def find_Index_Of(nested_list, target_value):
    results = []
    # Inner recursive function
    def search(sublist, current_path):
        for index, item in enumerate(sublist):
            # Build the path as we go deeper
            new_path = current_path + [index]
            # If item matches the target, add the path
            if item == target_value:
                results.append(new_path)
            # If item is a list, search inside recursively
            elif isinstance(item, list):
                search(item, new_path)
    # Start the search from the top level
    search(nested_list, [])
    return results
       


def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                index_list.append([index] + i)
    return index_list


# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]

    nestedList_data = [1, [2,3,4], [1, 2, 3], 2, [11, 22, 30], 3 , [5, 4, 30], 4 ]
    print(find_Index_Of(nestedList_data, 1))
    print(find_Index_Of(nestedList_data, 4))
    
