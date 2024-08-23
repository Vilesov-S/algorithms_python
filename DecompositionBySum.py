def decomposition(n : int) -> list:
    row = [n]
    yield row
    while len(row) != n:
        for i in range(len(row) - 1, -1, -1):
            if row[i] != 1:
                row[i] -= 1
                if (s := sum(row[i + 1:]) + 1) >= 3:
                    row = row[:i + 1] + [s]
                    break
                else:
                    if i == len(row) - 1:
                        row.append(1)
                    else:
                        row[i + 1] += 1
                    break
        yield row


def main():
    n = 3
    print(f"{n = }:")
    for i, row in enumerate(decomposition(n), 1):
        print(f"{i}: {row}")
    print('\n')
    
    n = 5
    print(f"{n = }:")
    for i, row in enumerate(decomposition(n), 1):
        print(f"{i}: {row}")
    print('\n')

if __name__ == "__main__":
    main()
