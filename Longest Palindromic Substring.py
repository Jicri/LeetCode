def Longest_Palindromic_Substring(word):
    a = []
    ans_1 = ''
    ansf_1 = []
    for i in range(len(word)):
        b = word[i:]
        a.append(b)
    print(a)
    for j in a:
        std = j[0]
        for d in range(len(j)):
            if j[d] == std:
                ans_1 = ans_1 + j[d]
                ansf_1.append(ans_1)
            else:
                std = j[d]
        print(ansf_1)
        break


Longest_Palindromic_Substring('ddmax')
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
