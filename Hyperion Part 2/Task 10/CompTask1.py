import numpy as np 


"""FIRST QUESTION"""

# this way is incorrect because the syntax is invalid
# np.array((1, 0, 0), (0, 1, 0), (0, 0, 1,dtype=float)

# this is the correct way to lay it out
np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)],dtype=float)


"""SECOND QUESTION"""

# this is a 1 dimensional array
a = np.array([0, 0, 0])
print(a)

# this is a 2 dimensional array
a2 = np.array([[0, 0, 0]])
print(a2)

# The difference between 'a' and 'a2' is that they have different dimensions


"""THIRD QUESTION"""

arr = np.linspace(1, 48, 48).reshape(3, 4, 4)
print(arr)

# 20.0
print(arr[1][0][3])

# [9, 10, 11, 12]
print(arr[0][2])

# [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
print(arr[2])

# [[5. 6.], [21. 22.] [37. 38.]]
print(arr[0:3,1,0:2])

# [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
print(arr[2,0:4,::-1][0:4,0:2])

# [[ 13., 9., 5., 1.], [29., 25., 21., 17.] , [45., 41., 37., 33.]]
print(arr[0:3,0:4,0][0:3,::-1])
