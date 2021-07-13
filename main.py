from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
   
# Initialising the ImageDataGenerator class.
# We will pass in the augmentation parameters in the constructor.
datagen = ImageDataGenerator(
        rotation_range = 40,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True,
        brightness_range = (0.5, 1.5))
    
# Loading a sample image 

path = r'rust'
count=0
for filename in os.listdir(path):
    count+=1    
    p = path + "'" + filename    
    p = p.replace("'", "\\")
    img = load_img(p) 

    # Converting the input sample image to an array
    x = img_to_array(img)
    # Reshaping the input image
    x = x.reshape((1, ) + x.shape) 
    
    # Generating and saving 5 augmented samples 
    # using the above defined parameters. 
    i = 0
    for batch in datagen.flow(x, batch_size = 1,
                            save_to_dir ='russt', 
                            save_prefix ='rust', save_format ='png'):
        i += 1
        if i > 2:
            break