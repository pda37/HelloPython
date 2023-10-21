"""
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释:
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
"""
def largestTriangleArea(points):
    l_max = 0
    h_max = 0
    s_max1 = 0
    s_max2 = 0
    a1, b1, c1, d1, a2, b2, c2, d2 = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            if abs(points[i][0]-points[j][0]) > l_max:
                a1 = points[i][0]
                b1 = points[i][1]
                c1 = points[j][0]
                d1 = points[j][1]
                l_max = abs(points[i][0]-points[j][0])
            if abs(points[i][1]-points[j][1]) > h_max:
                a2 = points[i][0]
                b2 = points[i][1]
                c2 = points[j][0]
                d2 = points[j][1]
                h_max = abs(points[i][0]-points[j][0])
    print(a1, b1, c1, d1, a2, b2, c2, d2)
    # 需要去掉已选中的两点
    for k in points:
        e = k[0]
        f = k[1]
        if a1 != e and c1 != e and b1 != f and d1 != f:
            s1 = abs(a1 * d1 + b1 * e + c1 * f - a1 * f - b1 * c1 - d1 * e) / 2
            s_max1 = max(s_max1, s1)
        if a2 != e and c2 != e and b2 != f and d2 != f:
            s2 = abs(a2 * d2 + b2 * e + c2 * f - a1 * f - b2 * c2 - d2 * e) / 2
            s_max2 = max(s_max2, s2)
    return max(s_max1, s_max2)


print(largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))


# def largestTriangleArea(points):
#     s_max = 0
#     for i in range(len(points)-2):
#         for j in range(i+1, len(points)-1):
#             for k in range(j+1, len(points)):
#                 a = points[i][0]
#                 b = points[i][1]
#                 c = points[j][0]
#                 d = points[j][1]
#                 e = points[k][0]
#                 f = points[k][1]
#                 s = abs(a*d+b*e+c*f-a*f-b*c-d*e)/2
#                 s_max = max(s_max, s)
#     return s_max

