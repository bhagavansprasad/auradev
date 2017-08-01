'''
import numpy as np
z = np.array([[3, 5, 0], 
              [0, 1, 7]])

print ("z          ", z)        #entire array
print ("[0,0]      ", z[0,  0]) #0 row and 0 col
print ("z[0:    ] :", z[0:])    #0 row and all col
print ("z[:,  0] :", z[:0])     #all rows 0 col
print ("z[1:,  1] :", z[1:,1])  #1 row 1 col
print ("z[0:,  :1] :", z[0:, :1])  #0 row 1 all col
print ("z[0:, 2:] :", z[0:, 2:])#0 row 2 col
'''

'''

import numpy as np
m = np.array([6, 2, 4])
n = np.array([True, False, True])
print(m ** n)
'''


'''
p = [2, 6, 8, 13, 5, 9]
#print(np.order(p, reverse=False)) #wrong statement
print(sorted(p, reverse=False))
'''


'''
import numpy as np
x = np.array([1, 13, 16, 17])
y = np.array([16, 23, 11, 7])
z = np.column_stack([x, y])
print ("x :", x)
print ("y :", y)
print ("z :", z)
print(z.shape)
'''

'''
import numpy as np
x = np.array([[1, 2, 7], [7, 7, 1]])
y = np.array([[6, 5, 5], [0, 6, 1]])
print ("x :", x)
print ("y :", y)
print (x * y)
'''

import numpy as np
store = np.array(["X", "Z", "Z", "Z", "Y"])
cost  = np.array([7, 8, 1, 1, 3])
select_cost = cost[store == "Z"]
print(select_cost)
