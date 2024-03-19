import sklearn.neighbors
import os

from ...structures import ModelHandler, DatasetHandler, TimerHandler

class KNN(ModelHandler):
    def __init__(self, dataset_path, model_save_folder_path, model_file_name, resized_image_size, image_color_channel_count, test_ratio, print_update_time, neighbor_count):
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
        self.NEIGHBOR_COUNT = neighbor_count
        
        self.dataset = DatasetHandler(self.dataset_path, self.IMAGE_SIZE, self.IMAGE_COLOR_CHANNEL_COUNT, self.TEST_RATIO)
        self.model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=self.NEIGHBOR_COUNT)
        
        self.PRINT_UPDATE_TIME = print_update_time
        self.timer = TimerHandler(True, self.PRINT_UPDATE_TIME)
        
        return
    