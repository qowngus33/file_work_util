"""
Read Yolo txt label and change specific label
"""
import numpy as np
import cv2
import os
from tqdm import tqdm
from file_to_list import file_to_list_func

if __name__ == "__main__":
    path = "/Volumes/NONAME/additional_lab_dataset/0718_add/"
    folder = "labels/"

    files = os.listdir(path+folder)

    labels = []
    for file in files:
        if "txt" in file:
            labels.append(file)
    print(len(labels))
    labels.sort()

    cnt = 0
    for i in tqdm(range(len(labels))):
        new_lines = ""
        with open(path+folder+f"{labels[i]}", 'r') as f:
            lines = f.readlines()
            for k in lines:
                k = k.rstrip()
                content = k.split(' ')
                # 7 : Latex Gloves
                # 9 : No Gloves
                # 14 : Work Gloves
                if content[0] == '9' or content[0] == '14':
                    content[0] = '7'
                new_lines += (" ".join(content) + '\n')

        with open(path + folder + f"{labels[i]}", "w") as wf:
            wf.write(new_lines)
