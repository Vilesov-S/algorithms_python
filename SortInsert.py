def insert_sort(row):
    n = len(row)
    for i in range(n):
        tmp = row[i]
        k = i
        while (k > 0 and tmp < row[k - 1]):
            row[k] = row[k - 1]
            k -= 1
        row[k] = tmp
    

def main():
    row = [4, 5, 7, 3, 4, 2, 1, -1, 0, -6]
    insert_sort(row)
    print(row)
    pass

if __name__ == "__main__":
    main()
