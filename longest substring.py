def longest_substring(str_num):
    s = ''
    s1 = []
    # 收集在不重複下的各個長度
    for d in range(len(str_num)):
        if str_num[d] not in s:
            s = s + str_num[d]
        elif str_num[d] in s:
            s1.append(s)
            s = ''
            s = s + str_num[d]
    s1.append(s)
    # 去判斷哪個是最大長度
    for i in s1:
        max = len(s1[0])
        if len(i) >= max:
            max = len(i)
            max_name = i

    print(s1)
    print(max_name, 'with the length of', max)


longest_substring('efrtghabcr')


#s = "abcabcbb"
#s = "abcaecbb"
