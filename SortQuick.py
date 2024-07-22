def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    else:
        less = []
        equal = []
        more = []
        reference = arr[len(arr) // 2]
        for element in arr:
            if element < reference:
                less.append(element)
            if element == reference:
                equal.append(element)
            if element > reference:
                more.append(element)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + equal + more


def main():
    test_list = [4, 5, 7, 3, -2, -5, 6, -11, 45, 100, -324]
    print(quick_sort(test_list))

if __name__ == "__main__":
    main()
