nums = [int(s) for s in filter(None, input().split())]

print(nums[0], end = '')
for i in range(2, len(nums)):
    print("-{},{}".format(nums[i]-1, nums[i]+1), end = '')
print("-{}".format(nums[1]))
'''
The first line splits the string of numbers and spaces on the spaces, then
interprets these as ints which are placed in a list.

nums[0] is the start of the range which is printed first, without a newline.
Then, all of the ranges are printed inside of a loop through the list.

Lastly, nums[1] is printed, representing the end of the range.
'''
