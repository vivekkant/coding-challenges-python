
def is_vowel(ch):
    vowel = 'AEIOU'
    return ch in vowel

def get_substring_list(s, start_vowel):
    i = 0
    count = 0
    for ch in s:
        if is_vowel(ch) == start_vowel:
            count += (len(s) - i)
        i += 1
    return count

def minion_game(string):
    stuart = get_substring_list(string, False)
    kevin = get_substring_list(string, True)
    if (stuart > kevin):
        print('Stuart', stuart)
    elif (stuart < kevin):
        print('Kevin', kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)

