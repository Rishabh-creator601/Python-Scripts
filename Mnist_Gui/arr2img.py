from tensorflow.keras.datasets import mnist 
from tensorflow.keras.preprocessing.image import array_to_img
import cv2,os ,tqdm
import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image




def make_dir(name):
	if not os.path.exists(name):
		os.mkdir(name)


make_dir("images")

(x_train,y_train),(x_test,y_test) =  mnist.load_data()

x_train = np.array(x_train).astype("float32") / 255.0






for i in tqdm.tqdm(range(len(x_train) +1)):
	img = array_to_img(x_train[i].astype("float32").reshape(28,28,1))
	img.save("images/img_{}.png".format(i+1))



