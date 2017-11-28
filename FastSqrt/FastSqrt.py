# The above question can be done using divide and conquer algorithm
# recursively check the
#  sqrt(number)
#    while left<right:
#        mid=(right+left)/2
#        if |(number-(mid ^2))|<0.01:
#            print mid
#            break
#        else if  (mid ^2)> number:
#            right=mid
#        else
#            left=mid

# Time Complexity
# Since every time we are eliminating almost half of the side on which we are supposed to recure,
# hence the Time complexity is
# O (log n)

# Space Complexity
# Since in every call we are using a constant amount of space to do some work
# O(1)


x = input()
number = float(x)
if number == 0 or number == 1:
    print(number)
else:
    left = 0
    right = number if number > 1 else 1
    while left < right:
        mid = (right + left) / 2
        if abs(number - (mid * mid)) < 0.01:
            print(mid)
            break
        elif (mid * mid) > number:
            right = mid
        else:
            left = mid

