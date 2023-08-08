import numpy as np
import cv2
import os
from tqdm import tqdm
from file_to_list import file_to_list_func

if __name__ == "__main__":
    path = "/Volumes/NONAME/construction_dataset/"
    save_path = "/Volumes/NONAME/Trouser_dataset/images_and_label/"
    folder = "0718(Lab)(F)/labels/"

    files = os.listdir(path+folder)

    labels = []
    for file in files:
        if "txt" in file:
            labels.append(file)
    print(len(labels))
    labels.sort()

    cnt = 0
    for i in range(len(labels)):
        with open(path + folder + f"{labels[i]}", 'r') as f:
            lines = f.readlines()
            new_lines = ""
            for k in lines:
                k = k.rstrip()
                content = k.split(' ')
                if content[0] == '15':
                    content[0] = '0'
                    new_lines = (" ".join(content)+'\n')
                    break

        with open(save_path + f"{labels[i]}", "w") as f:
            f.write(new_lines)
