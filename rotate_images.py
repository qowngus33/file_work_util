"""
Rotate Images by 90 degrees clockwise
"""
import numpy as np
import cv2
import os
from tqdm import tqdm
from file_to_list import file_to_list_func

if __name__ == "__main__":
    path = "/Volumes/NONAME/construction_dataset/0803(O)/"
    folder = "Gram/"
    save_folder = "Rotated_Gram/"

    f = open("label.txt", "r")

    folder_names_list = []
    while True:
        line = f.readline().strip().split(" ")
        if line[0] != "":
            folder_names_list.append(line[0])
        else:
            break

    folder_names_list = list(set(folder_names_list))
    print(folder_names_list)
    print(len(folder_names_list))

    for i in tqdm(range(len(folder_names_list))):
        os.chdir(path+folder+folder_names_list[i])  # 해당 폴더로 이동
        files = os.listdir(path+folder+folder_names_list[i])  # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음
        files.sort()
        for j, file in enumerate(tqdm(files)):
            img = cv2.imread(file)
            if not os.path.exists(path+save_folder+folder_names_list[i].zfill(4)):
                os.mkdir(path+save_folder+folder_names_list[i].zfill(4))
            img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            try:
                cv2.imwrite(path+save_folder+folder_names_list[i].zfill(4)+"/"+file, img90)
            except:
                print(file)

