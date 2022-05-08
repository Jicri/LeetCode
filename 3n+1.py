ans_1 = []
max_num = []


def ACM100(i, j):
    for num in range(i, j+1):
        ans = []
        while True:
            if num == 1:
                break
            elif num % 2 != 0:
                num = (3*num) + 1
            elif num % 2 == 0:
                num = num / 2
            ans.append(num)
        ans_1.append(ans)
    # print(ans_1)
    # 找最大長度
    max = ans_1[0]
    for s1 in range(len(ans_1)):
        if s1 > 0:
            if len(ans_1[s1]) >= len(max):
                max = ans_1[s1]
                if s1 == len(ans_1)-1:
                    for s2 in range(len(ans_1)):
                        if len(ans_1[s2]) == len(max):
                            max_num.append(s2)
            else:
                if s1 == len(ans_1)-1:
                    for s2 in range(len(ans_1)):
                        if len(ans_1[s2]) == len(max):
                            max_num.append(s2)

    # #找最大長度對應的數字
    # for s2 in range(len(ans_1)):
    #     if len(ans_1[s2]) == len(max):
    #         max_num.append(s2)
    print(max_num)
    for s3 in max_num:
        print(f'{i+s3}的時候有最大長度{len(max)}')


ACM100(80, 120)
