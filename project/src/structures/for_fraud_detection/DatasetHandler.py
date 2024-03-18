import os
import cv2
import sklearn
import tqdm

class DatasetHandler:
    def __init__(self, dataset_path, resized_image_size, image_color_channel_count, test_ratio):
        self.dataset_path = dataset_path
        self.dataset_size = self.get_dataset_image_count()
        
        self.IMAGE_SIZE = resized_image_size
        self.IMAGE_COLOR_COUNT = image_color_channel_count
        self.images, self.labels = self.save_images_and_labels()
        
        self.TEST_RATIO = test_ratio
        self.X_train, self.X_test, self.Y_train, self.Y_test = self.split_images()
        
        return
    
    def get_dataset_image_count(self):
        image_count = 0
        for directory_name, directory_names, file_names in os.walk(self.dataset_path):
            for file_name in file_names:
                if file_name.endswith(".pkl"):
                    continue
                
                image_count += 1
                
        return image_count

    def save_images_and_labels(self):
        images = []
        labels = []
        
        with tqdm.tqdm(desc="Importing Images...", unit=" images", total=self.dataset_size) as progress_bar:
            for directory_name, directory_names, file_names in os.walk(self.dataset_path):
                for file_name in file_names:
                    if file_name.endswith(".pkl"):
                        continue
                
                    image_path = os.path.join(directory_name, file_name)
                    image_name = '/'.join(image_path.split('\\')[-3:])
                    
                    image = cv2.imread(image_path)
                    resized_image = cv2.resize(image, (self.IMAGE_SIZE, self.IMAGE_SIZE))
                    normalized_image = resized_image / 255.0
                    flattened_image = normalized_image.reshape(self.IMAGE_SIZE * self.IMAGE_SIZE * self.IMAGE_COLOR_COUNT)
                    
                    label = str(os.path.join(directory_name, file_name)).split('\\')[-2]
                    images.append(flattened_image)
                    labels.append(label)
                    
                    progress_bar.desc = f"Importing Images... ({image_name})"
                    progress_bar.update(1)
                    
            return images, labels
    

    def split_images(self):
        X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(self.images, self.labels, test_size=self.TEST_RATIO)
        return X_train, X_test, Y_train, Y_test
    