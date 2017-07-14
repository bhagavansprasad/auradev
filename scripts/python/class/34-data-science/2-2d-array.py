np_2d = np.array([1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7])
				  
print (np_2d)
print (np_2d.shape)
print (np_2d[0][2])
print (np_2d[0,2])
print (np_2d[:,1:3]) height and weight of 2 and 3rd
print (np_2d[1,:]) weight of all members

np.mean(np_city[:,0])
np.median(np_city[:,0])
np.corrcoef(np_city[:,0], np_city[:,1])
                               
				  #mean      distribution  standard  sample
height = np.round(np.random.normal(1.75,    0.20,       5000),      2)
weight = np.round(np.random.normal(60.32,   15,         5000),      2)
np_city = np.column_stack
