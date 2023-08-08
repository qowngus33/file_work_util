"""
Split files by 8:2 ratio train:valid
"""
import numpy as np
import cv2
import os
from tqdm import tqdm
import shutil
import random

if __name__ == "__main__":
    path = "/Volumes/NONAME/Trouser_dataset/"
    folder = "images_and_label/"

    os.chdir(path+folder)  # 해당 폴더로 이동
    files = os.listdir(path+folder)  # 해당 폴더에 있는 파일 이름을 리스트 형태로 받음
    files.sort()

    labels = []
    for j, file in enumerate(tqdm(files)):
        if "txt" in file:
            labels.append(file)
    random.shuffle(labels)

    for txt in tqdm(labels[:len(labels)*4//5]):
        shutil.copy(txt, path+"train/labels/")
        img = cv2.imread(txt[:-3]+"jpg")
        cv2.imwrite(path + "train/images/" + txt[:-3]+"jpg", img)

    for txt in tqdm(labels[len(labels)*4//5:]):
        shutil.copy(txt, path+"valid/labels/")
        img = cv2.imread(txt[:-3]+"jpg")
        cv2.imwrite(path + "valid/images/" + txt[:-3]+"jpg", img)
