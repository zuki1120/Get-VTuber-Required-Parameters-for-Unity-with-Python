import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

data_filepath = './Data/'
analyze_filepath = './offset_analyze'
file = os.listdir(data_filepath)
for f in os.listdir(data_filepath):
    
    info = os.path.join(data_filepath, f)
    data = pd.read_csv(info, header = None)
    data.columns = ['roll', 'pitch', 'yaw',
                    'ear_left', 'ear_right',
                    'x_ratio_left', 'y_ratio_left',
                    'x_ratio_right', 'y_ratio_right',
                    'mar', 'mouth_distance']
    r_counter, c_counter = data.shape
    data['frame'] = range(0, r_counter)
    
    f_name = f.replace('.mp4.csv', '')
    plt.style.use('ggplot')

    for i in range(data.shape[1] - 1):
        #print(data.iloc[:, [i]])
        #print(data.columns[i])
        plt.plot(data['frame'], data[data.columns[i]])  
        plt.xlabel("frame", fontweight = "bold")
        plt.ylabel("offset", fontweight = "bold")
        plt.title(data.columns[i])
        offset_filepath = os.path.join(analyze_filepath, f'{f_name}/')
        if not os.path.isdir(offset_filepath):
            os.mkdir(offset_filepath)
        plt.savefig(os.path.join(offset_filepath, f'{f_name}_{data.columns[i]}.jpg'),
                    bbox_inches = 'tight',
                    pad_inches = 0.0)
        plt.close()

def compare(folder_path, target):
    list2dataframe = []
    compare_f = []
    count = 0
    for f in os.listdir(folder_path):
        path_file = os.path.join(folder_path, f)
        compare_data = pd.read_csv(path_file, header = None)
        compare_data.columns = ['roll', 'pitch', 'yaw',
                    'ear_left', 'ear_right',
                    'x_ratio_left', 'y_ratio_left',
                    'x_ratio_right', 'y_ratio_right',
                    'mar', 'mouth_distance']
        compare_r, compare_c = compare_data.shape
        compare_data['frame'] = range(0, compare_r)
        compare_f.append(f.replace('.mp4.csv', ''))
        count + 1
        list2dataframe.append(compare_data)

    for i in range(11):
        fig, ax = plt.subplots()
        for j in range(len(list2dataframe)):
            ax.plot(list2dataframe[j]['frame'], list2dataframe[j][compare_data.columns[i]], label = compare_f[j])
        
        ax.set_xlabel('frame')
        ax.set_ylabel('offset')
        ax.set_title(compare_data.columns[i])
        ax.legend()

        offset_filepath = os.path.join(analyze_filepath, f'{target}_compare/')
        if not os.path.isdir(offset_filepath):
            os.mkdir(offset_filepath)
        plt.savefig(os.path.join(offset_filepath, f'compare_{compare_data.columns[i]}.jpg'),
                    bbox_inches = 'tight',
                    pad_inches = 0.0)
        plt.close()

compare('./Data/', target = 'happy')