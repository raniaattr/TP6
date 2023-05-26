import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Question1
image=plt.imread('citroen.jpg')
plt.imshow(image)
plt.show()

# Question2
R=image[:,:,0]/255
G=image[:,:,1]/255
B=image[:,:,2]/255
print(np.min(R,axis=0))




plt.imshow(image[:,:,0],cmap='Reds')
plt.colorbar()
#plt.show()
plt.imshow(image[:,:,1],cmap='Greens')
plt.colorbar()
#plt.show()
plt.imshow(image[:,:,2],cmap='Blues')
plt.colorbar()
#plt.show()