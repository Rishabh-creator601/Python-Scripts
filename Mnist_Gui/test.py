from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import array_to_img,img_to_array
import cv2
import numpy as np


model = load_model("mnist_model.h5")


img = cv2.imread("one.png",cv2.IMREAD_UNCHANGED)
img = img_to_array(img)
img = img.reshape(-1,784)


print(np.argmax(model.predict(img),axis=1))

