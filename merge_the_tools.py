def merge_the_tools(string, k):
    n = len(string)
    for i in range(n//k):
        s = string[i * k : (i + 1) * k]
        p = ''
        for ch in s:
            if ch not in p:
                p += ch
        print(p)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)