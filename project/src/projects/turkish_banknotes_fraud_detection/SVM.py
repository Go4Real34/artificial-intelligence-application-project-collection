import sklearn.svm
import pickle
import os

from ...structures import Dataset

class SVM:
    def __init__(self, dataset_path, model_save_path, resized_image_size, image_color_channel_count):
        self.dataset_path = dataset_path
        self.model_save_path = model_save_path
        
        self.IMAGE_SIZE = resized_image_size
        self.IMAGE_COLOR_CHANNEL_COUNT = image_color_channel_count
        
        self.dataset = Dataset(self.dataset_path, self.IMAGE_SIZE, self.IMAGE_COLOR_CHANNEL_COUNT)
        self.model = sklearn.svm.SVC(kernel='rbf')
        
        return
    
    def train_model(self):
        if os.path.exists(self.model_save_path):
            overwrite_confirm = input("An already trained model is found. Do you want to retrain the model? (Y/N):").upper().rstrip().lstrip()
            if overwrite_confirm != 'Y':
                with open(self.model_save_path, 'rb') as file:
                    self.model = pickle.load(file)
                    
                return

        print("\nModel training started.")
        self.model.fit(self.dataset.X_train, self.dataset.Y_train)
        print("Model training finished.")
        
        with open(self.model_save_path, "wb") as file:
            pickle.dump(self.model, file)
            
        print(f"Model has been saved to \"{self.model_save_path}\".")
        
        return
    