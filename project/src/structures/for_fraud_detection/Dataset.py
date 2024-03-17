import os
import cv2
import sklearn

class Dataset:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.dataset_length = self.get_dataset_image_count()
        
        self.IMAGE_SIZE = 64
        self.IMAGE_COLOR_COUNT = 3
        self.images, self.labels = self.save_images_and_labels()
        
        self.TEST_RATIO = 0.25
        self.X_train, self.X_test, self.Y_train, self.Y_test = self.split_images()
        
        return
    

    def print_importing_progress(self, image_path, current_image_count, maximum_print_size):
        image_path_split = image_path.split("\\")[-3:]
        image_path_text = ""
        for path in image_path_split:
            image_path_text += (path + '/')
        image_path_text = '\'' + image_path_text.rstrip('/') + '\''
        
        text_to_print = f"Importing images: {image_path_text}, {current_image_count}/{self.dataset_length} ({round(((current_image_count / self.dataset_length) * 100), 2)}%)"
        length_of_text = len(text_to_print)
        print(text_to_print, " " * (maximum_print_size - length_of_text), end='\r\r')
        if length_of_text > maximum_print_size:
            maximum_print_size = length_of_text
            
        return maximum_print_size
    

    def get_dataset_image_count(self):
        image_count = 0
        for directory_name, directory_names, file_names in os.walk(self.dataset_path):
            for file_name in file_names:
                image_count += 1
                
        return image_count
    

    def save_images_and_labels(self):
        images = []
        labels = []
        maximum_printed_text_size = 0
        image_count = 0
        for directory_name, directory_names, file_names in os.walk(self.dataset_path):
            for file_name in file_names:
                image_path = os.path.join(directory_name, file_name)
                
                image = cv2.imread(image_path)
                resized_image = cv2.resize(image, (self.IMAGE_SIZE, self.IMAGE_SIZE))
                normalized_image = resized_image / 255.0
                flattened_image = normalized_image.reshape(self.IMAGE_SIZE * self.IMAGE_SIZE * self.IMAGE_COLOR_COUNT)
                
                label = str(os.path.join(directory_name, file_name)).split('\\')[-2]
                
                images.append(flattened_image)
                labels.append(label)
                image_count += 1
                
                maximum_printed_text_size = self.print_importing_progress(image_path, image_count, maximum_printed_text_size)
                
        return images, labels
    

    def split_images(self):
        X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(self.images, self.labels, test_size=self.TEST_RATIO)
        return X_train, X_test, Y_train, Y_test
    