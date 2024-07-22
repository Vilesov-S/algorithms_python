def choice_sort(row):
    n = len(row)
    for i in range(n):
        k = i
        for j in range(i, n):
            if (row[k] > row[j]):
                k = j
        row[k], row[i] = row[i], row[k]

def main():
    row = [4, 5, 7, 3, 4, 2, 1, -1, 0, -6]
    choice_sort(row)
    print(row)

if __name__ == "__main__":
    main()
