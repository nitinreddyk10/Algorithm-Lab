a = input()
b = input()

def get_count(str):
    count = 1
    str_count = {}
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            count += 1
        else:
            while count != 0:
                str_count.update({i-count+1: count})
                count -= 1
            count = 1
    while count != 0:
        str_count.update({len(str)-count: count})
        count -= 1
    return str_count

a_count = get_count(a)
b_count = get_count(b)

# print(a_count, b_count)

def get_string(a, b, a_ind, b_ind, a_count, b_count, str):
    str1, str2 = "", ""
    if a_ind >= len(a):
        return str
    a_ind_next = a_ind + a_count[a_ind]
    try:
        b_ind_next = b.index(a[a_ind], b_ind)
        # b_len_next = b_count[b_ind_next+1]
        # a_len_next = a.index(b[b_ind_next+b_len_next], a_ind) - a_ind
        # if b_len_next > a_len_next:
        str1 =  get_string(b, a, b_ind_next+1, a_ind_next, b_count, a_count, str+a[a_ind:a_ind_next])
    except ValueError:
        pass
    except KeyError:
        # return str
        pass

    str2 = get_string(a, b, a_ind_next, b_ind, a_count, b_count, str+a[a_ind:a_ind_next])

    if len(str1) < len(str2):
        return str2
    else:
        return str1

max_str1 = get_string(a, b, 0, 0, a_count, b_count, "")
max_str2 = get_string(b, a, 0, 0, b_count, a_count, "")
if len(max_str1) < len(max_str2):
    max_str = max_str2
else:
    max_str = max_str1

count = 0
for i in max_str:
    if i in a and i in b:
        print(max_str)
        print(len(max_str))
        exit()
print("*")
    