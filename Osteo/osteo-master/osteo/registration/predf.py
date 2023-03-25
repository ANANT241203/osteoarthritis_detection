from keras.models import load_model

from tensorflow.keras.preprocessing.image import ImageDataGenerator

model = load_model('osteox.h5')

path=r"C:\Users\Sstan\Desktop\Osteo\osteo-master\osteo\media\osteo"


def prediction():
    test_data = ImageDataGenerator(rescale=1./255)
    test_img= test_data.flow_from_directory(
            path,
            target_size=(150, 150),
            batch_size=1,
            class_mode='binary')
    
    pred = model.predict(test_img)
    
    return pred[0][0]
