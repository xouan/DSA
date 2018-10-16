


def bubble_sort(alist):
    n = len(alist)
    for i in range(n-1):
        for j in range(n-1-i):
            if alist[j+1] < alist[j]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

def select_sort(alist):
    n = len(alist)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if alist[min] > alist[j]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]

def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        temp = alist[i]
        j = i-1
        while j >= 0 and temp < alist[j]:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = temp

def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = alist[i]
            j = i
            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        gap = gap // 2

'''
def shell_sort(alist):
    sub_list_count = len(alist) // 2
    while sub_list_count > 0:
        for start_pos in range(sub_list_count):
            gap_insert_sort(alist, start_pos, sub_list_count)
        sub_list_count = sub_list_count // 2
def gap_insert_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current_value = alist[i]
        pos = i
        while pos >= gap and alist[pos-gap] > current_value:
            alist[pos] = alist[pos-gap]
            pos = pos - gap
        alist[pos] = current_value
'''
def merge_sort(alist):
    n = len(alist)
    if n > 1:
        mid = n // 2
        left_half = alist[:mid]
        right_half = alist[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(left_half, right_half, alist)
def merge(left_half, right_half, alist):
    p = len(left_half)
    q = len(right_half)
    i = 0
    j = 0
    k = 0
    while i < p and j < q:
        if left_half[i] < right_half[j]:
            alist[k] = left_half[i]
            i += 1
        else:
            alist[k] = right_half[j]
            j += 1
        k += 1
    while i < p:
        alist[k] = left_half[i]
        i += 1
        k += 1
    while j < q:
        alist[k] = right_half[j]
        j += 1
        k += 1

def quick_sort(alist):
    quick_sort_help(alist, 0, len(alist)-1)
def quick_sort_help(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_help(alist, first, split_point-1)
        quick_sort_help(alist, split_point+1, last)
def partition(alist, first, last):
    pivot_value = alist[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while left <= right and alist[left] <= pivot_value:
            left += 1
        while right >= left and alist[right] >= pivot_value:
            right -= 1
        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]
    alist[first], alist[right] = alist[right], alist[first]
    return right

def heap_sort(arr):
    heap_arr = [0] + arr
    build_heap(heap_arr)
    del_heap(heap_arr)
def build_heap(heap_arr):
    n = len(heap_arr) - 1
    i = n // 2
    while i >= 1:
        k = i
        v = heap_arr[k]
        heap = False
        while not heap and 2 * k <= n:
            j = 2 * k
            if j < n:
                if heap_arr[j] < heap_arr[j+1]:
                    j += 1
            if v >= heap_arr[j]:
                heap = True
            else:
                heap_arr[k] = heap_arr[j]
                k = j
                heap_arr[k] = v
        i -= 1
    print(heap_arr)      
def del_heap(heap_arr):
    i = len(heap_arr) - 1
    while i >= 1:
        retval = heap_arr[1]
        print(retval)
        heap_arr[1] = heap_arr[i]
        heap_arr[i] = retval
        i -= 1
        k = 1
        heap = False
        while not heap and 2 * k <= i:
            j = 2 * k
            v = heap_arr[k]
            if j < i:
                if heap_arr[j] < heap_arr[j + 1]:
                    j = j + 1
            if v >= heap_arr[j]:
                heap = True
            else:
                heap_arr[k] = heap_arr[j]
                k = j
                heap_arr[k] = v
if __name__ == "__main__":
    test_list = [89, 45, 68, 90, 29, 34, 17]
    bubble_sort(test_list)
    #select_sort(test_list)
    #insert_sort(test_list)
    #shell_sort(test_list)
    #merge_sort(test_list)
    #quick_sort(test_list)
    #heap_sort(test_list)
    print(test_list)