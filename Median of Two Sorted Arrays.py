def median_two_array(nums1, nums2):
    a = nums1 + nums2
    a.sort(reverse=False)
    print(a)
    if len(a) % 2 != 0:
        b = int((len(a)-1)*0.5)
        print('奇數中位數 = ', a[b])
    elif len(a) % 2 == 0:
        c1 = int(((len(a)-1) / 2)-0.5)
        c2 = int(((len(a)-1) / 2)+0.5)
        b = (a[c1] + a[c2]) / 2
        print('偶數中位數 = ', b)


median_two_array([1, 2, 3, 5, 9, 50, 60], [2, 3, 6, 8, 12, 89])
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
