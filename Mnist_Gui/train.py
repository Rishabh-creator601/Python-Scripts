from tensorflow.keras.datasets import mnist 
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical




(x_train,y_train),(x_test,y_test) =  mnist.load_data()


x_train = x_train /255.0
x_test = x_test / 255.0



y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


model = Sequential([

	Flatten(input_shape=(784,)),
	Dense(512,activation='relu'),
	Dense(10,activation='softmax')


])


model.compile(loss='categorical_crossentropy',optimizer='adam',metrics='accuracy')



model.fit(x_train,y_train,epochs=10,batch_size=64)



loss,acc = model.evaluate(x_test,y_test)



if (acc * 100.0) >= 97.0:
	model.save("mnist_model.h5")
	print("Model Saved")
else:
	print("Model Accuracy is Less ! ")

