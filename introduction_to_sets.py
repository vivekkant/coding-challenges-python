def average(array):
    s = set(array)
    total = sum(s)
    avg = total/len(s)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)