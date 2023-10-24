def linear_search_1(array: list[str], element: str):
    found_index = -1
    i = 0
    while found_index == -1 and i < len(array):
        if array[i] == element:
            found_index = i
        i += 1
    return found_index

def linear_search_2(array: list[str], element: str):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1