import numpy as np
#set random seed for repo
np.random.seed(42)
#generate a 2d numpy arr
data=np.random.rand(100,3)
#mean and std deviation
mean=np.mean(data, axis=0)
std=np.std(data,axis=0)
#normalize using broadcasting
normalized=(data-mean)/std
#slice the normalized 
split_index=int(0.8 * normalized.shape[0])
train_set = normalized[: split_index]
test_set = normalized[split_index:]
#modifies sliced value
print("value before modification:", normalized[0,0])
train_set[0,0]= 999
print("value after modification:",normalized[0,0])
#print
print("\nOriginal data shape:", data.shape)
print("mean shape:", mean.shape)
print("standard deviation shape:", std.shape)
print("training set shape:", train_set.shape)
print("test set shape:", test_set.shape)
print("\nExplanation:")
print("since slicing creates a view (not a copy),modifying train_set")
print("also modified the corresponding value in the normalized array.")
    
