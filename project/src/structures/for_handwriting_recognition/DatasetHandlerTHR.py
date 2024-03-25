import os
import cv2
import tensorflow
import tqdm

class DatasetHandlerTHR:
    def __init__(self, dataset_path, image_size, test_ratio):
        self.IMAGE_SIZE = image_size
        
        self.is_dataset_suitable = True
        if (dataset_path is None) and (test_ratio is None):
            self.is_dataset_suitable = False
            return
        
        self.dataset_path = dataset_path
        self.dataset_size = self.get_dataset_image_count()
        
        self.images, self.labels = self.save_images_and_labels()
        
        self.TEST_RATIO = test_ratio
        self.X_train, self.X_test, self.Y_train, self.Y_test = self.split_images()
        
        return
    
    def get_dataset_image_count(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        image_count = 0
        for directory_name, directory_names, file_names in os.walk(self.dataset_path):
            for file_name in file_names:
                if not file_name.endswith(".jpg"):
                    continue
                
                image_count += 1
                
        return image_count
        
    def save_images_and_labels(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        images = []
        labels = []
        
        with tqdm.tqdm(desc="Importing Images...", unit=" images", total=self.dataset_size) as progress_bar:
            for directory_name, directory_names, file_names in os.walk(self.dataset_path):
                for file_name in file_names:
                    if not file_name.endswith(".jpg"):
                        continue
                
                    image_path = os.path.join(directory_name, file_name)
                    image_name = '/'.join(image_path.split('\\')[-3:])
                    
                    image = self.process_image(image_path, False)
                    label = str(os.path.join(directory_name, file_name)).split('\\')[-2]
                    
                    images.append(image)
                    labels.append(label)
                    
                    progress_bar.desc = f"Importing Images... ({image_name})"
                    progress_bar.update(1)
                    
        return images, labels

    def process_image(self, image_path, is_user_image):
        image = cv2.imread(image_path)

        if is_user_image:
            resized_image = cv2.resize(image, (self.IMAGE_SIZE, self.IMAGE_SIZE))
            
        else:
            resized_image = image
        
        return resized_image
    
    def split_images(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        X_train, X_test, Y_train, Y_test = tensorflow.keras.utils.split_dataset(self.images, self.labels, test_size=self.TEST_RATIO)
        return X_train, X_test, Y_train, Y_test
    