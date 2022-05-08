from audioop import reverse
import random
import statistics

pro_num = input('請輸入商品數量 : ')
pro_num = int(pro_num)
price = input('請輸入希望的價差 : ')
price = int(price)
pro_value_list = []
care_list = []
for i in range(pro_num):
    pro_value = []
    for j in range(3):
        pro_value.append(random.randint(0, 100))
    pro_value_list.append(pro_value)
print(pro_value_list)
for s in pro_value_list:
    s.sort(reverse=True)
    if s[0]-s[len(s)-1] > price:
        count = 1
        if count == 1:
            a1 = statistics.mean(s)
            care_list.append(a1)
            count = 0
total = sum(care_list)
print(f'總共{len(care_list)}件商品超過價差，平均總和為{total}')
