import sklearn.svm
import sklearn.metrics
import pickle
import os
import threading

from ...structures import DatasetHandler, TimerHandler

class SVM:
    def __init__(self, dataset_path, model_save_folder_path, model_file_name, resized_image_size, image_color_channel_count, test_ratio, print_update_time):
        self.is_model_suitable = False
        
        self.dataset_path = dataset_path
        if not os.path.exists(self.dataset_path):
            os.makedirs(self.dataset_path)
            
            print("Please, either;")
            print("\tDownload the dataset from the Kaggle and extract to the location 'src/tests/dataset/': https://www.kaggle.com/datasets/baltacifatih/turkish-lira-banknote-dataset or,")
            print("\tClone or download the repository again from the project GitHub page: https://github.com/Go4Real34/artificial-intelligence-application-project-collection")
            return
            
        else:
            self.is_model_suitable = True
            
        self.model_save_folder_path = model_save_folder_path
        self.model_file_name = model_file_name
        self.model_save_path = os.path.join(self.model_save_folder_path, self.model_file_name)
        
        self.IMAGE_SIZE = resized_image_size
        self.IMAGE_COLOR_CHANNEL_COUNT = image_color_channel_count
        self.TEST_RATIO = test_ratio
        
        self.dataset = DatasetHandler(self.dataset_path, self.IMAGE_SIZE, self.IMAGE_COLOR_CHANNEL_COUNT, self.TEST_RATIO)
        self.model = sklearn.svm.SVC(kernel='rbf')
        
        self.PRINT_UPDATE_TIME = print_update_time
        self.timer = TimerHandler(True, self.PRINT_UPDATE_TIME)
        
        return
    
    def train(self):
        if not self.is_model_suitable:
            print("Model is not suitable for training. Please check the error messages above.")
            return
        
        if self.check_for_model(True):
            self.timer.is_model_main_thread_finished = True
            return
        
        self.timer.is_model_main_thread_finished = False
            
        train_thread = threading.Thread(target=self.train_model)
        time_thread = threading.Thread(target=self.timer.print_elapsed_time, kwargs={ 'is_training': True })
        
        train_thread.start()
        time_thread.start()
        time_thread.join()
        
        return
    
    def test(self):
        if not self.is_model_suitable:
            print("Model is not suitable for testing. Please check the error messages above.")
            return
        
        if self.check_for_model(False):
            self.timer.is_model_main_thread_finished = True
            return
        
        self.timer.is_model_main_thread_finished = False
            
        test_thread = threading.Thread(target=self.test_model)
        time_thread = threading.Thread(target=self.timer.print_elapsed_time, kwargs={ 'is_training': False })
        
        test_thread.start()
        time_thread.start()
        time_thread.join()
        
        return
    
    def train_model(self):
        print("\nModel training started.")
        print("Please wait while the model is being trained.")
        print("The time needed is dependent on your computer's hardware.")
        self.model.fit(self.dataset.X_train, self.dataset.Y_train)
        self.timer.is_model_main_thread_finished = True
        print("\nModel training finished.")
        
        if not os.path.exists(self.model_save_folder_path):
            os.makedirs(self.model_save_folder_path)
            
        with open(self.model_save_path, "wb") as file:
            pickle.dump(self.model, file)
            
        print(f"Model has been saved to \"{self.model_save_path}\".")
        
        return
    
    def test_model(self):
        print("\nModel testing started.")
        print("Please wait while the model is being trained.")
        print("The time needed is dependent on your computer's hardware.")
        predictions = self.model.predict(self.dataset.X_test)
        accuracy = sklearn.metrics.accuracy_score(self.dataset.Y_test, predictions)
        self.timer.is_model_main_thread_finished = True
        print(f"\nModel testing finished.")
        
        print(f"Accuracy: {round((accuracy * 100), 2)}%")
        
        return
    
    def check_for_model(self, is_training):
        if is_training:
            if os.path.exists(self.model_save_path):
                overwrite_confirm = input("An already trained model is found. Do you want to retrain the model? (Y/N):").upper().rstrip().lstrip()
                if overwrite_confirm != 'Y':
                    self.timer.is_model_main_thread_finished = True
                
                    with open(self.model_save_path, "rb") as file:
                        self.model = pickle.load(file)
                    
                    return True
                
                else:
                    os.remove(self.model_save_path)
                    self.timer.is_model_main_thread_finished = False
                    return False
                
        else:
            if os.path.exists(self.model_save_path):
                with open(self.model_save_path, "rb") as file:
                    self.timer.is_model_main_thread_finished = False
                    
                    self.model = pickle.load(file)
                    return False
                
            else:
                print("No trained model found. Please train the model first.")
                self.timer.is_model_main_thread_finished = True
                return True
    