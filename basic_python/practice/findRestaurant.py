def findRestaurant(list1, list2):
    m, n = len(list1), len(list2)
    ans = []
    max_index = 2000
    if m < n:
        for i in range(m):
            if list1[i] in list2:
                if i + list2.index(list1[i]) < max_index:
                    ans = [list1[i]]
                    max_index = i + list2.index(list1[i])
                elif i + list2.index(list1[i]) == max_index:
                    ans.append(list1[i])
                    max_index = i + list2.index(list1[i])
    else:
        for i in range(n):
            if list2[i] in list1:
                if i + list1.index(list2[i]) < max_index:
                    ans = [list2[i]]
                    max_index = i + list1.index(list2[i])
                elif i + list1.index(list2[i]) == max_index:
                    ans.append(list2[i])
                    max_index = i + list1.index(list2[i])
    return ans


print(findRestaurant(["KFC", "Shogun", "Burger King"], ["Shogun", "Tapioca Express", "Burger King", "KFC"]))
