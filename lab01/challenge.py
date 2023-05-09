def get_blocks(string):
    count = 1
    str_count = {}
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            while count != 0:
                str_count.update({i-count+1: count})
                count -= 1
            count = 1
    while count != 0:
        str_count.update({len(string)-count: count})
        count -= 1
    return str_count

def get_string(a, b, a_ind, b_ind, a_count, b_count, string):
    str1, str2 = "", ""
    if a_ind >= len(a):
        return string
    a_ind_next = a_ind + a_count[a_ind]
    try:
        b_ind_next = b.index(a[a_ind], b_ind)
        # b_len_next = b_count[b_ind_next+1]
        # a_len_next = a.index(b[b_ind_next+b_len_next], a_ind) - a_ind
        # if b_len_next > a_len_next:
        str1 =  get_string(b, a, b_ind_next+1, a_ind_next, b_count, a_count, string+a[a_ind:a_ind_next])
    except ValueError or KeyError:
        pass

    str2 = get_string(a, b, a_ind_next, b_ind, a_count, b_count, string+a[a_ind:a_ind_next])

    if len(str1) < len(str2):
        return str2
    else:
        return str1

a = input()
b = input()

a_next_block = get_blocks(a)
b_next_block = get_blocks(b)

# print(a_next_block, b_next_block)

string1 = get_string(a, b, 0, 0, a_next_block, b_next_block, "")
string2 = get_string(b, a, 0, 0, b_next_block, a_next_block, "")

if len(string1) < len(string2):
    final_string = string2
else:
    final_string = string1

for i in final_string:
    if i in a and i in b:
        print(final_string)
        print(len(final_string))
        exit()
print("*")
