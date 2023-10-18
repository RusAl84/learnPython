def sum_arr(arr: list[int])->int:
    result = 0
    for el in arr:
        if el % 2 == 0:
            result += el
    return result 

if __name__ == '__main__':
    print(sum_arr([2,6,8,9]))