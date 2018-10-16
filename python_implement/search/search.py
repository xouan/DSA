

def sequential_search(alist, item):
    n = len(alist)
    pos = 0
    found = False
    while pos < n and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    if found:
        return pos
    else:
        return -1

def binary_search(alist, item):
    l = 0
    r = len(alist) - 1
    found = False
    while l <= r and not found:
        mid = (l + r) // 2
        if alist[mid] == item:
            found = True
        elif alist[mid] > item:
            r = mid - 1
        else:
            l = mid + 1
    if found:
        return mid
    else:
        return -1
if __name__ == "__main__":
    print("start")
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 65, 8, 65]
    print(sequential_search(test_list, 8))
    print(binary_search(test_list, 8))
    print("end")