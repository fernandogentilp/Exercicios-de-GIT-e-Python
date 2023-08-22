def sort(array):
        for final in range(len(array), 0, -1):
            exchanging = False
            print("Loop")
            for current in range(0, final - 1):
                if array[current] > array[current + 1]:
                    array[current], array[current + 1] = array[current + 1], array[current]
                    exchanging = True
            if not exchanging:
                 break
        

array = sorted([9, 8, 7, 6, 5, 2, 3 , 1])
sort(array)
print(array)

