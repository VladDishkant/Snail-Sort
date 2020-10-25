# Given an n x n array, return the array elements arranged from outermost elements
# to the middle element, traveling clockwise.
# For example:
# array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# array = [[1,2,3],
#         [8,9,4],
#         [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

def right_down(arr, result):
    for i in range(len(arr)):
        result.append(arr[0][0])
        del arr[0][0]
    for i in range(1, len(arr)):
        result.append(arr[i][len(arr) - 1])
        del arr[i][len(arr) - 1]
    return arr, result


def left_up(arr, result):
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[len(arr) - 1][i])
        del arr[len(arr) - 1][i]
    for i in range(len(arr) - 2, -1, -1):
        result.append(arr[i][0])
        del arr[i][0]
    return arr, result


def snail(snail_map):
    if [len(snail_map) for i in range(len(snail_map))] == [len(snail_map[i]) for i in range(len(snail_map))]:
        result = []
        arr = snail_map.copy()
        for i in range(len(snail_map)):
            if len(arr) == 1 and len(arr[0]) == 1:
                result.append(arr[0][0])
            elif i % 2 == 0:
                arr, result = right_down(arr, result)
            elif i % 2 == 1:
                arr, result = left_up(arr, result)
            else:
                print("Error")
            arr = [value for value in arr if value]
        return result
    else:
        return []


array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]

result = snail(array)
print(result)