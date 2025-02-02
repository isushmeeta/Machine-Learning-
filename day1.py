import numpy as np
arr=np.array([1,2,3,4,5])#1Darray
print(arr)

#checking numpy version 
print(np.__version__)

# to check dimensions
print(arr.ndim)

#0D array 
arr1=np.array(42)
print(arr1)
print(arr1.ndim)

#2D array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.ndim)


#3D array
arr3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr3)
print(arr3.ndim)

#an array with higher dimensions a be defined 
arr4= np.array([1,2,3,4], ndmin=5) #here defined dimension is 5
print (arr4)


#Access the element on the first row, second column:
arr5 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr5[0, 1]) #0=first row , 1=second column 
print('5th element on 2nd row: ', arr5[1, 4])


#Access the third element of the second array of the first array:
arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr6[0, 1, 2]) #6 
print('Last element from 2nd dim: ', arr6[1, -1])
