def add_two_num(data_1, data_2):
    ans_1 = []
    ans_2 = []
    a = ''
    b = ''
    ans_fin = []
    if len(data_1) < 100 and len(data_2) < 100:
        for i in range(len(data_1)):
            if (data_1[i] > 0 and len(str(data_1[i])) == 1):
                ans_1.append(data_1[len(data_1)-(i+1)])
                a = a + str(data_1[len(data_1)-(i+1)])
            else:
                print('輸入數字不能超過10', 'data_1', data_1[i])
        for j in range(len(data_2)):
            if (data_2[j] > 0 and len(str(data_2[j])) == 1):
                ans_2.append(data_2[len(data_2)-(j+1)])
                b = b + str(data_2[len(data_2)-(j+1)])
            else:
                print('輸入數字不能超過10', 'data_2', data_2[j])
        if len(ans_1) == len(data_1) and len(ans_2) == len(data_2):
            sum = int(a) + int(b)
            sum = str(sum)
            for v in range(len(sum)):
                ans_fin.append(sum[len(sum)-(v+1)])
            print(ans_fin)
    else:
        print('請不要輸入100筆以上的資料')


add_two_num([1, 6, 4], [5, 3, 7, 6, 18, 4])


# l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807
