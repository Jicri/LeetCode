def Longest_Palindromic_Substring(word):
    a = []
    ansf_1 = []
    ansf_2 = []
    ans_f = []
    for i in range(len(word)):
        b = word[i:]
        a.append(b)
    print(a)
    for j in a:
        std = j[0]
        ans_1 = ''
        ans_2 = ''
        for d in range(len(j)):
            if j[d] == std:
                ans_1 = ans_1 + j[d]
                if len(ans_1) > 1 and ans_1 not in ansf_1:
                    ansf_1.append(ans_1)
            else:
                std = j[d]
                ans_1 = ''
                ans_1 = ans_1 + j[d]
        for s in j:
            ans_2 = ans_2 + s
            if len(ans_2) > 2:
                sa = 0
                for s1 in range(len(ans_2)):
                    if ans_2[s1] == ans_2[len(ans_2)-(1+s1)]:
                        sa += 1
                        if sa == len(ans_2):
                            ansf_2.append(ans_2)
    ansf_3 = ansf_1 + ansf_2
    max = ansf_3[0]
    for s2 in ansf_3:
        if len(s2) >= len(max):
            max = s2
    for s3 in ansf_3:
        if len(s3) == len(max):
            ans_f.append(s3)

    # print(ansf_1)
    # print(ansf_2)
    print(ansf_3)
    print(ans_f)


Longest_Palindromic_Substring('aeabcbwew')
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
