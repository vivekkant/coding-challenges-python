if __name__ == '__main__':
    n = int(input())
    stamps = set()
    for i in range(n):
        s = input()
        stamps.add(s)

    print(len(stamps))