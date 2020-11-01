import numpy as np
import matplotlib.pyplot as plt
import os


def generate_latent_points(latent_dim, n_class,n_samples=50):

    x_input = np.random.randn(latent_dim * n_samples)

    z_input = x_input.reshape(n_samples, latent_dim)

    temp=np.array([n_class])
    temp=temp.reshape((-1,1))
    
    labels = temp.repeat(n_samples,axis=0)
    return [z_input, labels]


def generate_fake_samples(generator, latent_dim, n_class ,p,n_samples=50):

    z_input, labels_input = generate_latent_points(latent_dim, n_class, n_samples)
    
 

    images = generator.predict([z_input, labels_input])
    images=images.reshape((50,p,p))
    plt.figure(figsize=(20,20))
    for i in range(1,10):
        for j in range(1,6):
            plt.subplot(10,5,i*5+j)
            plt.imshow(images[i*5+j-1])
    plt.savefig('static/images/plot.png')
    
    ###########return things to be changed#############
    return "images"
