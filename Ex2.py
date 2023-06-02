import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def conversion(image_RGB):
    R=image_RGB[:,:,0]/255
    G=image_RGB[:,:,1]/255
    B=image_RGB[:,:,2]/255
    Cmin = np.min(image_RGB / 255, axis=2)
    Cmax = np.max(image_RGB / 255, axis=2)
    delta=Cmax-Cmin
    H = np.select([np.logical_and(Cmax==R, delta!=0), np.logical_and(Cmax==G,delta!=0), np.logical_and(Cmax==B,delta!=0)], [1/6*((G-B)/delta)%6, 1/6*((B-R)/delta)+2, 1/6*((R-G)/delta)+4], default=0)
    S = np.select([Cmax!=0], [delta/Cmax], default=0)
    V = Cmax
    image_HSV = np.stack((H, S, V),axis=2)
    return image_HSV


if __name__=='__main__':

    #Question1
    image_RGB = plt.imread('citroen.jpg')
    plt.imshow(image_RGB)
    plt.title('Image RGB')
    plt.show()

    #Question2
    image_HSV=conversion(image_RGB)
    plt.imshow(image_HSV)
    plt.colorbar()
    plt.title('Image HSV')
    plt.show()

    #Question3
    print(f'Canal Hue : {image_HSV[:, :, 0]}')
    image_H=image_HSV.copy()
    image_H[:,:,1]=0
    image_H[:,:,2]=0
    plt.imshow(image_H)
    plt.title('Image canal H')
    plt.show()
    print(f'Canal Saturation : {image_HSV[:, :, 1]}')
    image_S=image_HSV.copy()
    image_S[:,:,0]=0
    image_S[:,:,2]=0
    plt.imshow(image_S)
    plt.title('Image canal S')
    plt.show()
    print(f'Canal Value : {image_HSV[:, :, 2]}')
    image_V=image_HSV.copy()
    image_V[:,:,1]=0
    image_V[:,:,0]=0
    plt.imshow(image_V)
    plt.title('Image canal V')
    plt.show()
