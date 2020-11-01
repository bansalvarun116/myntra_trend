from flask import Flask, render_template, url_for
import keras
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import ast



import generate_images
import cnn_pre_post
app=Flask(__name__)


#####     loading models      ###########

mgen=load_model("models/mnist_gen.h5")
mgan=load_model("models/mnist_gan.h5")
mdis=load_model("models/mnist_dis.h5")

#agen=load_model("models/attribute_gen.h5")
#agan=load_model("models/attribute_gan.h5")
#adis=load_model("models/attribute_dis.h5")

cnn=load_model("models/cnn_trend_score.h5")


#####     loading models      ###########

##########loading keys for attribute dataset################
file = open("myntra_key.txt", "r")

contents = file.read()
key = ast.literal_eval(contents)

file.close()


file = open("myntra_key2.txt", "r")

contents = file.read()
key2 = ast.literal_eval(contents)

file.close()


##########loading keys for attribute dataset################
def get_label(target):
    target=np.array(target)
    for i in key:
        check=np.array(key[i])
        if np.sum(check==target)==27:
            return key2[i]
    return 9 

@app.route("/")
@app.route("/home")
def home(): 
    image_file = url_for('static', filename="images/display.svg")
    image_file1 = url_for('static', filename="images/tab1.png")
    image_file2 = url_for('static', filename="images/tab2.png")
    image_file3 = url_for('static', filename="images/tab3.png")
    return render_template('index.html', image_file=image_file, image_file1=image_file1, image_file2=image_file2, image_file3=image_file3)

@app.route("/design_trendy_clothes")
def design_trendy_clothes():
    ## fmist dataset
    ##attribute dataset
    return "design_trendy_clothes"

    
@app.route("/design_trendy_clothes/fmnist")
def fmnist():
    ##### list of 0 to 9 #################
    temp=0
    return generate_images.generate_fake_samples(mgen,100,temp,28)


@app.route("/design_trendy_clothes/attribute_dataset")
def attribute_dataset():
    collar=0
    gender=0
    necktie=0
    pattern=0
    placket=0
    scarf=0
    skin_exp=0
    category=0
    neckline=0
    slevelength=0
    temp1=[]
    for i in range(6):
        if i==pattern:
            temp1.append(1)
        else:
            temp1.append(0)
    temp2=[]
    for i in range(8):
        if i==category:
            temp2.append(1)
        else:
            temp2.append(0)
    temp3=[]
    for j in range(4):
        if j==neckline:
            temp3.append(1)
        else:
            temp3.append(0)
    temp4=[]
    for j in range(3):
        if j==slevelength:
            temp4.append(1)
        else:
            temp4.append(0)
    tempf=[collar, gender,necktie]
    temp6=[placket,scarf,skin_exp]
    tempf=tempf+temp1
    tempf=tempf+temp6
    tempf=tempf+temp2
    tempf=tempf+temp3
    tempf=tempf+temp4



    temp=get_label(tempf)
    ##temp=0
    ##return generate_images.generate_fake_samples(mgen,100,temp,28)
    ## call something like this 
    return "attribute_dataset"



    
@app.route("/check_your_trend_score")
def check_your_trend_score():
    ###img=img
    ###taking image input 

    img=cnn_pre_post.pre(img)
    result=cnn_pre_post.post(cnn,img)
    
    return "check_your_trend_score"
    
    