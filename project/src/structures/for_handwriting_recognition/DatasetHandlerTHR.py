import os
import cv2
import numpy
import sklearn.model_selection
import tqdm
import shutil
import subprocess
import psutil

class DatasetHandlerTHR:
    def __init__(self, dataset_path, dataset_folder_name, image_size, test_ratio):
        self.IMAGE_SIZE = image_size
        
        self.is_dataset_suitable = True
        if (dataset_path is None) and (test_ratio is None):
            self.is_dataset_suitable = False
            return
        
        self.dataset_path = dataset_path
        self.dataset_folder_name = dataset_folder_name
        self.dataset_folder_path = os.path.join(self.dataset_path, self.dataset_folder_name)
        
        self.image_count, self.folder_count = 0, 0
        self.total_items_in_dataset = 0
        
        self.RAR_FILE_INFORMATION_LINE_COUNT_OFFSET = 8
        self.rars, self.total_items_in_rars, self.longest_path_size = [], 0, 0
        
        self.process = None
        self.images, self.labels = [], []
        
        if os.path.exists(self.dataset_folder_path):
            self.image_count, self.folder_count = self.get_dataset_item_counts()
            self.total_items_in_dataset = self.image_count + self.folder_count
            self.rars, self.total_items_in_rars, self.longest_path_size = self.count_rars()
            if self.total_items_in_dataset != self.total_items_in_rars:
                print("\nAll dataset images was not verified. Program will try to re-extract dataset contents.\n")
                if not self.check_winrar():
                    print("\nWinRAR application is either not installed in or not in the PATH variables of your system.")
                    print("Please install WinRAR from here: https://www.win-rar.com/start.html?&L=0, and add it to PATH variables of your computer.")
                    self.is_dataset_suitable = False
                    return
                
                self.clear_dataset()
                self.extract_dataset()
                self.image_count = self.get_dataset_item_counts()
                self.images, self.labels = self.save_images_and_labels()
                
            else:
                print("\nAll images are verified.\n")
                self.images, self.labels = self.save_images_and_labels()
                
        else:
            print("\nDataset folder does not exist. Program will try to extract dataset contents.\n")
            if not self.check_winrar():
                print("\nWinRAR application is either not installed in or not in the PATH variables of your system.")
                print("Please install WinRAR from here: https://www.win-rar.com/start.html?&L=0, and add it to PATH variables of your computer.")
                self.is_dataset_suitable = False
                return
            
            self.clear_dataset()
            self.extract_dataset()
            self.image_count = self.get_dataset_item_counts()
            self.images, self.labels = self.save_images_and_labels()
            
        self.TEST_RATIO = test_ratio
        self.X_train, self.X_test, self.Y_train, self.Y_test = self.split_images()
        
        return
    
    def extract_dataset(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        first_rar_file_name = self.rars[0]
        starting_rar_path = os.path.join(self.dataset_path, first_rar_file_name)
        command = ["winrar", "x", "-ibck", starting_rar_path, self.dataset_folder_path]
        
        try:
            with tqdm.tqdm(desc="Extracting Dataset Files... ", unit=" items", total=self.total_items_in_rars, 
                           bar_format="{desc}{percentage:3.2f}% |{bar}| {n_fmt}/{total_fmt} [{elapsed} < {remaining}, {rate_fmt}{postfix}]") as progress_bar:
                if not os.path.exists(self.dataset_folder_path):
                    os.makedirs(self.dataset_folder_path)
                    needed_blank_count = self.longest_path_size - len("images/")
                    desc = "Extracting Dataset Files: (images/)" + ' ' * needed_blank_count
                    progress_bar.set_description(desc)
                    
                progress_bar.update(1)
                
                self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                last_file_count = 0
                
                last_folder_collection = []
                last_file_collection_size = 0
                current_index = ''
                current_label = ''
                
                while self.process.poll() is None:
                    current_folder_collection = os.listdir(self.dataset_folder_path)
                    if current_folder_collection != last_folder_collection:
                        for index in range(len(current_folder_collection)):
                            try:
                                if current_folder_collection[index] != last_folder_collection[index]:
                                    current_label = current_folder_collection[index]
                                    current_index = index
                                    break
                                
                            except IndexError:
                                current_label = current_folder_collection[index]
                                current_index = index
                                break
                            
                        last_folder_collection = current_folder_collection
                        
                    current_folder_path = os.path.join(self.dataset_folder_path, current_label)
                    current_file_collection = os.listdir(current_folder_path)
                    current_file_collection_size = len(current_file_collection)
                    if last_file_collection_size != current_file_collection_size:
                        if current_file_collection_size != 0:
                            current_file = current_file_collection[-1]
                            
                        else:
                            current_file = ''
                            
                        file_text_path = f"{current_label}/{current_file}"
                        needed_blank_count = self.longest_path_size - len(file_text_path)
                        desc = f"Extracting Dataset Files... (images/{file_text_path})" + ' ' * needed_blank_count
                        progress_bar.set_description(desc)
                        last_file_collection_size = current_file_collection_size
                        
                    current_file_count = sum(len(files) for root, dirs, files in os.walk(self.dataset_folder_path))
                    progress_bar.update(current_file_count - last_file_count)
                    last_file_count = current_file_count
                    
                progress_bar.set_description("Extracted Dataset Files. ")
                
        except KeyboardInterrupt:
            self.terminate_rar_process()
            
        return
    
    def terminate_rar_process(self):
        try:
            process_id = self.process.pid
            parent_process = psutil.Process(process_id)
            children_processes = parent_process.children(recursive=True)
            for child_process in children_processes:
                child_process.terminate()
                
            dead, alive = psutil.wait_procs(children_processes, timeout=5)
            for child_process in alive:
                child_process.kill()
                
            self.process.terminate()
            self.process.wait()
            
        except psutil.NoSuchProcess:
            print("No WinRaR process is found.")
            
        print("Stopped extraction.")
        
    def count_rars(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        rars = []
        for file in os.listdir(self.dataset_path):
            if file.endswith(".rar"):
                rars.append(file)
                
        total_rar_count = len(rars)
        
        total_files = 0
        longest_path_size = 0
        with tqdm.tqdm(desc="Reading RAR Files... ", unit=" items", total=total_rar_count, 
                       bar_format="{desc}{percentage:3.2f}% |{bar}| {n_fmt}/{total_fmt} [{elapsed} < {remaining}, {rate_fmt}{postfix}]") as progress_bar:
            for rar in rars:
                rar_path = os.path.join(self.dataset_path, rar)
                command = ["rar", "l", rar_path]
                result = subprocess.run(command, capture_output=True, text=True, check=True, encoding="latin-1")
                items = result.stdout.split('\n')
                size, item_count = items[-3].split()
                current_rar_item_count = int(item_count)
                total_files += current_rar_item_count
                
                desc = f"Reading RAR Files... ({rar}), Total File Count: ({total_files})"
                progress_bar.set_description(desc)
                

                for index, item in enumerate(items):
                    if index - self.RAR_FILE_INFORMATION_LINE_COUNT_OFFSET == current_rar_item_count + 1:
                        break
                    
                    if index >= self.RAR_FILE_INFORMATION_LINE_COUNT_OFFSET + 1:
                        line = item.split()
                        attributes, size, date, time, name = line
                        size_of_path = len(name)
                        longest_path_size = max(longest_path_size, size_of_path)
                        
                progress_bar.update(1)

            progress_bar.set_description("Read RAR Files. ")
                
        return rars, total_files + 1, longest_path_size
    
    def check_winrar(self):
        return any(os.access(os.path.join(path, "winrar.exe"), os.X_OK) for path in os.environ["PATH"].split(os.pathsep))
    
    def clear_dataset(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        total_files, total_directories, longest_path_length = self.count_existing_files()
        total_items = total_files + total_directories
        with tqdm.tqdm(desc="Clearing Dataset Files... ", unit=" items", total=total_items, 
                       bar_format="{desc}{percentage:3.2f}% |{bar}| {n_fmt}/{total_fmt} [{elapsed} < {remaining}, {rate_fmt}{postfix}]") as progress_bar:
            for root, dirs, files in os.walk(self.dataset_folder_path, topdown=False):
                for name in files:
                    file_path = os.path.join(root, name)
                    os.remove(file_path)
                    file_path_words = file_path.split("\\")[-3:]
                    file_path_words_combined = '/'.join(file_path_words)
                    needed_blank_count = self.longest_path_size - len(file_path_words_combined)
                    desc = f"Clearing Dataset Files... ({file_path_words_combined})" + ' ' * needed_blank_count
                    progress_bar.set_description(desc)
                    progress_bar.update(1)
                    
                for name in dirs:
                    dir_path = os.path.join(root, name)
                    shutil.rmtree(dir_path)
                    dir_path_words = dir_path.split("\\")[-3:]
                    dir_path_words_combined = '/'.join(dir_path_words)
                    needed_blank_count = self.longest_path_size - len(dir_path_words_combined)
                    desc = f"Clearing Dataset Files... ({dir_path_words_combined})" + ' ' * needed_blank_count
                    progress_bar.set_description(desc)
                    progress_bar.update(1)
                    
            shutil.rmtree(self.dataset_folder_path)
            dataset_folder_name = self.dataset_folder_path.split("\\")[-1]
            dataset_folder_name_combined = dataset_folder_name + '/'
            needed_blank_count = self.longest_path_size - len(dataset_folder_name_combined)
            desc = f"Clearing Dataset Files... ({dataset_folder_name_combined})" + ' ' * needed_blank_count
            progress_bar.set_description(desc)
            progress_bar.update(1)
            
            progress_bar.set_description("Cleared Dataset Files. ")
            
        return
        
    def count_existing_files(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        total_files = 0
        total_directories = 0
        longest_path_size = 0
        for root, dirs, files in os.walk(self.dataset_folder_path):
            total_files += len(files)
            total_directories += len(dirs)
            for file in files:
                file_path_words = os.path.join(root, file).split("\\")[-3:]
                file_path = '/'.join(file_path_words)
                longest_path_size = max(longest_path_size, len(file_path))
                
        return total_files, total_directories + 1, longest_path_size
    
    def get_dataset_item_counts(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        image_count = 0
        folder_count = 0
        longest_path_length = 0
        for root, dirs, files in os.walk(self.dataset_folder_path):
            for file in files:
                if not file.endswith(".png"):
                    continue
                
                image_count += 1
                
            folder_count += 1
            
        return image_count, folder_count
        
    def save_images_and_labels(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        images = []
        labels = []
        
        with tqdm.tqdm(desc="Importing Images... ", unit=" items", total=self.total_items_in_dataset) as progress_bar:
            for root, dirs, files in os.walk(self.dataset_folder_path):
                for file in files:
                    if not file.endswith(".png"):
                        continue
                
                    image_path = os.path.join(root, file)
                    image_name = '/'.join(image_path.split('\\')[-3:])
                    
                    image_data_as_array = numpy.fromfile(image_path, dtype=numpy.uint8)
                    image = cv2.imdecode(image_data_as_array, cv2.IMREAD_UNCHANGED)
                    label = str(os.path.join(root, file)).split('\\')[-2]
                    
                    images.append(image)
                    labels.append(label)
                    
                    file_path_text = f"{label}/{file}"
                    needed_blank_count = self.longest_path_size - len(file_path_text)
                    desc = f"Importing Images... ({image_name})" + ' ' * needed_blank_count
                    progress_bar.set_description(desc)
                    progress_bar.update(1)
                    
                progress_bar.update(1)
                    
            progress_bar.set_description("Imported Images. ")
            
        return images, labels
    
    def split_images(self):
        if not self.is_dataset_suitable:
            print("Dataset is not suitable for model training or testing. Please use a specific dataset.")
            return
        
        X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(self.images, self.labels, test_size=self.TEST_RATIO)
        return X_train, X_test, Y_train, Y_test
    