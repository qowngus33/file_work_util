"""
Merge Yolo txt label files together
"""
import numpy as np
import cv2
import os
from tqdm import tqdm
from file_to_list import file_to_list_func

if __name__ == "__main__":
    path = "/Volumes/NONAME/"
    folder = "VIG_Test_data/"

    trouser_files = os.listdir(path+folder+"trouser-labels/")

    trouser_labels = []
    for file in trouser_files:
        if "txt" in file:
            trouser_labels.append(file)
    print(len(trouser_labels))
    trouser_labels.sort()

    cnt = 0
    for i in tqdm(range(len(trouser_labels))):
        new_lines = ""
        with open(path+folder+"trouser-labels/"+f"{trouser_labels[i]}", 'r') as f:
            lines = f.readlines()
            for k in lines:
                k = k.rstrip()
                content = k.split(' ')
                # content[0] = str(int(content[0])+15)
                if content[0] == "15":
                    new_lines += (" ".join(content)+'\n')

        try:
            with open(path+folder+"labels/"+f"{trouser_labels[i]}", 'r') as lf:
                lines = lf.readlines()
                for k in lines:
                    k = k.rstrip()
                    content = k.split(' ')
                    # if content[0] == '14':
                    #     content[0] = '7'  # 7 for construction dataset 15 for lab dataset
                    # if content[0] != "0":
                    #     content[0] = str(int(content[0])-1)
                    new_lines += (" ".join(content)+'\n')
        except:
            print(path+folder+"labels/"+f"{trouser_labels[i]}")
        with open(path + folder + "new_labels/" + f"{trouser_labels[i]}", "w") as wf:
            wf.write(new_lines)
