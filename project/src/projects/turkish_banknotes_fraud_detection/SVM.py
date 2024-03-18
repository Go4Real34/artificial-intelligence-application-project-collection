import sklearn.svm
import sklearn.metrics
import pickle
import os
import threading
import time

from ...structures import Dataset

class SVM:
    def __init__(self, dataset_path, model_save_path, resized_image_size, image_color_channel_count, test_ratio, print_update_time):
        self.dataset_path = dataset_path
        self.model_save_path = model_save_path
        
        self.IMAGE_SIZE = resized_image_size
        self.IMAGE_COLOR_CHANNEL_COUNT = image_color_channel_count
        self.TEST_RATIO = test_ratio
        
        self.dataset = Dataset(self.dataset_path, self.IMAGE_SIZE, self.IMAGE_COLOR_CHANNEL_COUNT, self.TEST_RATIO)
        self.model = sklearn.svm.SVC(kernel='rbf')
        
        self.is_model_main_thread_finished = False
        
        self.HOURS_TO_MINUTES = 60
        self.MINUTES_TO_SECONDS = 60
        self.HOURS_TO_SECONDS = self.HOURS_TO_MINUTES * self.MINUTES_TO_SECONDS
        
        self.PRINT_UPDATE_TIME = print_update_time
        
        return
    
    def train(self):
        if self.is_model_main_thread_finished:
            self.is_model_main_thread_finished = False
            
        train_thread = threading.Thread(target=self.train_model)
        time_thread = threading.Thread(target=self.print_elapsed_time, kwargs={ 'is_training': True })
        
        train_thread.start()
        time_thread.start()
        time_thread.join()
        
        return
    
    def train_model(self):
        if os.path.exists(self.model_save_path):
            overwrite_confirm = input("An already trained model is found. Do you want to retrain the model? (Y/N):").upper().rstrip().lstrip()
            if overwrite_confirm != 'Y':
                self.is_model_main_thread_finished = True
                
                with open(self.model_save_path, 'rb') as file:
                    self.model = pickle.load(file)
                    
                return

        if self.is_model_main_thread_finished:
            self.is_model_main_thread_finished = False
            
        print("\nModel training started.")
        self.model.fit(self.dataset.X_train, self.dataset.Y_train)
        self.is_model_main_thread_finished = True
        print("Model training finished.")
        
        with open(self.model_save_path, "wb") as file:
            pickle.dump(self.model, file)
            
        print(f"Model has been saved to \"{self.model_save_path}\".")
        
        return
    
    def test_model(self):
        if not os.path.exists(self.model_save_path):
            print("No trained model found. Model testing is not possible.")
            return
        
        print("\nModel testing started.")
        predictions = self.model.predict(self.dataset.X_test)
        accuracy = sklearn.metrics.accuracy_score(self.dataset.Y_test, predictions)
        print(f"Model testing finished. Accuracy: {round((accuracy * 100), 2)}%")
        
        return
    
    def print_elapsed_time(self, is_training):
        maximum_print_size = 0
    
        start_time = time.perf_counter()
        while not self.is_model_main_thread_finished:
            elapsed_time = time.perf_counter() - start_time
        
            if is_training:
                text_to_print = f"Model has been training for {self.format_time(elapsed_time)}."
            
            else:
                text_to_print = f"Model has been testing for {self.format_time(elapsed_time)}."
            
            length_of_text = len(text_to_print)
            print(text_to_print, " " * (maximum_print_size - length_of_text), end='\r')
            if length_of_text > maximum_print_size:
                maximum_print_size = length_of_text
        
            time.sleep(self.PRINT_UPDATE_TIME)
        
        return

    def format_time(self, time_in_s):
        hours, seconds = divmod(time_in_s, self.HOURS_TO_SECONDS)
        minutes, seconds = divmod(time_in_s, self.MINUTES_TO_SECONDS)
    
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
    
        formatted_time = ""
        if hours == 0 and minutes == 0 and seconds == 0:
            formatted_time = "0s"
    
        else:
            if hours > 0:
                formatted_time += f"{hours}h "
            if minutes > 0:
                formatted_time += f"{minutes}m "
            if seconds > 0:
                formatted_time += f"{seconds}s "
            
        return formatted_time.lstrip().rstrip()
    