import numpy as np
import cv2
import os
from tqdm import tqdm
from file_to_list import file_to_list_func

if __name__ == "__main__":
    path = "/Volumes/SANDISK123/foot_eye_data/eye_data/train_valid/"
    folder = "glasses/"

    files = []
    txt = []
    jpg = []

    os.chdir(path+folder)  # 해당 폴더로 이동
    files = os.listdir(path+folder)  # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음
    for file in tqdm(files):
        if file.find("jpg") != -1:
            img = cv2.imread(file)
            h, w, c = img.shape
            if w < 50:
                jpg.append(file)

    jpg.sort()
    print(len(jpg))
    for img in jpg:
        print(img, end=" ")
