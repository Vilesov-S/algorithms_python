def buble_sort(row):
    n = len(row)
    for i in range(n):
        for j in range(i, n):
            if row[i] > row[j]:
                row[i], row[j] = row[j], row[i]

def main():
    row = [4, 5, 7, 3, 4, 2, 1, -1, 0, -6]
    buble_sort(row)
    print(row)
    pass

if __name__ == "__main__":
    main()
