import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)

print ("np_height :", np_height)
print ("np_weight :", np_weight)

bmi = np_height / np_weight ** 2
print ("bmi :", bmi)

np_double_height = np_height + np_height
print ("np_double_height :", np_double_height)

print ("np_double_height > 3.5                   :", np_double_height > 3.5)
print ("np_double_height[np_double_height > 3.5] :", np_double_height[np_double_height > 3.5])

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])
