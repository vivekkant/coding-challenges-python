

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    elements = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    score = 0
    for elem in elements:
        if elem in set_a:
            score =+ 1
        elif elem in set_b:
            score -= 1
    print(score)
