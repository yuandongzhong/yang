def to_hex(dec_num):
    hex_num = hex(dec_num).replace('0x', '')
    x = 7 - len(hex_num)
    return "0" * x + hex_num


def to_sn(hex_str):
    the_sum = 0
    mod_s = 0
    add = 0
    n = 2
    for i in range(1, 8):
        the_sum += int(hex_str[-i], 16) * n
        n += 1
    mod_s = the_sum % 11
    add = 11 - mod_s
    if add <= 9:
        add = '0' + str(add)
    else:
        add = str(add)
    return hex_str + str(add)

# for i in range(1, 11):
#     print(i, to_hex(i), to_sn((to_hex(i))))


if __name__ == "__main__":
    start = int(input('Start Value: '))
    end = int(input('End Value: '))
    
    with open('sn.txt', 'w') as f:
        for i in range(start, end):
            f.write(to_sn((to_hex(i))))
            f.write('\n')

