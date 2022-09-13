def count_substring(string, sub_string):
    string_size = len(string)
    substring_size = len(sub_string)
    count = 0
    for i in range(string_size - substring_size + 1):
        compare_string = string[i:i + substring_size]
        if compare_string == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)