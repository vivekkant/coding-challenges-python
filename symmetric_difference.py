

if __name__ == '__main__':
    m = int(input())
    m_set = set(map(int, input().split()))
    n = int(input())
    n_set = set(map(int, input().split()))

    m_diff = list(m_set.difference(n_set))
    n_diff = list(n_set.difference(m_set))

    l = [*m_diff, *n_diff]
    l.sort()

    for i in l:
        print(i)

