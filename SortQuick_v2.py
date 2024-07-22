def quick_sort(L):
    if L: return quick_sort([x for x in L[1:] if x<L[0]]) + L[0:1] + quick_sort([x for x in L[1:] if x>=L[0]])
    return []


def main():
    test_list = [4, 5, 7, 3, -2, -5, 6, -11, 45, 100, -324]
    print(quick_sort(test_list))

if __name__ == "__main__":
    main()
