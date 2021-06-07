# v = [17, 92 ,18, 33, 58, 7, 33, 42]
#
# def big(n, v):
#     if n <= 1:
#         return v[n-1]
#     else:
#         if(v[n-1]>big(n-2, v)):
#             return v[n-1]
#         else:
#             return big(n-2, v)
#
# print(big(len(v), v))

def find_max(nums, n): # nums 는 리스트 / n은 리스트의 길이
# 맨 처음 1일 때를 정의 해 주는 것
    if n == 1:
        return nums[0]

# 자동으로 계산 하도록 (재귀) 끝날때 까지 0 부터 n까지 수를 갱신해주면서 갱신할 때마다 밑에 있는 연산을 실행
    max_num = find_max(nums, n-1)

# 어떻게 연산을 할 것인지
    if(max_num > nums[n-1]):
        return max_num
    else:
        return nums[n-1]

a = [17, 92, 18, 24, 35]
print(find_max(a, len(a)))