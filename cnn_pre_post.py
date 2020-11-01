######### trendy score ############
import numpy as np
from keras.preprocessing import image

def pre(img):
    dim0=299
    dim1=240
    img = image.load_img(img)


    img=np.asarray(img)
    a,b,c=img.shape
    x_start=(a-dim0)//2
    x_end=x_start+dim0
    y_start=(b-dim1)//2
    y_end=y_start+dim1
    img=img[x_start:x_end,y_start:y_end,:]
    if img.shape[0]==300:
        img=img[1:,:,:]
    if img.shape[1]==241:
        img=img[:,1:,:]
    print(img.shape)
    return img

##### update ongoing trend ###########
ongoing_trend=[1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
ongoing_trend=np.asarray(ongoing_trend)
def post(model,img):
    img=img.reshape((1,299,240,3))
    vec=model.predict(img)
    vec=np.asarray(vec)
    result=np.sum(np.abs(vec-ongoing_trend))/np.sum(ongoing_trend)
    return result*100