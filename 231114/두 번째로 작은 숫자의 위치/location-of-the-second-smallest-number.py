n = int(input())
datas = list(map(int, input().split()))
nums = []
for i in range(len(datas)):
    nums.append((datas[i], i + 1))
nums.sort()
result = nums[0]
for i in range(len(nums)):
    if nums[i][0] > result[0]:
        result = nums[i]
        break

if result == nums[0] or datas.count(result[0]) > 1:
    print(-1)
else:
    print(result[1])